"""
utils.py — Metric functions for provenance card benchmark evaluation.
"""

import re
import numpy as np
from typing import Any
from collections import Counter


# ---------------------------------------------------------------------------
# Schema-aware provenance attribute definitions
# ---------------------------------------------------------------------------
# Two schemas are present in the source files:
#
#   FLOWCEPT (_F.jsonl)  — workflow + task telemetry records produced by FlowCept.
#     Record 0 is a "workflow" record; subsequent records are "task" records.
#
#   YPROV (_Y.json)      — W3C PROV-DM documents produced by yProv4ML.
#     Top-level sections: prefix, agent, activity, wasAssociatedWith, entity.
# ---------------------------------------------------------------------------

# FlowCept: keys that carry meaningful provenance from the workflow record
FLOWCEPT_WORKFLOW_KEYS = [
    "workflow_id",        # unique workflow run identifier
    "campaign_id",        # groups multiple workflow runs
    "name",               # workflow step name (Inspect, Infer, Propose, …)
    "user",               # OS user who executed the workflow
    "sys_name",           # host OS name
    "flowcept_version",   # FlowCept library version
    "utc_timestamp",      # workflow start timestamp (UTC epoch)
]

# FlowCept: keys from the nested machine_info block
FLOWCEPT_MACHINE_KEYS = [
    "platform.system",      # OS (Darwin, Linux, …)
    "platform.node",        # hostname
    "platform.release",     # OS release string
    "platform.machine",     # hardware architecture (arm64, x86_64, …)
    "platform.processor",   # processor type
    "cpu.brand_raw",        # CPU brand string (e.g. Apple M1 Max)
    "cpu.arch",             # CPU architecture class (ARM_8, …)
    "cpu.count",            # number of logical CPU cores
    "cpu.python_version",   # Python version string
    "memory.virtual.total", # total RAM in bytes
    "disk.total",           # total disk capacity in bytes
    "disk.used",            # disk space in use
]

# FlowCept: keys from each task record
FLOWCEPT_TASK_KEYS = [
    "task_id",        # unique task identifier
    "activity_id",    # logical activity name (e.g. _sample_file)
    "workflow_id",    # back-reference to parent workflow
    "started_at",     # task start timestamp (epoch)
    "status",         # completion status
    "used",           # data inputs consumed by the task
    "generated",      # data outputs produced by the task
]

# FlowCept: process-level keys inside telemetry_at_start.process
FLOWCEPT_PROCESS_KEYS = [
    "process.pid",          # process ID
    "process.executable",   # Python interpreter path
    "process.cmd_line",     # full command line used to launch the job
    "process.num_threads",  # thread count at task start
]

# All FlowCept keys flattened (used as the default checklist for _F.jsonl)
FLOWCEPT_ALL_KEYS = (
    FLOWCEPT_WORKFLOW_KEYS
    + FLOWCEPT_MACHINE_KEYS
    + FLOWCEPT_TASK_KEYS
    + FLOWCEPT_PROCESS_KEYS
)

# yProv4ML: keys from the main activity block
YPROV_ACTIVITY_KEYS = [
    "yprov:experiment_name",  # human-readable experiment label
    "yprov:run_id",           # integer run counter
    "yprov:python_version",   # Python version used during the run
    "yprov:PID",              # process UUID
    "yprov:global_rank",      # distributed rank (0 = master)
    "yprov:provenance_path",  # directory where provenance files are written
    "yprov:artifact_uri",     # URI of the run's artifact directory
    "yprov:experiment_dir",   # root experiment directory
    "prov:startedAtTime",     # ISO-8601 run start time
    "prov:endedAtTime",       # ISO-8601 run end time
]

# yProv4ML: entity keys (dataset-level provenance, stored as prov:value strings)
YPROV_ENTITY_KEYS = [
    "files",            # list of input files (path, name, suffix, size)
    "total_size",       # total input data size in bytes
    "formats",          # list of file extensions present
    "file_count",       # number of input files
    "modality",         # data modality (gridded, tabular, image, unknown, …)
    "likely_domain",    # inferred scientific/application domain
    "has_labels",       # whether labelled targets were detected
    "has_splits",       # whether train/test splits exist
    "sparsity",         # sparsity estimate (if applicable)
    "suggested_format", # recommended storage format (npz, parquet, …)
    "output_format",    # format chosen for the output artefact
    "pipeline_steps",   # ordered list of recommended ML pipeline steps
    "confidence",       # confidence level of the domain inference
    "notes",            # free-text notes / warnings from the discovery run
    "sample_data",      # sample of data structure / first-item keys
]

# yProv4ML: GPU telemetry entity prefixes (apple_gpu/metric/step)
YPROV_GPU_METRIC_KEYS = [
    "apple_gpu/cpu_usage",
    "apple_gpu/memory_usage",
    "apple_gpu/disk_usage",
    "apple_gpu/gpu_memory_power",
    "apple_gpu/gpu_memory_usage",
    "apple_gpu/gpu_usage",
    "apple_gpu/gpu_power_usage",
    "apple_gpu/gpu_temperature",
]

# All yProv keys flattened (used as the default checklist for _Y.json)
YPROV_ALL_KEYS = YPROV_ACTIVITY_KEYS + YPROV_ENTITY_KEYS

# Generic fallback (used when format cannot be detected)
DEFAULT_PROVENANCE_CHECKLIST = list(dict.fromkeys(
    FLOWCEPT_WORKFLOW_KEYS + YPROV_ACTIVITY_KEYS + YPROV_ENTITY_KEYS
))


def detect_schema(source_path: str) -> str:
    """
    Return 'flowcept', 'yprov', or 'unknown' based on the source file name
    and its content.
    """
    path = source_path.lower()
    if path.endswith("_f.jsonl") or path.endswith("_f.json"):
        return "flowcept"
    if path.endswith("_y.json") or path.endswith("_y.jsonl"):
        return "yprov"
    # Heuristic: peek at content
    try:
        with open(source_path) as f:
            first = f.read(500)
        if "yprov:" in first or "prov:startedAtTime" in first:
            return "yprov"
        if "workflow_id" in first or "campaign_id" in first:
            return "flowcept"
    except Exception:
        pass
    return "unknown"


def checklist_for_schema(schema: str) -> list[str]:
    """Return the appropriate provenance checklist for a detected schema."""
    if schema == "flowcept":
        return FLOWCEPT_ALL_KEYS
    if schema == "yprov":
        return YPROV_ALL_KEYS
    return DEFAULT_PROVENANCE_CHECKLIST


# ---------------------------------------------------------------------------
# 1. FACTUAL COVERAGE SCORE
# ---------------------------------------------------------------------------

def factual_coverage_score(description: str, checklist: list[str] = None) -> dict:
    """
    Check how many provenance attributes from a checklist are mentioned
    in the model's description.

    Args:
        description:  The model's output text.
        checklist:    List of attribute keywords to look for.
                      Defaults to DEFAULT_PROVENANCE_CHECKLIST.

    Returns:
        dict with 'score' (0-1), 'found', and 'missing' attributes.
    """
    checklist = checklist or DEFAULT_PROVENANCE_CHECKLIST
    desc_lower = description.lower()
    found   = [attr for attr in checklist if attr in desc_lower]
    missing = [attr for attr in checklist if attr not in desc_lower]
    return {
        "score":   round(len(found) / len(checklist), 4),
        "found":   found,
        "missing": missing,
    }


# ---------------------------------------------------------------------------
# 2. HALLUCINATION RATE
# ---------------------------------------------------------------------------

def extract_claims(text: str) -> list[str]:
    """Split text into individual sentences as a rough claim unit."""
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [s.strip() for s in sentences if len(s.strip()) > 10]


def is_claim_supported(claim: str, source_text: str, threshold: float = 0.5) -> bool:
    """
    Lightweight lexical check: a claim is 'supported' if enough of its
    content words appear in the source text.
    For production use, replace with an NLI model (e.g. via transformers).
    """
    stopwords = {"the", "a", "an", "is", "are", "was", "were", "in", "of",
                 "to", "and", "or", "it", "this", "that", "with", "for",
                 "on", "at", "by", "from", "as", "be", "has", "have", "its"}

    claim_words  = set(re.findall(r"\b\w+\b", claim.lower())) - stopwords
    source_words = set(re.findall(r"\b\w+\b", source_text.lower()))

    if not claim_words:
        return True
    overlap = claim_words & source_words
    return (len(overlap) / len(claim_words)) >= threshold


def hallucination_rate(description: str, source_text: str, threshold: float = 0.5) -> dict:
    """
    Estimate what fraction of the model's claims are NOT supported by the source.

    Args:
        description:  Model output.
        source_text:  The original file content the model was shown.
        threshold:    Minimum word-overlap ratio to consider a claim supported.

    Returns:
        dict with 'rate' (0-1), 'unsupported_claims', 'total_claims'.
    """
    claims      = extract_claims(description)
    unsupported = [c for c in claims if not is_claim_supported(c, source_text, threshold)]
    return {
        "rate":               round(len(unsupported) / len(claims), 4) if claims else 0.0,
        "unsupported_claims": unsupported,
        "total_claims":       len(claims),
    }


# ---------------------------------------------------------------------------
# 3. SEMANTIC CONSISTENCY ACROSS CHUNKS
# ---------------------------------------------------------------------------

def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    a, b   = np.array(vec_a), np.array(vec_b)
    denom  = np.linalg.norm(a) * np.linalg.norm(b)
    return float(np.dot(a, b) / denom) if denom > 0 else 0.0


def tfidf_vector(text: str, vocab: list[str]) -> list[float]:
    """Minimal TF vector over a fixed vocab (no external deps)."""
    words  = re.findall(r"\b\w+\b", text.lower())
    counts = Counter(words)
    total  = max(len(words), 1)
    return [counts.get(w, 0) / total for w in vocab]


def semantic_consistency(summaries: list[str]) -> dict:
    """
    Measure pairwise cosine similarity between chunk summaries.
    High consistency → model produces coherent descriptions across chunks.

    Args:
        summaries: List of per-chunk summary strings.

    Returns:
        dict with 'mean_similarity', 'min_similarity', 'pairwise_scores'.
    """
    if len(summaries) < 2:
        return {"mean_similarity": 1.0, "min_similarity": 1.0, "pairwise_scores": []}

    # Build shared vocabulary
    all_words = set(re.findall(r"\b\w+\b", " ".join(summaries).lower()))
    vocab     = sorted(all_words)

    vectors = [tfidf_vector(s, vocab) for s in summaries]

    pairwise = []
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            score = cosine_similarity(vectors[i], vectors[j])
            pairwise.append({"chunk_i": i, "chunk_j": j, "similarity": round(score, 4)})

    scores = [p["similarity"] for p in pairwise]
    return {
        "mean_similarity": round(float(np.mean(scores)), 4),
        "min_similarity":  round(float(np.min(scores)), 4),
        "pairwise_scores": pairwise,
    }


# ---------------------------------------------------------------------------
# 4. ROUGE-L SCORE
# ---------------------------------------------------------------------------

def _lcs_length(x: list, y: list) -> int:
    """Compute length of longest common subsequence."""
    m, n  = len(x), len(y)
    table = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[m][n]


def rouge_l(hypothesis: str, reference: str) -> dict:
    """
    Compute ROUGE-L (F1) between a model description and a reference description.

    Args:
        hypothesis: Model output.
        reference:  Gold-standard / human-written description.

    Returns:
        dict with 'precision', 'recall', 'f1'.
    """
    hyp_tokens = re.findall(r"\b\w+\b", hypothesis.lower())
    ref_tokens = re.findall(r"\b\w+\b", reference.lower())

    if not hyp_tokens or not ref_tokens:
        return {"precision": 0.0, "recall": 0.0, "f1": 0.0}

    lcs   = _lcs_length(hyp_tokens, ref_tokens)
    prec  = lcs / len(hyp_tokens)
    rec   = lcs / len(ref_tokens)
    f1    = (2 * prec * rec / (prec + rec)) if (prec + rec) > 0 else 0.0

    return {
        "precision": round(prec, 4),
        "recall":    round(rec, 4),
        "f1":        round(f1, 4),
    }


# ---------------------------------------------------------------------------
# 5. TOKENS TO ADEQUATE COVERAGE
# ---------------------------------------------------------------------------

def tokens_to_coverage(
    per_chunk_summaries: list[str],
    per_chunk_token_counts: list[int],
    checklist: list[str] = None,
    coverage_threshold: float = 0.7,
) -> dict:
    """
    Find how many tokens were consumed before the cumulative description
    crossed a coverage threshold.

    Args:
        per_chunk_summaries:     Ordered list of summaries (one per chunk).
        per_chunk_token_counts:  Tokens used for each chunk.
        checklist:               Attribute checklist for coverage scoring.
        coverage_threshold:      Score at which coverage is 'adequate'.

    Returns:
        dict with 'tokens_at_threshold', 'chunk_at_threshold', 'coverage_curve'.
    """
    cumulative_text   = ""
    cumulative_tokens = 0
    curve             = []
    threshold_hit     = None

    for i, (summary, tokens) in enumerate(zip(per_chunk_summaries, per_chunk_token_counts)):
        cumulative_text   += " " + summary
        cumulative_tokens += tokens
        coverage = factual_coverage_score(cumulative_text, checklist)["score"]
        curve.append({"chunk": i, "tokens": cumulative_tokens, "coverage": coverage})

        if threshold_hit is None and coverage >= coverage_threshold:
            threshold_hit = {"chunk": i, "tokens": cumulative_tokens, "coverage": coverage}

    return {
        "tokens_at_threshold": threshold_hit["tokens"] if threshold_hit else None,
        "chunk_at_threshold":  threshold_hit["chunk"]  if threshold_hit else None,
        "coverage_curve":      curve,
    }


# ---------------------------------------------------------------------------
# 6. CHUNK COUNT SENSITIVITY
# ---------------------------------------------------------------------------

def chunk_count_sensitivity(
    descriptions_by_chunk_count: dict[int, str],
    reference: str,
) -> dict:
    """
    Measure how ROUGE-L F1 changes as you vary the number of chunks.
    Helps detect whether quality degrades gracefully with file size.

    Args:
        descriptions_by_chunk_count: {num_chunks: final_description_text}
        reference:                   Gold-standard description.

    Returns:
        dict with 'scores' list and 'degradation_slope'.
    """
    scores = []
    for n_chunks, description in sorted(descriptions_by_chunk_count.items()):
        f1 = rouge_l(description, reference)["f1"]
        scores.append({"num_chunks": n_chunks, "rouge_l_f1": f1})

    if len(scores) >= 2:
        x = np.array([s["num_chunks"]  for s in scores], dtype=float)
        y = np.array([s["rouge_l_f1"]  for s in scores], dtype=float)
        slope = float(np.polyfit(x, y, 1)[0])   # negative → degrading
    else:
        slope = None

    return {"scores": scores, "degradation_slope": round(slope, 6) if slope is not None else None}


# ---------------------------------------------------------------------------
# 7. ATTRIBUTE EXTRACTION ACCURACY
# ---------------------------------------------------------------------------

def attribute_extraction_accuracy(
    extracted: dict[str, Any],
    ground_truth: dict[str, Any],
) -> dict:
    """
    Compare model-extracted provenance attributes against known ground truth.

    Args:
        extracted:    Dict of attributes the model extracted, e.g.
                      {"author": "Alice", "version": "1.0", "license": "MIT"}
        ground_truth: Dict of the correct attribute values.

    Returns:
        dict with 'accuracy', 'correct', 'incorrect', 'missing' fields.
    """
    correct   = []
    incorrect = []
    missing   = []

    for key, true_val in ground_truth.items():
        if key not in extracted:
            missing.append(key)
        elif str(extracted[key]).strip().lower() == str(true_val).strip().lower():
            correct.append(key)
        else:
            incorrect.append({"field": key, "expected": true_val, "got": extracted[key]})

    total    = len(ground_truth)
    accuracy = round(len(correct) / total, 4) if total > 0 else 0.0

    return {
        "accuracy":  accuracy,
        "correct":   correct,
        "incorrect": incorrect,
        "missing":   missing,
    }


# ---------------------------------------------------------------------------
# 8. WITH vs WITHOUT PROVENANCE CARD DELTA
# ---------------------------------------------------------------------------

def provenance_card_delta(
    description_without_card: str,
    description_with_card: str,
    reference: str,
    checklist: list[str] = None,
) -> dict:
    """
    Core metric for the research question: does adding a provenance card
    actually improve model output quality?

    Computes delta across ROUGE-L F1 and coverage score.

    Args:
        description_without_card: Final description produced without a card.
        description_with_card:    Final description produced with a card prepended.
        reference:                Gold-standard description.
        checklist:                Attribute checklist for coverage scoring.

    Returns:
        dict with per-metric absolute deltas and a composite improvement score.
    """
    rouge_without  = rouge_l(description_without_card, reference)["f1"]
    rouge_with     = rouge_l(description_with_card,    reference)["f1"]

    coverage_without = factual_coverage_score(description_without_card, checklist)["score"]
    coverage_with    = factual_coverage_score(description_with_card,    checklist)["score"]

    rouge_delta    = round(rouge_with    - rouge_without,    4)
    coverage_delta = round(coverage_with - coverage_without, 4)
    composite      = round((rouge_delta + coverage_delta) / 2, 4)

    return {
        "rouge_l_without":    rouge_without,
        "rouge_l_with":       rouge_with,
        "rouge_l_delta":      rouge_delta,
        "coverage_without":   coverage_without,
        "coverage_with":      coverage_with,
        "coverage_delta":     coverage_delta,
        "composite_delta":    composite,
        "card_is_beneficial": composite > 0,
    }


# ---------------------------------------------------------------------------
# CONVENIENCE: run all metrics at once
# ---------------------------------------------------------------------------

def evaluate_all(
    description: str,
    source_text: str,
    reference: str,
    chunk_summaries: list[str] = None,
    chunk_token_counts: list[int] = None,
    description_without_card: str = None,
    extracted_attributes: dict = None,
    ground_truth_attributes: dict = None,
    checklist: list[str] = None,
) -> dict:
    """
    Run every available metric and return a unified results dict.
    Optional args can be omitted — their metrics will be skipped.
    """
    results = {}

    results["factual_coverage"]  = factual_coverage_score(description, checklist)
    results["hallucination"]     = hallucination_rate(description, source_text)
    results["rouge_l"]           = rouge_l(description, reference)

    if chunk_summaries and len(chunk_summaries) >= 2:
        results["semantic_consistency"] = semantic_consistency(chunk_summaries)

    if chunk_summaries and chunk_token_counts:
        results["tokens_to_coverage"] = tokens_to_coverage(
            chunk_summaries, chunk_token_counts, checklist
        )

    if description_without_card:
        results["provenance_card_delta"] = provenance_card_delta(
            description_without_card, description, reference, checklist
        )

    if extracted_attributes and ground_truth_attributes:
        results["attribute_extraction"] = attribute_extraction_accuracy(
            extracted_attributes, ground_truth_attributes
        )

    return results
