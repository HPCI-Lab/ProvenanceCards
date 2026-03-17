import argparse
import json
import sys
from pathlib import Path
import sklearn
import pandas as pd

from metrics import (
    factual_coverage_score,
    hallucination_rate,
    semantic_consistency,
    rouge_l,
    chunk_count_sensitivity,
    distinct_n,
    self_bleu,
    # calculate_perplexity,
    # calculate_log_likelihood,
    calculate_bleu_multi_ref,
    calculate_bleu,
)
from extraction import *
from utils import _load_jsonl, _load_md

def group_by_file(output_files: list[Path]) -> dict[str, list[Path]]:
    """Group output JSON paths by the input file they describe."""
    groups: dict[str, list[Path]] = {}
    for p in output_files:
        groups.setdefault(p, []).append(p)
    return groups


def analyze_single(data: dict, source_file : str,reference: str | None, ground_truth_attrs: dict | None, checklist : list[str]) -> dict:
    metrics = {}
    
    if source_file.endswith(".json"): 
        source_file = str(json.load(open(source_file, "r")))
    elif source_file.endswith(".jsonl"):
        source_file = "\n".join([str(l) for l in _load_jsonl(source_file)])
    elif source_file.endswith(".md"):
        source_file = "\n".join(_load_md(source_file))

    source_coverage = factual_coverage_score(source_file, checklist)
    data_coverage = factual_coverage_score(data["final_description"], checklist)
    metrics["absolute_factual_coverage"] = data_coverage
    founds = [d for d in data_coverage["found"] if d in source_coverage["found"]]
    def compute_f1vector(found, checklist): 
        return [1 if c in found else 0 for c in checklist]
    f1vector_source = compute_f1vector(source_coverage["found"], checklist)
    f1vector_data = compute_f1vector(data_coverage["found"], checklist)
    metrics["relative_factual_coverage"] = {
        "score": len(founds) / len(source_coverage["found"]),
        "found": founds, 
        "f1": sklearn.metrics.f1_score(f1vector_data, f1vector_source)
    }
    # This tells me how many tokens are necessary for each covered word
    if len(data_coverage["found"]) > 0: 
        metrics["tokens_for_coverage"] = len(data["final_description"].split(" ")) / len(data_coverage["found"])
    else: 
        metrics["tokens_for_coverage"] = None

    metrics["hallucination"] = hallucination_rate(data["final_description"], data["source_text"])

    if len(data["chunk_summaries"]) >= 2:
        metrics["semantic_consistency"] = semantic_consistency(data["chunk_summaries"])
    else:
        metrics["semantic_consistency"] = {"mean_similarity": None, "note": "single chunk"}

    metrics["rouge_l"] = rouge_l(data["final_description"], reference)

    metrics["distinct_n"] = distinct_n(data["final_description"])
    metrics["self_bleu"] = self_bleu(data["final_description"])
    # metrics["calculate_perplexity"] = calculate_perplexity(data["final_description"])
    # metrics["calculate_log_likelihood"] = calculate_log_likelihood(data["final_description"])
    metrics["bleu_multi_ref"] = calculate_bleu_multi_ref(reference, data["final_description"])
    metrics["bleu"] = calculate_bleu(reference, data["final_description"])

    metrics["total_letters"] = len(data["final_description"])
    metrics["total_words"] = len(data["final_description"].split(" "))
    metrics["total_sentences"] = len(data["final_description"].split(". "))

    return metrics


def analyze_chunk_sensitivity(outputs_by_file: dict[str, list[dict]], reference: str) -> dict[str, dict]:
    per_model: dict[str, dict[int, str]] = {}
    for _, file_outputs in outputs_by_file.items():
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

            cov = metrics.get("absolute_factual_coverage", {})
            row["absolute_factual_coverage_score"] = cov.get("score")
            row["absolute_factual_coverage_found"] = len(cov.get("found", []))
            row["absolute_factual_coverage_missing"] = len(cov.get("missing", []))

            cov = metrics.get("relative_factual_coverage", {})
            row["relative_factual_coverage_score"] = cov.get("score")
            row["relative_factual_coverage_f1"] = cov.get("score")
            row["relative_factual_coverage_found"] = len(cov.get("found", []))

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

            row["tokens_for_coverage"] = metrics.get("tokens_for_coverage", 0.0)

            row["distinct_n"] = metrics.get("distinct_n", 0.0)
            row["self_bleu"] = metrics.get("self_bleu", 0.0)
            row["bleu_multi_ref"] =metrics.get("bleu_multi_ref", 0.0)
            row["bleu"] = metrics.get("bleu", 0.0)

            # metrics["calculate_perplexity"] = calculate_perplexity(data["final_description"])
            # metrics["calculate_log_likelihood"] = calculate_log_likelihood(data["final_description"])

            row["total_letters"] = metrics.get("total_letters", 0.0)
            row["total_words"] = metrics.get("total_words", 0.0)
            row["total_sentences"] = metrics.get("total_sentences", 0.0)

            rows.append(row)

    return pd.DataFrame(rows)


def main():
    parser = argparse.ArgumentParser(description="A-posteriori provenance card benchmark analysis")
    parser.add_argument("run", help="Path to a specific run folder (default: latest) or file")
    parser.add_argument("--outputs-root", default="outputs", help="Root folder containing run subfolders")
    parser.add_argument("--save-csv", default="analysis_results.csv", help="Where to save the summary CSV")
    args = parser.parse_args()

    run_dir = Path(args.run)
    print(f"🔍 Analysing run: {run_dir}")

    # Discover all model output JSON files in the run folder
    if run_dir.is_file(): 
        output_files = [run_dir]
        run_dir = run_dir.parents[0]
    else: 
        output_files = sorted(run_dir.glob("*.json"))
        if not output_files:
            sys.exit(f"No output JSON files found in {run_dir}")
        print(f"📂 Found {len(output_files)} output file(s)")

    # Group by input file
    file_groups = group_by_file(output_files)
    all_outputs_by_file: dict[str, list[dict]] = {
        stem: [json.load(open(p)) for p in paths]
        for stem, paths in file_groups.items()
    }

    all_metrics: dict[str, dict[str, dict]] = {}

    for file_stem, outputs in all_outputs_by_file.items():
        print(f"File: {file_stem}")
        all_metrics[file_stem] = {}

        reference = compute_reference_from_source(file_stem)
        ground_truth_attrs = compute_ground_truth_attrs_from_source(file_stem)
        source_file = json.load(open(file_stem))["input_file"]
        schema = detect_schema(source_file)
        checklist = checklist_for_schema(schema)

        for data in outputs:
            model = data["model_name"]
            print(f"\n  ▶ {model}")
            metrics = analyze_single(data, source_file, reference, ground_truth_attrs, checklist)
            all_metrics[file_stem][model] = metrics

            # Pretty-print key numbers
            acov = metrics["absolute_factual_coverage"]
            rcov = metrics["relative_factual_coverage"]
            hal = metrics["hallucination"]
            sem = metrics["semantic_consistency"]
            print(f" Abs Coverage:       {acov['score']:.2%}  (found: {acov['found']})")
            print(f" Rel Coverage:       {rcov['score']:.2%}  (found: {rcov['found']})")
            print(f" Rel Coverage F1:       {rcov['f1']:.2%}")
            print(f"    Hallucination:  {hal['rate']:.2%}  ({hal['unsupported_claims'].__len__()} unsupported / {hal['total_claims']} claims)")
            if sem.get("mean_similarity") is not None:
                print(f"    Consistency:    mean={sem['mean_similarity']:.3f}  min={sem['min_similarity']:.3f}")
            if reference:
                rl = metrics["rouge_l"]
                print(f"    ROUGE-L F1:     {rl['f1']:.4f}")
                print(f"    Tokens for coverage: {metrics["tokens_for_coverage"]} tokens")

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
