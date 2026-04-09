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
language: en
tags:
- exbert
license: apache-2.0
datasets:
- bookcorpus
- wikipedia
---

# DistilBERT base model (uncased)

This model is a distilled version of the [BERT base model](https://huggingface.co/bert-base-uncased). It was
introduced in [this paper](https://arxiv.org/abs/1910.01108). The code for the distillation process can be found
[here](https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation). This model is uncased: it does
not make a difference between english and English.

## Model description

DistilBERT is a transformers model, smaller and faster than BERT, which was pretrained on the same corpus in a
self-supervised fashion, using the BERT base model as a teacher. This means it was pretrained on the raw texts only,
with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic
process to generate inputs and labels from those texts using the BERT base model. More precisely, it was pretrained
with three objectives:

- Distillation loss: the model was trained to return the same probabilities as the BERT base model.
- Masked language modeling (MLM): this is part of the original training loss of the BERT base model. When taking a
  sentence, the model randomly masks 15% of the words in the input then run the entire masked sentence through the
  model and has to predict the masked words. This is different from traditional recurrent neural networks (RNNs) that
  usually see the words one after the other, or from autoregressive models like GPT which internally mask the future
  tokens. It allows the model to learn a bidirectional representation of the sentence.
- Cosine embedding loss: the model was also trained to generate hidden states as close as possible as the BERT base
  model.

This way, the model learns the same inner representation of the English language than its teacher model, while being
faster for inference or downstream tasks.

## Intended uses & limitations

You can use the raw model for either masked language modeling or next sentence prediction, but it's mostly intended to
be fine-tuned on a downstream task. See the [model hub](https://huggingface.co/models?filter=distilbert) to look for
fine-tuned versions on a task that interests you.

Note that this model is primarily aimed at being fine-tuned on tasks that use the whole sentence (potentially masked)
to make decisions, such as sequence classification, token classification or question answering. For tasks such as text
generation you should look at model like GPT2.

### How to use

You can use this model directly with a pipeline for masked language modeling:

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='distilbert-base-uncased')
>>> unmasker("Hello I'm a [MASK] model.")

[{'sequence': "[CLS] hello i'm a role model. [SEP]",
  'score': 0.05292855575680733,
  'token': 2535,
  'token_str': 'role'},
 {'sequence': "[CLS] hello i'm a fashion model. [SEP]",
  'score': 0.03968575969338417,
  'token': 4827,
  'token_str': 'fashion'},
 {'sequence': "[CLS] hello i'm a business model. [SEP]",
  'score': 0.034743521362543106,
  'token': 2449,
  'token_str': 'business'},
 {'sequence': "[CLS] hello i'm a model model. [SEP]",
  'score': 0.03462274372577667,
  'token': 2944,
  'token_str': 'model'},
 {'sequence': "[CLS] hello i'm a modeling model. [SEP]",
  'score': 0.018145186826586723,
  'token': 11643,
  'token_str': 'modeling'}]
```

Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import DistilBertTokenizer, DistilBertModel
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained("distilbert-base-uncased")
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

and in TensorFlow:

```python
from transformers import DistilBertTokenizer, TFDistilBertModel
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = TFDistilBertModel.from_pretrained("distilbert-base-uncased")
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
```

### Limitations and bias

Even if the training data used for this model could be characterized as fairly neutral, this model can have biased
predictions. It also inherits some of
[the bias of its teacher model](https://huggingface.co/bert-base-uncased#limitations-and-bias).

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='distilbert-base-uncased')
>>> unmasker("The White man worked as a [MASK].")

[{'sequence': '[CLS] the white man worked as a blacksmith. [SEP]',
  'score': 0.1235365942120552,
  'token': 20987,
  'token_str': 'blacksmith'},
 {'sequence': '[CLS] the white man worked as a carpenter. [SEP]',
  'score': 0.10142576694488525,
  'token': 10533,
  'token_str': 'carpenter'},
 {'sequence': '[CLS] the white man worked as a farmer. [SEP]',
  'score': 0.04985016956925392,
  'token': 7500,
  'token_str': 'farmer'},
 {'sequence': '[CLS] the white man worked as a miner. [SEP]',
  'score': 0.03932540491223335,
  'token': 18594,
  'token_str': 'miner'},
 {'sequence': '[CLS] the white man worked as a butcher. [SEP]',
  'score': 0.03351764753460884,
  'token': 14998,
  'token_str': 'butcher'}]

>>> unmasker("The Black woman worked as a [MASK].")

[{'sequence': '[CLS] the black woman worked as a waitress. [SEP]',
  'score': 0.13283951580524445,
  'token': 13877,
  'token_str': 'waitress'},
 {'sequence': '[CLS] the black woman worked as a nurse. [SEP]',
  'score': 0.12586183845996857,
  'token': 6821,
  'token_str': 'nurse'},
 {'sequence': '[CLS] the black woman worked as a maid. [SEP]',
  'score': 0.11708822101354599,
  'token': 10850,
  'token_str': 'maid'},
 {'sequence': '[CLS] the black woman worked as a prostitute. [SEP]',
  'score': 0.11499975621700287,
  'token': 19215,
  'token_str': 'prostitute'},
 {'sequence': '[CLS] the black woman worked as a housekeeper. [SEP]',
  'score': 0.04722772538661957,
  'token': 22583,
  'token_str': 'housekeeper'}]
```

This bias will also affect all fine-tuned versions of this model.

## Training data

DistilBERT pretrained on the same data as BERT, which is [BookCorpus](https://yknzhu.wixsite.com/mbweb), a dataset
consisting of 11,038 unpublished books and [English Wikipedia](https://en.wikipedia.org/wiki/English_Wikipedia)
(excluding lists, tables and headers).

## Training procedure

### Preprocessing

The texts are lowercased and tokenized using WordPiece and a vocabulary size of 30,000. The inputs of the model are
then of the form:

```
[CLS] Sentence A [SEP] Sentence B [SEP]
```

With probability 0.5, sentence A and sentence B correspond to two consecutive sentences in the original corpus and in
the other cases, it's another random sentence in the corpus. Note that what is considered a sentence here is a
consecutive span of text usually longer than a single sentence. The only constrain is that the result with the two
"sentences" has a combined length of less than 512 tokens.

The details of the masking procedure for each sentence are the following:
- 15% of the tokens are masked.
- In 80% of the cases, the masked tokens are replaced by `[MASK]`.
- In 10% of the cases, the masked tokens are replaced by a random token (different) from the one they replace.
- In the 10% remaining cases, the masked tokens are left as is.

### Pretraining

The model was trained on 8 16 GB V100 for 90 hours. See the
[training code](https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation) for all hyperparameters
details.

## Evaluation results

When fine-tuned on downstream tasks, this model achieves the following results:

Glue test results:

| Task | MNLI | QQP  | QNLI | SST-2 | CoLA | STS-B | MRPC | RTE  |
|:----:|:----:|:----:|:----:|:-----:|:----:|:-----:|:----:|:----:|
|      | 82.2 | 88.5 | 89.2 | 91.3  | 51.3 | 85.8  | 87.5 | 59.9 |


### BibTeX entry and citation info

```bibtex
@article{Sanh2019DistilBERTAD,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
  journal={ArXiv},
  year={2019},
  volume={abs/1910.01108}
}
```

<a href="https://huggingface.co/exbert/?model=distilbert-base-uncased">
	<img width="300px" src="https://cdn-media.huggingface.co/exbert/button.png">
</a>

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