import argparse
import json
import sys
from pathlib import Path

import pandas as pd

from metrics import (
    factual_coverage_score,
    hallucination_rate,
    semantic_consistency,
    rouge_l,
    tokens_to_coverage,
    chunk_count_sensitivity,
    attribute_extraction_accuracy,
    provenance_card_delta,
    distinct_n,
    self_bleu,
    calculate_perplexity,
    calculate_log_likelihood,
    calculate_bleu_multi_ref,
    calculate_bleu,
)
from extraction import *


def group_by_file(output_files: list[Path]) -> dict[str, list[Path]]:
    """Group output JSON paths by the input file they describe."""
    groups: dict[str, list[Path]] = {}
    for p in output_files:
        groups.setdefault(p, []).append(p)
    return groups


def analyze_single(data: dict,reference: str | None,ground_truth_attrs: dict | None,checklist: list[str] | None) -> dict:
    metrics = {}

    metrics["factual_coverage"] = factual_coverage_score(data["final_description"], checklist)
    metrics["hallucination"] = hallucination_rate(data["final_description"], data["source_text"])

    if len(data["chunk_summaries"]) >= 2:
        metrics["semantic_consistency"] = semantic_consistency(data["chunk_summaries"])
    else:
        metrics["semantic_consistency"] = {"mean_similarity": None, "note": "single chunk"}

    metrics["rouge_l"] = rouge_l(data["final_description"], reference)
    metrics["tokens_to_coverage"] = tokens_to_coverage(data["chunk_summaries"],data["chunk_token_counts"],checklist)

    extracted = {
        k: data["final_description"]
        for k in ground_truth_attrs
        if k.lower() in data["final_description"].lower()
    }
    metrics["attribute_extraction"] = attribute_extraction_accuracy(extracted, ground_truth_attrs)

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
        stem: [json.load(open(p)) for p in paths]
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
