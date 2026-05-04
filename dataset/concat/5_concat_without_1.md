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