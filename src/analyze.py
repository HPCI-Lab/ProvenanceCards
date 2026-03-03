import argparse
import json
import sys
from pathlib import Path

import pandas as pd

from utils import (
    factual_coverage_score,
    hallucination_rate,
    semantic_consistency,
    rouge_l,
    tokens_to_coverage,
    chunk_count_sensitivity,
    attribute_extraction_accuracy,
    provenance_card_delta,
)


from utils import detect_schema, checklist_for_schema, FLOWCEPT_WORKFLOW_KEYS, FLOWCEPT_MACHINE_KEYS, FLOWCEPT_TASK_KEYS, YPROV_ACTIVITY_KEYS, YPROV_ENTITY_KEYS

def load_output(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)

def _load_jsonl(path: str) -> list[dict]:
    """Load a .jsonl file into a list of dicts, skipping blank lines."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return records


def _flatten_dict(d: dict, prefix: str = "", sep: str = ".") -> dict:
    """Recursively flatten a nested dict into dot-notation keys."""
    out = {}
    for k, v in d.items():
        key = f"{prefix}{sep}{k}" if prefix else k
        if isinstance(v, dict):
            out.update(_flatten_dict(v, key, sep))
        else:
            out[key] = v
    return out


# ---------------------------------------------------------------------------
# FlowCept (_F.jsonl) extraction
# ---------------------------------------------------------------------------

def _extract_flowcept(records: list[dict]) -> dict:
    """
    Extract ground-truth provenance attributes from a FlowCept JSONL record set.
    Pulls from the workflow record (record[0]) and all task records.
    """
    attrs = {}
    workflow = next((r for r in records if r.get("type") == "workflow"), records[0])

    # Top-level workflow fields
    for k in FLOWCEPT_WORKFLOW_KEYS:
        if k in workflow:
            attrs[k] = workflow[k]

    # Nested machine_info — flatten and pull known keys
    machine_flat = {}
    for interceptor_id, minfo in workflow.get("machine_info", {}).items():
        machine_flat.update(_flatten_dict(minfo))
    for k in FLOWCEPT_MACHINE_KEYS:
        leaf = k.split(".")[-1]
        # Try dot-notation first, then leaf key
        val = machine_flat.get(k) or machine_flat.get(leaf)
        if val is not None:
            attrs[f"machine.{k}"] = val

    # Summarise tasks
    tasks = [r for r in records if r.get("type") == "task"]
    attrs["total_tasks"] = len(tasks)
    attrs["activity_ids"] = list({t.get("activity_id") for t in tasks if t.get("activity_id")})

    # Process info from first task
    if tasks:
        t0 = tasks[0]
        proc = t0.get("telemetry_at_start", {}).get("process", {})
        for k in ["pid", "executable", "cmd_line", "num_threads"]:
            if k in proc:
                attrs[f"process.{k}"] = proc[k]
        if "generated" in t0 and t0["generated"]:
            attrs["generated_keys"] = list(t0["generated"].keys())

    return attrs


def _flowcept_to_reference(attrs: dict, source_path: str) -> str:
    """Render FlowCept attributes as a readable reference description."""
    lines = [
        f"Source file: {source_path}",
        f"Schema: FlowCept workflow provenance",
        "",
        "## Workflow Identity",
    ]
    for k in ["workflow_id", "campaign_id", "name", "user", "utc_timestamp", "flowcept_version"]:
        if k in attrs:
            lines.append(f"- {k}: {attrs[k]}")

    lines.append("\n## Execution Environment")
    for k, v in attrs.items():
        if k.startswith("machine."):
            lines.append(f"- {k.replace('machine.', '')}: {v}")

    lines.append("\n## Tasks")
    lines.append(f"- total_tasks: {attrs.get('total_tasks', 'unknown')}")
    lines.append(f"- activity_ids: {attrs.get('activity_ids', [])}")

    lines.append("\n## Process")
    for k, v in attrs.items():
        if k.startswith("process."):
            lines.append(f"- {k.replace('process.', '')}: {v}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# yProv4ML (_Y.json) extraction
# ---------------------------------------------------------------------------

def _parse_entity_value(raw: str):
    """Try to parse a prov:value string as Python literal or return as-is."""
    import ast
    try:
        return ast.literal_eval(raw)
    except Exception:
        return raw


def _extract_yprov(data: dict) -> dict:
    """
    Extract ground-truth provenance attributes from a yProv4ML JSON document.
    """
    attrs = {}

    # Agent
    agents = list(data.get("agent", {}).keys())
    if agents:
        attrs["agent"] = agents[0]

    # Main activity (the run_ entry)
    for act_name, act_val in data.get("activity", {}).items():
        if isinstance(act_val, dict) and "yprov:experiment_name" in act_val:
            attrs["activity_name"] = act_name
            for k in YPROV_ACTIVITY_KEYS:
                if k in act_val:
                    v = act_val[k]
                    # Unwrap {$: val, type: xsd:int} pattern
                    if isinstance(v, dict) and "$" in v:
                        v = v["$"]
                    attrs[k] = v
            break

    # Sub-activities (Inspect, Infer, Propose, Generation, apple_gpu/*)
    sub_activities = {}
    for act_name, act_val in data.get("activity", {}).items():
        if isinstance(act_val, dict) and "prov:startedAtTime" in act_val:
            sub_activities[act_name] = act_val.get("prov:startedAtTime")
    if sub_activities:
        attrs["workflow_steps"] = list(sub_activities.keys())

    # Entities: core dataset provenance
    entities = data.get("entity", {})
    for k in YPROV_ENTITY_KEYS:
        if k in entities:
            raw = entities[k].get("prov:value", "")
            attrs[f"entity.{k}"] = _parse_entity_value(raw) if raw else None

    # GPU telemetry entity summary
    gpu_steps = {k for k in entities if k.startswith("apple_gpu/")}
    if gpu_steps:
        attrs["gpu_telemetry_steps"] = sorted(gpu_steps)

    return attrs


def _yprov_to_reference(attrs: dict, source_path: str) -> str:
    """Render yProv4ML attributes as a readable reference description."""
    lines = [
        f"Source file: {source_path}",
        f"Schema: yProv4ML (W3C PROV-DM)",
        "",
        "## Experiment Identity",
    ]
    for k in ["yprov:experiment_name", "yprov:run_id", "yprov:PID", "yprov:global_rank", "agent"]:
        if k in attrs:
            lines.append(f"- {k}: {attrs[k]}")

    lines.append("\n## Timing")
    for k in ["prov:startedAtTime", "prov:endedAtTime"]:
        if k in attrs:
            lines.append(f"- {k}: {attrs[k]}")

    lines.append("\n## Workflow Steps")
    lines.append(f"- steps: {attrs.get('workflow_steps', [])}")

    lines.append("\n## Dataset Provenance")
    for k, v in attrs.items():
        if k.startswith("entity."):
            label = k.replace("entity.", "")
            display = json.dumps(v) if isinstance(v, (list, dict)) else str(v)
            lines.append(f"- {label}: {display[:200]}")

    lines.append("\n## Environment")
    for k in ["yprov:python_version", "yprov:provenance_path", "yprov:artifact_uri"]:
        if k in attrs:
            lines.append(f"- {k}: {attrs[k]}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Public API: compute reference + ground truth from a saved output file
# ---------------------------------------------------------------------------

def compute_reference_from_source(file: str) -> str:
    """
    Derive a reference description from the benchmark output JSON.
    Dispatches to the correct schema handler based on the source file name.
    """
    meta        = json.load(open(file))
    source_path = meta["input_file"]
    schema      = detect_schema(source_path)

    if schema == "flowcept":
        records = _load_jsonl(source_path)
        attrs   = _extract_flowcept(records)
        return _flowcept_to_reference(attrs, source_path)

    elif schema == "yprov":
        data  = json.load(open(source_path))
        attrs = _extract_yprov(data)
        return _yprov_to_reference(attrs, source_path)

    else:
        # Fallback: use source_text captured during the benchmark run
        return meta.get("source_text", f"Source file: {source_path} (unknown schema)")


def compute_ground_truth_attrs_from_source(file: str) -> dict:
    """
    Derive a ground-truth attribute dict from the benchmark output JSON.
    Returns a flat {str: any} dict suitable for attribute_extraction_accuracy().
    """
    meta        = json.load(open(file))
    source_path = meta["input_file"]
    schema      = detect_schema(source_path)

    if schema == "flowcept":
        records = _load_jsonl(source_path)
        return _extract_flowcept(records)

    elif schema == "yprov":
        data = json.load(open(source_path))
        return _extract_yprov(data)

    else:
        return {"source_path": source_path, "schema": "unknown"}


def group_by_file(output_files: list[Path]) -> dict[str, list[Path]]:
    """Group output JSON paths by the input file they describe."""
    groups: dict[str, list[Path]] = {}
    for p in output_files:
        groups.setdefault(p, []).append(p)
    return groups


def analyze_single(data: dict,reference: str | None,ground_truth_attrs: dict | None,checklist: list[str] | None) -> dict:
    metrics = {}

    # 1. Factual coverage
    metrics["factual_coverage"] = factual_coverage_score(
        data["final_description"], checklist
    )

    # 2. Hallucination rate
    metrics["hallucination"] = hallucination_rate(
        data["final_description"], data["source_text"]
    )

    # 3. Semantic consistency across chunks
    if len(data["chunk_summaries"]) >= 2:
        metrics["semantic_consistency"] = semantic_consistency(data["chunk_summaries"])
    else:
        metrics["semantic_consistency"] = {"mean_similarity": None, "note": "single chunk"}

    # 4 & 5. ROUGE-L + tokens-to-coverage (need reference)
    if reference:
        metrics["rouge_l"] = rouge_l(data["final_description"], reference)
        metrics["tokens_to_coverage"] = tokens_to_coverage(
            data["chunk_summaries"],
            data["chunk_token_counts"],
            checklist,
        )
    else:
        metrics["rouge_l"]             = {"note": "no reference provided"}
        metrics["tokens_to_coverage"]  = {"note": "no reference provided"}

    # 6. Attribute extraction accuracy (needs ground truth dict)
    if ground_truth_attrs:
        # Ask the model description to "answer" via simple key scanning
        extracted = {
            k: data["final_description"]
            for k in ground_truth_attrs
            if k.lower() in data["final_description"].lower()
        }
        metrics["attribute_extraction"] = attribute_extraction_accuracy(
            extracted, ground_truth_attrs
        )
    else:
        metrics["attribute_extraction"] = {"note": "no ground truth provided"}

    return metrics


def analyze_card_delta(outputs_without: list[dict],outputs_with: list[dict],reference: str,checklist: list[str] | None) -> list[dict]:
    """
    Compare paired outputs (same model, same file) with and without a
    provenance card prepended.

    Expects outputs_without and outputs_with to be ordered identically
    (same model order).
    """
    deltas = []
    for wo, wi in zip(outputs_without, outputs_with):
        assert wo["model_name"] == wi["model_name"], "Model mismatch in card delta pairs"
        delta = provenance_card_delta(
            wo["final_description"],
            wi["final_description"],
            reference,
            checklist,
        )
        deltas.append({"model": wo["model_name"], **delta})
    return deltas



def analyze_chunk_sensitivity(outputs_by_file: dict[str, list[dict]], reference: str) -> dict[str, dict]:
    per_model: dict[str, dict[int, str]] = {}
    for _file_stem, file_outputs in outputs_by_file.items():
        for data in file_outputs:
            model = data["model_name"]
            n     = data["num_chunks"]
            per_model.setdefault(model, {})[n] = data["final_description"]

    results = {}
    for model, mapping in per_model.items():
        results[model] = chunk_count_sensitivity(mapping, reference)
    return results


def build_summary_df(all_metrics: dict[str, dict[str, dict]]) -> pd.DataFrame:
    rows = []
    for file_stem, model_metrics in all_metrics.items():
        for model_name, metrics in model_metrics.items():
            row = {"file": file_stem, "model": model_name}

            cov = metrics.get("factual_coverage", {})
            row["coverage_score"] = cov.get("score")
            row["coverage_found"] = len(cov.get("found", []))
            row["coverage_missing"] = len(cov.get("missing", []))

            hal = metrics.get("hallucination", {})
            row["hallucination_rate"] = hal.get("rate")
            row["unsupported_claims"] = len(hal.get("unsupported_claims", []))
            row["total_claims"] = hal.get("total_claims")

            sem = metrics.get("semantic_consistency", {})
            row["semantic_mean_sim"] = sem.get("mean_similarity")
            row["semantic_min_sim"] = sem.get("min_similarity")

            rl  = metrics.get("rouge_l", {})
            row["rouge_l_f1"] = rl.get("f1")
            row["rouge_l_precision"] = rl.get("precision")
            row["rouge_l_recall"] = rl.get("recall")

            ttc = metrics.get("tokens_to_coverage", {})
            row["tokens_at_threshold"] = ttc.get("tokens_at_threshold")
            row["chunk_at_threshold"] = ttc.get("chunk_at_threshold")

            ae  = metrics.get("attribute_extraction", {})
            row["attr_accuracy"] = ae.get("accuracy")

            rows.append(row)

    return pd.DataFrame(rows)

def main():
    parser = argparse.ArgumentParser(description="A-posteriori provenance card benchmark analysis")
    parser.add_argument("run", help="Path to a specific run folder (default: latest)")
    parser.add_argument("--outputs-root", default="outputs", help="Root folder containing run subfolders")
    parser.add_argument("--save-csv", default="analysis_results.csv", help="Where to save the summary CSV")
    args = parser.parse_args()

    run_dir = Path(args.run)
    print(f"🔍 Analysing run: {run_dir}")

    # Discover all model output JSON files in the run folder
    output_files = sorted(run_dir.glob("*.json"))
    if not output_files:
        sys.exit(f"No output JSON files found in {run_dir}")

    print(f"📂 Found {len(output_files)} output file(s)")

    # Group by input file
    file_groups = group_by_file(output_files)
    all_outputs_by_file: dict[str, list[dict]] = {
        stem: [load_output(p) for p in paths]
        for stem, paths in file_groups.items()
    }

    all_metrics: dict[str, dict[str, dict]] = {}

    for file_stem, outputs in all_outputs_by_file.items():
        print(f"File: {file_stem}")
        all_metrics[file_stem] = {}

        reference = compute_reference_from_source(file_stem)
        ground_truth_attrs = compute_ground_truth_attrs_from_source(file_stem)
        schema = detect_schema(json.load(open(file_stem))["input_file"])
        checklist = checklist_for_schema(schema)

        for data in outputs:
            model = data["model_name"]
            print(f"\n  ▶ {model}")
            metrics = analyze_single(data, reference, ground_truth_attrs, checklist)
            all_metrics[file_stem][model] = metrics

            # Pretty-print key numbers
            cov = metrics["factual_coverage"]
            hal = metrics["hallucination"]
            sem = metrics["semantic_consistency"]
            print(f"    Coverage:       {cov['score']:.2%}  (found: {cov['found']})")
            print(f"    Hallucination:  {hal['rate']:.2%}  ({hal['unsupported_claims'].__len__()} unsupported / {hal['total_claims']} claims)")
            if sem.get("mean_similarity") is not None:
                print(f"    Consistency:    mean={sem['mean_similarity']:.3f}  min={sem['min_similarity']:.3f}")
            if reference:
                rl = metrics["rouge_l"]
                print(f"    ROUGE-L F1:     {rl['f1']:.4f}")
                ttc = metrics["tokens_to_coverage"]
                print(f"    Tokens→coverage: {ttc.get('tokens_at_threshold', 'N/A')} tokens")


    if reference and len(all_outputs_by_file) > 1:
        print("Chunk Count Sensitivity")
        sensitivity = analyze_chunk_sensitivity(all_outputs_by_file, reference)
        for model, s in sensitivity.items():
            slope = s.get("degradation_slope")
            direction = "↓ degrading" if (slope is not None and slope < 0) else "↑ improving / stable"
            print(f"  {model:30s}  slope={slope}  ({direction})")

    summary_df = build_summary_df(all_metrics)
    csv_out = run_dir / args.save_csv
    summary_df.to_csv(csv_out, index=False)

    print(f"\n📊 Summary CSV saved to {csv_out}")


if __name__ == "__main__":
    main()
