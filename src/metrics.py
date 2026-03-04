
import re
import numpy as np
from typing import Any
from collections import Counter
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

from consts import *


# ---------------------------------------------------------------------------
# 1. FACTUAL COVERAGE SCORE
# ---------------------------------------------------------------------------

def factual_coverage_score(description: str, checklist: list[str] = None) -> dict:
    """
    Check how many provenance attributes from a checklist are mentioned
    in the model's description.
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

# TODO: This has to be made better
def is_claim_supported(claim: str, source_text: str, threshold: float = 0.5) -> bool:
    """
    Lightweight lexical check: a claim is 'supported' if enough of its content words appear in the source text.
    To improve, maybe try replace with an NLI model?
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


# TODO: improve the reference, right now it's not great
def rouge_l(hypothesis: str, reference: str) -> dict:
    hyp_tokens = re.findall(r"\b\w+\b", hypothesis.lower())
    ref_tokens = re.findall(r"\b\w+\b", reference.lower())

    if not hyp_tokens or not ref_tokens:
        return {"precision": 0.0, "recall": 0.0, "f1": 0.0}

    lcs   = _lcs_length(hyp_tokens, ref_tokens)
    prec  = lcs / len(hyp_tokens)
    rec   = lcs / len(ref_tokens)
    f1    = (2 * prec * rec / (prec + rec)) if (prec + rec) > 0 else 0.0

    return {"precision": prec, "recall": rec, "f1": f1}


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

def chunk_count_sensitivity(descriptions_by_chunk_count: dict[int, str],reference: str) -> dict:
    """
    Measure how ROUGE-L F1 changes as you vary the number of chunks.
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


def calculate_perplexity(text, model_name="gpt2"):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
    model.eval()

    encodings = tokenizer(text, return_tensors="pt")
    input_ids = encodings.input_ids.to(device)

    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss

    perplexity = torch.exp(loss).item()
    return perplexity

def calculate_log_likelihood(text, model_name="gpt2"):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
    model.eval()

    encodings = tokenizer(text, return_tensors="pt")
    input_ids = encodings.input_ids.to(device)

    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss  # CrossEntropyLoss = -avg log likelihood

    avg_log_likelihood = -loss.item()
    return avg_log_likelihood


def calculate_bleu(reference, candidate):
    reference_tokens = reference.split()
    candidate_tokens = candidate.split()

    smoothie = SmoothingFunction().method4

    score = sentence_bleu(
        [reference_tokens],
        candidate_tokens,
        smoothing_function=smoothie
    )

    return score


def calculate_bleu_multi_ref(references, candidate):
    references_tokens = [ref.split() for ref in references]
    candidate_tokens = candidate.split()

    smoothie = SmoothingFunction().method4

    return sentence_bleu(
        references_tokens,
        candidate_tokens,
        smoothing_function=smoothie
    )


def self_bleu(texts):
    smoothie = SmoothingFunction().method4
    scores = []

    tokenized_texts = [text.split() for text in texts]

    for i, candidate in enumerate(tokenized_texts):
        references = tokenized_texts[:i] + tokenized_texts[i+1:]
        if not references:
            continue

        score = sentence_bleu(
            references,
            candidate,
            smoothing_function=smoothie
        )
        scores.append(score)

    return sum(scores) / len(scores) if scores else 0.0


def distinct_n(texts, n=2):
    all_ngrams = []
    total_ngrams = 0

    for text in texts:
        tokens = text.split()
        ngrams = [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
        all_ngrams.extend(ngrams)
        total_ngrams += len(ngrams)

    if total_ngrams == 0:
        return 0.0

    unique_ngrams = len(set(all_ngrams))
    return unique_ngrams / total_ngrams