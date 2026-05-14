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

# Workflow Card: Use Case 5 — Phishing Email & URL Detection Fine-Tuning

---

## 1. Workflow

- **name**: distilbert_phishing_detection_finetuning
- **description**: End-to-end ML workflow that fine-tunes DistilBERT-base-uncased on the PhishingEmailDetectionv2.0 dataset using the Hugging Face Trainer API to produce a 4-class sequence classification model capable of distinguishing legitimate emails, phishing emails, legitimate URLs, and phishing URLs with high precision and recall.

---

## 2. Summary

- **execution_id**: distilbert_phishing_detection_finetuning_v0
- **version**: 0
- **started_at**: 2024-05-09T14:10:00Z
- **ended_at**: 2024-05-09T17:43:28Z
- **duration**: 3h 33m 28s
- **status**: Completed
- **location**: us-east-1 (AWS EC2 g4dn.2xlarge)
- **user**: cybersectony
- **entrypoint.repository**: https://github.com/cybersectony/phishing-detection-distilbert
- **entrypoint.branch**: main
- **entrypoint.short_sha**: c14f8a2

---

## 3. Infrastructure

- **host_os**: Ubuntu 22.04.3 LTS
- **compute_hardware**: 1× NVIDIA T4-16GB, Intel Xeon Platinum 8259CL, 32 GB RAM
- **runtime_environment**: Python 3.10.12, CUDA 11.8, cuDNN 8.6.0
- **resource_manager**: AWS EC2 (on-demand, launched via AWS CLI)
- **primary_software**: Python, PyTorch, Hugging Face Transformers, Hugging Face Trainer API
- **environment_snapshot**: torch==2.2.1, transformers==4.40.0, datasets==2.19.1, evaluate==0.4.2, scikit-learn==1.4.2, accelerate==0.29.3

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

- **cpu**: Peak 8-core utilisation ~45% during tokenisation and DataLoader prefetching; predominantly GPU-bound during training forward/backward passes
- **memory**: Peak RAM usage: 18.4 GB (tokenised dataset fully cached in memory + DataLoader workers buffer)
- **gpu**: 1× NVIDIA T4-16GB; peak VRAM usage 13.8 GB (batch size 32 + classifier head gradients); average GPU utilisation ~91% during training steps
- **disk**: ~8 GB total — ~67 MB base model weights + ~67.2 MB dataset (Parquet) + ~4 GB tokenised cache + ~260 MB fine-tuned model checkpoint + ~3.6 GB Trainer logging artefacts
- **network**: ~350 MB ingress (base model + dataset download from HuggingFace Hub); ~270 MB egress (fine-tuned model upload to HuggingFace Hub)

---

## 5. Activities

#### Activity: `DataPreparation`

- **name**: DataPreparation
- **task_count**: 1
- **started_at**: 2024-05-09T14:10:00Z
- **ended_at**: 2024-05-09T14:38:17Z
- **duration**: 28m 17s
- **status**: success: 1
  - **hosts**: ip-10-0-4-21.ec2.internal
  - **inputs**:
    - `cybersectony/PhishingEmailDetectionv2.0 (raw)` — 200,000 entries combining email messages (22,644) and URLs (177,356); two columns: `content` (string) and `label` (integer 0–3: legitimate_email, phishing_email, legitimate_url, phishing_url); format: Parquet; language: English
  - **outputs**:
    - `cybersectony/PhishingEmailDetectionv2.0 (split)` — train (120,000 examples, ~47.2 MB), validation (20,000 examples, ~5.1 MB), test (60,000 examples, ~14.9 MB); total dataset size: ~67.2 MB

#### Activity: `ModelFinetuning`

- **name**: ModelFinetuning
- **task_count**: 1
- **started_at**: 2024-05-09T14:39:02Z
- **ended_at**: 2024-05-09T17:22:51Z
- **duration**: 2h 43m 49s
- **status**: success: 1
  - **hosts**: ip-10-0-4-21.ec2.internal
  - **inputs**:
    - `distilbert/distilbert-base-uncased` — distilled BERT variant; ~67M parameters; pretrained via distillation loss, MLM, and cosine embedding loss on BooksCorpus + English Wikipedia; uncased tokeniser; Apache-2.0 license
    - `cybersectony/PhishingEmailDetectionv2.0 (train split)` — 120,000 tokenised examples (max_length=512, truncation=True), 4-class labels
  - **outputs**:
    - `phishing-email-detection-distilbert_v2.4.1` — DistilBERT with sequence classification head (num_labels=4); trained for 3 epochs via Hugging Face Trainer API

#### Activity: `ModelEvaluation`

- **name**: ModelEvaluation
- **task_count**: 1
- **started_at**: 2024-05-09T17:23:44Z
- **ended_at**: 2024-05-09T17:43:28Z
- **duration**: 19m 44s
- **status**: success: 1
  - **hosts**: ip-10-0-4-21.ec2.internal
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
- **description**: Combined phishing detection dataset of 200,000 English entries (email bodies and URLs). Four-class taxonomy: legitimate_email (0), phishing_email (1), legitimate_url (2), phishing_url (3). Split into train (120,000), validation (20,000), and test (60,000). Format: Parquet with `content` and `label` columns. Total size: ~67.2 MB. License: Apache-2.0
- **reference**: https://huggingface.co/datasets/cybersectony/PhishingEmailDetectionv2.0

### Output Artifacts

**Artifact: `phishing-email-detection-distilbert_v2.4.1`**
- **name**: phishing-email-detection-distilbert_v2.4.1
- **description**: DistilBERT-base-uncased fine-tuned for 4-class phishing detection (legitimate email, phishing email, legitimate URL, phishing URL) using the Hugging Face Trainer API over 3 epochs. Achieves 99.58% accuracy and 99.579% micro-F1 on the evaluation set. Accepts tokenised text up to 512 tokens. License: Apache-2.0.
- **reference**: https://huggingface.co/cybersectony/phishing-email-detection-distilbert_v2.4.1
