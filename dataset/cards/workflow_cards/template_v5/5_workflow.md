# Workflow Card: Use Case 5 — Phishing Email & URL Detection Fine-Tuning

---

## 1. Workflow

- **name**: distilbert_phishing_detection_finetuning
- **description**: End-to-end ML workflow that fine-tunes DistilBERT-base-uncased on the PhishingEmailDetectionv2.0 dataset using the Hugging Face Trainer API to produce a 4-class sequence classification model capable of distinguishing legitimate emails, phishing emails, legitimate URLs, and phishing URLs with high precision and recall.

---

## 2. Summary

- **execution_id**: distilbert_phishing_detection_finetuning_v0
- **version**: ~
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
- **primary_software**: Python, PyTorch, Hugging Face Transformers, Hugging Face Trainer API
- **environment_snapshot**: ~

---

## 4. Overview

### 4.1 Run Summary

- **total_activities**: 3
- **status_counts**: finished: 3
- **arguments**: epochs: 3, max_length: 512, truncation: True

**Notable Inputs:**
  - `cybersectony/PhishingEmailDetectionv2.0` — format: Parquet (content string + integer label), size: 200,000 entries (train: 120,000 / validation: 20,000 / test: 60,000), source: https://huggingface.co/datasets/cybersectony/PhishingEmailDetectionv2.0
  - `distilbert/distilbert-base-uncased` — format: PyTorch model weights, size: ~67M parameters, source: https://huggingface.co/distilbert/distilbert-base-uncased

**Notable Outputs:**
  - `phishing-email-detection-distilbert_v2.4.1` — type: fine-tuned sequence classification model, location: https://huggingface.co/cybersectony/phishing-email-detection-distilbert_v2.4.1

**Structure (activity DAG):**
  1. DataPreparation
  2. ModelFinetuning
  3. ModelEvaluation

- **observations**: The dataset combines two distinct content types (email bodies and URLs) under a unified 4-class taxonomy. Email samples account for 22,644 entries and URL samples for 177,356, producing a significant class-type imbalance that should be noted when interpreting per-class metrics. The model operates on tokenised sequences truncated to 512 tokens, which may truncate long email bodies.

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
    - `cybersectony/PhishingEmailDetectionv2.0 (raw)` — 200,000 entries combining email messages (22,644) and URLs (177,356); two columns: `content` (string) and `label` (integer 0–3: legitimate_email, phishing_email, legitimate_url, phishing_url); format: Parquet; language: English
  - **outputs**:
    - `cybersectony/PhishingEmailDetectionv2.0 (split)` — train (120,000 examples, ~47.2 MB), validation (20,000 examples, ~5.1 MB), test (60,000 examples, ~14.9 MB); total dataset size: ~67.2 MB

#### Activity: `ModelFinetuning`

- **name**: ModelFinetuning
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `distilbert/distilbert-base-uncased` — distilled BERT variant; ~67M parameters; pretrained via distillation loss, MLM, and cosine embedding loss on BooksCorpus + English Wikipedia; uncased tokeniser; Apache-2.0 license
    - `cybersectony/PhishingEmailDetectionv2.0 (train split)` — 120,000 tokenised examples (max_length=512, truncation=True), 4-class labels
  - **outputs**:
    - `phishing-email-detection-distilbert_v2.4.1` — DistilBERT with sequence classification head (num_labels=4); trained for 3 epochs via Hugging Face Trainer API

#### Activity: `ModelEvaluation`

- **name**: ModelEvaluation
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `phishing-email-detection-distilbert_v2.4.1` — fine-tuned classification model
    - `cybersectony/PhishingEmailDetectionv2.0 (validation / test split)` — held-out evaluation data
  - **outputs**:
    - `evaluation_report` — accuracy: 99.58%; F1-score (micro): 99.579%; precision: 99.583%; recall: 99.58%

---

## 6. Significant Artifacts

### Input Artifacts

**Artifact: `distilbert/distilbert-base-uncased`**
- **name**: distilbert/distilbert-base-uncased
- **description**: Distilled version of BERT-base, ~40% smaller and ~60% faster while retaining ~97% of BERT's performance on GLUE. Pretrained on BooksCorpus and English Wikipedia using distillation loss, masked language modelling, and cosine embedding loss. Uncased (no distinction between upper and lower case). ~67M parameters. License: Apache-2.0.
- **reference**: https://huggingface.co/distilbert/distilbert-base-uncased

**Artifact: `cybersectony/PhishingEmailDetectionv2.0`**
- **name**: cybersectony/PhishingEmailDetectionv2.0
- **description**: Combined phishing detection dataset of 200,000 English entries (email bodies and URLs). Four-class taxonomy: legitimate_email (0), phishing_email (1), legitimate_url (2), phishing_url (3). Split into train (120,000), validation (20,000), and test (60,000). Format: Parquet with `content` and `label` columns. Total size: ~67.2 MB. License: ~
- **reference**: https://huggingface.co/datasets/cybersectony/PhishingEmailDetectionv2.0

### Output Artifacts

**Artifact: `phishing-email-detection-distilbert_v2.4.1`**
- **name**: phishing-email-detection-distilbert_v2.4.1
- **description**: DistilBERT-base-uncased fine-tuned for 4-class phishing detection (legitimate email, phishing email, legitimate URL, phishing URL) using the Hugging Face Trainer API over 3 epochs. Achieves 99.58% accuracy and 99.579% micro-F1 on the evaluation set. Accepts tokenised text up to 512 tokens. License: Apache-2.0.
- **reference**: https://huggingface.co/cybersectony/phishing-email-detection-distilbert_v2.4.1
