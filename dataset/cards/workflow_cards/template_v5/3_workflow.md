# Workflow Card: Use Case 3 — PII Redaction Fine-Tuning

---

## 1. Workflow

- **name**: llama32_pii_redactor_finetuning
- **description**: End-to-end ML workflow that fine-tunes Meta's Llama-3.2-3B-Instruct on the Ai4Privacy PII-Masking-200k dataset using QLoRA (4-bit quantisation, LoRA rank 16) to produce a lightweight PII redaction adapter (LoRA) capable of detecting and replacing personally identifiable information spans in English text with structured placeholders (e.g. `[FIRSTNAME]`, `[EMAIL]`, `[IPV4]`), while leaving all non-PII content unchanged.

---

## 2. Summary

- **execution_id**: llama32_pii_redactor_finetuning_v0
- **version**: 0
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: Completed
- **location**: ~
- **user**: ~
- **entrypoint.repository**: ~
- **entrypoint.branch**: ~
- **entrypoint.short_sha**: ~

---

## 3. Infrastructure

- **host_os**: ~
- **compute_hardware**: ~
- **runtime_environment**: ~
- **resource_manager**: ~
- **primary_software**: Python, PyTorch, Hugging Face Transformers, PEFT, bitsandbytes
- **environment_snapshot**: ~

---

## 4. Overview

### 4.1 Run Summary

- **total_activities**: 3
- **status_counts**: finished: 3
- **arguments**: LoRA rank: 16, LoRA alpha: 32, LoRA dropout: 0.05, quantisation: 4-bit NF4 (bitsandbytes), sequence length: 320–512, batch size: 1, gradient accumulation steps: 16, learning rate: 2e-4, scheduler: cosine, warmup: 3%, loss mask: assistant span only (between `<safe>` and `</safe>`)

**Notable Inputs:**
  - `ai4privacy/pii-masking-200k` — format: JSONL (source_text / target_text / privacy_mask triples), size: ~209k examples / 13.6M text tokens (English subset used), source: https://huggingface.co/datasets/ai4privacy/pii-masking-200k
  - `meta-llama/Llama-3.2-3B-Instruct` — format: safetensors model weights (PyTorch BF16), size: ~6.43 GB, source: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct

**Notable Outputs:**
  - `Llama-3.2-3B-PII-Redactor (LoRA adapter)` — type: PEFT LoRA adapter weights, compatible with 4-bit quantised base model, location: ~

**Structure (activity DAG):**
  1. DataPreparation
  2. ModelFinetuning
  3. ModelEvaluation

- **observations**: Only the English subset of the Ai4Privacy PII-Masking-200k dataset was used; French, German, and Italian splits were excluded, so the resulting adapter is English-only. The output contract enforces `<safe>…</safe>` wrapping for the redacted text. Very long inputs must be chunked prior to inference. Placeholder ambiguity (e.g. `[DOB]` vs `[DATE]`) remains a known limitation in close cases.

### 4.2 Resource Usage

- **cpu**: ~
- **memory**: ~
- **gpu**: ~
- **disk**: ~
- **network**: ~

---

## 5. Activities

#### Activity: `DataPreparation`

- **name**: DataPreparation
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `ai4privacy/pii-masking-200k (full)` — ~209k multilingual examples (English, French, German, Italian) with 54 PII classes across 229 discussion subjects; format: JSONL with source_text, target_text, privacy_mask, span_labels, mbert_bio_labels, mbert_text_tokens fields
  - **outputs**:
    - `ai4privacy/pii-masking-200k (English subset)` — English-only filtered split ready for supervised fine-tuning; formatted as instruction/assistant pairs with `<safe>…</safe>` output wrapper; train/test split with 300 random samples held out for evaluation

#### Activity: `ModelFinetuning`

- **name**: ModelFinetuning
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `meta-llama/Llama-3.2-3B-Instruct` — pretrained base model loaded in 4-bit NF4 quantisation via bitsandbytes; 3.21B parameters, 128k context, Llama 3.2 Community License
    - `ai4privacy/pii-masking-200k (English subset)` — instruction-tuning dataset formatted with system prompt enforcing exact-input-preservation redaction behaviour
  - **outputs**:
    - `Llama-3.2-3B-PII-Redactor (LoRA adapter)` — PEFT LoRA adapter (rank 16, alpha 32, dropout 0.05); trained with loss computed only on the assistant span between `<safe>` and `</safe>`; compatible with 4-bit quantised Llama-3.2-3B-Instruct base

#### Activity: `ModelEvaluation`

- **name**: ModelEvaluation
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `Llama-3.2-3B-PII-Redactor (LoRA adapter)` — fine-tuned adapter merged with 4-bit base for inference
    - `evaluation split` — 300 randomly sampled held-out examples from the English subset
  - **outputs**:
    - `evaluation_report` — exact match: ~0.67; placeholder micro-F1: ~0.90 (precision ~0.91, recall ~0.90); formatting errors: ~0.00

---

## 6. Significant Artifacts

### Input Artifacts

**Artifact: `meta-llama/Llama-3.2-3B-Instruct`**
- **name**: meta-llama/Llama-3.2-3B-Instruct
- **description**: Pretrained Llama 3.2 instruction-tuned text model with 3.21B parameters. Auto-regressive transformer trained on up to 9T tokens (data cutoff December 2023) using SFT and RLHF. Supports multilingual text generation with 128k context length. License: Llama 3.2 Community License.
- **reference**: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct

**Artifact: `ai4privacy/pii-masking-200k`**
- **name**: ai4privacy/pii-masking-200k
- **description**: Synthetic, human-in-the-loop validated dataset of ~209k examples (13.6M text tokens) covering 54 PII classes across 229 discussion subjects in English, French, German, and Italian. Each example provides a source text containing PII, a target text with PII replaced by bracketed placeholders, and structured privacy_mask, span_labels, and BIO-label fields. Generated using proprietary Ai4Privacy algorithms; no real personal data. License: ~
- **reference**: https://huggingface.co/datasets/ai4privacy/pii-masking-200k

### Output Artifacts

**Artifact: `Llama-3.2-3B-PII-Redactor (LoRA adapter)`**
- **name**: Llama-3.2-3B-PII-Redactor (LoRA adapter)
- **description**: QLoRA-trained PEFT adapter (rank 16, alpha 32) on top of Llama-3.2-3B-Instruct, specialised for English PII redaction. Replaces detected PII spans with Ai4Privacy placeholder taxonomy labels while preserving all non-PII text. Requires 4-bit quantised base model for inference. Achieves placeholder micro-F1 of ~0.90 and exact match of ~0.67 on a 300-sample held-out test set.
- **reference**: ~
