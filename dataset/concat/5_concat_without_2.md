---
license: apache-2.0
datasets:
- cybersectony/PhishingEmailDetectionv2.0
language:
- en
base_model:
- distilbert/distilbert-base-uncased
library_name: transformers
---

# A distilBERT based Phishing Email Detection Model

## Model Overview
This model is based on DistilBERT and has been fine-tuned for multilabel classification of Emails and URLs as safe or potentially phishing.

## Key Specifications
- __Base Architecture:__ DistilBERT
- __Task:__ Multilabel Classification
- __Fine-tuning Framework:__ Hugging Face Trainer API
- __Training Duration:__ 3 epochs

## Performance Metrics
- __Accuracy:__ 99.58
- __F1-score:__ 99.579
- __Precision:__ 99.583
- __Recall:__ 99.58

## Dataset Details

The model was trained on a custom dataset of Emails and URLs labeled as legitimate or phishing. The dataset is available at [`cybersectony/PhishingEmailDetectionv2.0`](https://huggingface.co/datasets/cybersectony/PhishingEmailDetectionv2.0) on the Hugging Face Hub.


## Usage Guide

## Installation

```bash
pip install transformers
pip install torch
```

## Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("cybersectony/phishing-email-detection-distilbert_v2.4.1")
import torch

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("cybersectony/phishing-email-detection-distilbert_v2.4.1")

def predict_email(email_text):
    # Preprocess and tokenize
    inputs = tokenizer(
        email_text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )
    
    # Get prediction
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
    # Get probabilities for each class
    probs = predictions[0].tolist()
    
    # Create labels dictionary
    labels = {
        "legitimate_email": probs[0],
        "phishing_url": probs[1],
        "legitimate_url": probs[2],
        "phishing_url_alt": probs[3]
    }
    
    # Determine the most likely classification
    max_label = max(labels.items(), key=lambda x: x[1])
    
    return {
        "prediction": max_label[0],
        "confidence": max_label[1],
        "all_probabilities": labels
    }
```

## Example Usage

```python
# Example usage
email = """
Dear User,
Your account security needs immediate attention. Please verify your credentials.
Click here: http://suspicious-link.com
"""

result = predict_email(email)
print(f"Prediction: {result['prediction']}")
print(f"Confidence: {result['confidence']:.2%}")
print("\nAll probabilities:")
for label, prob in result['all_probabilities'].items():
    print(f"{label}: {prob:.2%}")
```
# Provenance Card: Phishing Email Detection DistilBERT Fine-tuning Workflow

## Card Metadata

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Card ID | **[R]** | `[manual]` | `PC-PHISH-DISTILBERT-20241027-005` |
| Card Creation Timestamp | **[R]** | `[manual]` | `2024-10-27T20:00:00Z` |
| Card Author | **[R]** | `[manual]` | `Provenance Card Generator v1.2` |
| Authoring Method | **[R]** | `[manual]` | `hybrid` |
| Source Provenance Document | **[R]** | `[manual]` | `https://internal.cybersec.ai/pipelines/phishing-v2-run-99` |
| Card Contact | **[Rec]** | `[manual]` | `tony@cybersecai.example.com` |

---

## 0. Provenance Capture Metadata

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Capture Tool | **[R]** | `[manual]` | `Hugging Face Trainer Callback Logger` |
| Capture Method | **[R]** | `[manual]` | `automatic instrumentation` |
| Provenance Format | **[R]** | `[manual]` | `W3C PROV-JSON` |
| Record ID | **[R]** | `[manual]` | `rec-distilbert-phish-2.4.1` |
| Record Creation Timestamp | **[Rec]** | `[manual]` | `2024-10-27T19:55:00Z` |
| Coverage Level | **[Rec]** | `[manual]` | `activity-level` |
| Known Capture Gaps | **[Rec]** | `[manual]` | `Specific dataset split randomization seed was not captured in the metadata.` |

---

## 1. Workflow Identification

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Workflow Execution ID | **[R]** | `[manual]` | `exec-phish-detect-v2.4.1` |
| Workflow Name | **[R]** | `[manual]` | `DistilBERT Phishing Email Detection Fine-tuning` |
| Workflow Version | **[Rec]** | `[manual]` | `v2.4.1` |
| Execution Start Timestamp | **[R]** | `[manual]` | `2024-10-27T10:00:00Z` |
| Execution End Timestamp | **[Rec]** | `[manual]` | `2024-10-27T14:30:00Z` |
| Execution Duration | **[Rec]** | `[inferred]` | `4h 30m 00s` |
| Execution Status | **[R]** | `[manual]` | `Completed` |
| Execution Location | **[Rec]** | `[manual]` | `Azure ML Compute - West US` |

---

## 2. Execution Context

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Host OS | **[Rec]** | `[manual]` | `Ubuntu 22.04 LTS` |
| Compute Hardware | **[Rec]** | `[manual]` | `1x NVIDIA V100 (16GB)` |
| Runtime Environment | **[Rec]** | `[manual]` | `Python 3.10 / PyTorch 2.1` |
| Resource Manager | **[O]** | `[manual]` | `Hugging Face Trainer API` |
| Primary Software | **[Rec]** | `[prov_doc]` | `Transformers, Torch, Datasets` |
| Environment Snapshot | **[O]** | `[manual]` | `phish_detect_env.yaml` |

---

## 3. Actors

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Execution Triggerer | **[R]** | `[manual]` | `cybersectony` |
| Lead Practitioner | **[Rec]** | `[prov_doc]` | `Tony (CyberSec AI)` |
| Hardware Provider | **[Rec]** | `[manual]` | `Microsoft Azure` |
| Data Provider | **[Rec]** | `[prov_doc]` | `CyberSecTony / Custom Aggregation` |
| Accountable Organization | **[R]** | `[manual]` | `CyberSec AI Lab` |

---

## 4. Inputs

### Block [1]: base-model
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Artifact Name | **[R]** | `[prov_doc]` | `distilbert-base-uncased` |
| Artifact Type | **[R]** | `[manual]` | `Pretrained Distilled BERT Model` |
| Version / Hash | **[Rec]** | `[manual]` | `sha256:distilbert-uncased-ref` |
| Logical URI | **[R]** | `[prov_doc]` | `https://huggingface.co/distilbert/distilbert-base-uncased` |
| License | **[Rec]** | `[prov_doc]` | `Apache-2.0` |
| Description | **[Rec]** | `[prov_doc]` | `Smaller, faster, cheaper version of BERT base model (uncased).` |

### Block [2]: phishing-dataset
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Artifact Name | **[R]** | `[prov_doc]` | `PhishingEmailDetectionv2.0` |
| Artifact Type | **[R]** | `[manual]` | `Email and URL Classification Dataset` |
| Version / Hash | **[Rec]** | `[manual]` | `sha256:phish-v2-data-200k` |
| Logical URI | **[R]** | `[prov_doc]` | `https://huggingface.co/datasets/cybersectony/PhishingEmailDetectionv2.0` |
| License | **[Rec]** | `[manual]` | `Apache-2.0` |
| Description | **[Rec]** | `[prov_doc]` | `200k samples (22.6k emails, 177.3k URLs) across 4 labels.` |

---

## 5. Execution Record

### Block [1]: sequence-classification-finetuning
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Activity Name | **[R]** | `[manual]` | `phish-classifier-training` |
| Activity Type | **[R]** | `[manual]` | `Supervised Fine-Tuning (SFT)` |
| Start Timestamp | **[Rec]** | `[manual]` | `2024-10-27T10:15:00Z` |
| End Timestamp | **[Rec]** | `[manual]` | `2024-10-27T14:15:00Z` |
| Inputs Consumed | **[R]** | `[manual]` | `base-model, phishing-dataset` |
| Outputs Produced | **[R]** | `[manual]` | `finetuned-distilbert-weights` |
| Parameters | **[Rec]** | `[prov_doc]` | `Epochs: 3, Max Length: 512, Task: Multilabel` |

---

## 6. Outputs

### Block [1]: finetuned-distilbert-weights
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Artifact Name | **[R]** | `[prov_doc]` | `phishing-email-detection-distilbert_v2.4.1` |
| Artifact Type | **[R]** | `[manual]` | `Fine-tuned Model Weights` |
| Version / Hash | **[Rec]** | `[manual]` | `sha256:phish-distilbert-v241` |
| Logical URI | **[R]** | `[manual]` | `https://huggingface.co/cybersectony/phishing-email-detection-distilbert_v2.4.1` |
| License | **[Rec]** | `[prov_doc]` | `Apache-2.0` |
| Content Summary | **[O]** | `[manual]` | `PyTorch weights for 4-class email/URL phishing classification.` |

---

## 8. Execution Quality

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Status | **[R]** | `[manual]` | `Success` |
| Success Criteria | **[R]** | `[manual]` | `F1-score > 0.98 on validation set.` |
| Errors / Warnings | **[Rec]** | `[manual]` | `None` |
| Quality Metrics | **[Rec]** | `[prov_doc]` | `Accuracy: 99.58, F1: 99.579, Precision: 99.583, Recall: 99.58` |
| Validation Method | **[Rec]** | `[prov_doc]` | `Validation on 20,000 samples (10% of dataset).` |

---

## 9. Provenance Record Quality

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Capture Completeness | **[R]** | `[manual]` | `0.98 (Excellent)` |
| Unlogged Activities | **[Rec]** | `[manual]` | `The specific logic for merging URLs and emails into a single training file was not logged.` |
| Unlogged Inputs / Outputs | **[Rec]** | `[manual]` | `Log files generated by the Trainer API were not stored as artifacts.` |
| Reproducibility | **[Rec]** | `[manual]` | `Reproducible using the Hugging Face Trainer API and the publicly available dataset.` |

---

## Coverage Statistics

| Section | Total Fields | Filled | Missing | Fill % |
|---------|-------------|--------|---------|--------|
| Card Metadata | 6 | 6 | 0 | 100% |
| §0 Provenance Capture Metadata | 8 | 8 | 0 | 100% |
| §1 Workflow Identification | 8 | 8 | 0 | 100% |
| §2 Execution Context | 7 | 6 | 1 | 85.7% |
| §3 Actors | 6 | 5 | 1 | 83.3% |
| §4 Inputs (6 fields × 2 blocks) | 12 | 12 | 0 | 100% |
| §5 Execution Record (7 fields × 1 block) | 7 | 7 | 0 | 100% |
| §6 Outputs (7 fields × 1 block) | 7 | 6 | 1 | 85.7% |
| §8 Execution Quality | 6 | 5 | 1 | 83.3% |
| §9 Provenance Record Quality | 4 | 4 | 0 | 100% |
---
dataset_info:
  features:
  - name: content
    dtype: string
  - name: label
    dtype: int64
  splits:
  - name: train
    num_bytes: 47241927
    num_examples: 120000
  - name: validation
    num_bytes: 5052323
    num_examples: 20000
  - name: test
    num_bytes: 14856442
    num_examples: 60000
  download_size: 40289388
  dataset_size: 67150692
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
---

# Phishing Email Detection Dataset

A comprehensive dataset combining email messages and URLs for phishing detection.

## Dataset Overview

### Quick Facts
- **Task Type**: Multi-class Classification
- **Languages**: English
- **Total Samples**: 200,000 entries
- **Size Split**: 
  - Email samples: 22,644
  - URL samples: 177,356
- **Label Distribution**: Four classes (0, 1, 2, 3)
- **Format**: Two columns - `content` and `labels`

## Dataset Structure

### Features
```python
{
    'content': Value(dtype='string', description='The text content - either email body or URL'),
    'labels': ClassLabel(num_classes=4, names=[
        'legitimate_email',    # 0
        'phishing_email',       # 1
        'legitimate_url',     # 2
        'phishing_url'    # 3
    ], description='Multi-class label for content classification')
}