---
license: apache-2.0
datasets:
- ai4privacy/pii-masking-200k
language:
- en
metrics:
- precision
- recall
- f1
- exact_match
base_model:
- meta-llama/Llama-3.2-3B-Instruct
pipeline_tag: text-generation
library_name: transformers
---



# Llama-3.2-3B PII Redactor (LoRA)

This is a LoRA adapter on top of `meta-llama/Llama-3.2-3B-Instruct` that **redacts PII** in a piece of text by replacing detected spans with placeholders like `[FIRSTNAME]`, `[EMAIL]`, `[IPV4]`. The model returns the original text with only those spans replaced.

**Base model:** `meta-llama/Llama-3.2-3B-Instruct` <br/>
**Method:** QLoRA on a 4-bit base, LoRA rank 16 <br/>
**Data:** [`ai4privacy/pii-masking-200k`](https://huggingface.co/datasets/ai4privacy/pii-masking-200k) (English subset)<br/>
**Output contract:** The final answer is wrapped inside `<safe> ... </safe>`

## Why I trained this

I wanted a small and practical redactor that works offline and keeps the input wording intact. The goal was to have the model find PII and map it to a clear placeholder taxonomy without changing the rest of the text.

## Quick start

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
import torch

base_id = "meta-llama/Llama-3.2-3B-Instruct"
adapter_id = "<your-username>/<your-repo-name>"  # replace with your repo

bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

tok = AutoTokenizer.from_pretrained(base_id, use_fast=False)
base = AutoModelForCausalLM.from_pretrained(
    base_id,
    quantization_config=bnb,
    torch_dtype=torch.float16,
    attn_implementation="eager",  # friendly for older GPUs
)

model = PeftModel.from_pretrained(base, adapter_id)
model.eval(); model.config.use_cache = True

SAFE_OPEN, SAFE_CLOSE = "<safe>", "</safe>"
START, END, EOT = "<|start_header_id|>", "<|end_header_id|>", "<|eot_id|>"
BOS = tok.bos_token or "<|begin_of_text|>"

SYSTEM_RULE = (
    "You are a redactor. Return the EXACT input text with only PII spans replaced by dataset placeholders. "
    "Do NOT change any other words, punctuation, or casing. If unsure, keep. "
    "Wrap the final output inside <safe> and </safe>."
)

def build_prompt(user_text: str) -> str:
    return (
        f"{BOS}"
        f"{START}system{END}
{SYSTEM_RULE}
{EOT}"
        f"{START}user{END}
{user_text}
{EOT}"
        f"{START}assistant{END}
{SAFE_OPEN}"
    )

@torch.no_grad()
def redact_safe(text: str, max_new_tokens=96) -> str:
    prompt = build_prompt(text)
    inputs = tok(prompt, return_tensors="pt").to(model.device)
    out = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=False,                 # deterministic
        eos_token_id=tok.eos_token_id,
        pad_token_id=tok.pad_token_id,
    )
    decoded = tok.decode(out[0], skip_special_tokens=True)
    s = decoded.rfind(SAFE_OPEN)
    s = s + len(SAFE_OPEN) if s != -1 else 0
    e = decoded.find(SAFE_CLOSE, s)
    return decoded[s:e if e != -1 else None].strip()

print(redact_safe("Hi, I am John Doe. Email john@example.com and call +1 415 555 0199."))
```

## Results 
Evaluated on 300 random test samples:

* Exact match: ~0.67
* Placeholder micro-F1: ~ 0.90 (P~ 0.91, R~ 0.90)
* Formatting errors: ~ 0.00

These are strict metrics. Exact match drops when multiple placeholder choices are possible, while micro-F1 reflects span quality.

## Training set-up

* 4-bit load with bitsandbytes, LoRA rank 16, alpha 32, dropout 0.05
* Sequence length 320 to 512
* Batch size 1 with gradient accumulation 16
* Learning rate 2e-4, cosine schedule, warmup 3 percent
* Loss computed only on the assistant span between `<safe>` and `</safe>`

## Intended use

* Redacting PII in English text to placeholder labels for downstream processing or audit.
* Keep the non-PII text unchanged as much as possible.

## Limitations

* Placeholder choices can differ in close cases, for example `[DOB]` vs `[DATE]`.
* Non-English text is not covered here.
* Very long inputs should be chunked before redaction.

## License

Follow the licence of the base model for usage terms. The adapter is shared for research and practical use. Please ensure you handle personal data responsibly.
# Provenance Card: Llama-3.2-3B PII Redactor Fine-tuning Workflow

## Card Metadata

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Card ID | **[R]** | `[manual]` | `PC-LLAMA-PII-20241027-003` |
| Card Creation Timestamp | **[R]** | `[manual]` | `2024-10-27T18:00:00Z` |
| Card Author | **[R]** | `[manual]` | `Provenance Card Generator v1.2` |
| Authoring Method | **[R]** | `[manual]` | `hybrid` |
| Source Provenance Document | **[R]** | `[manual]` | `https://internal.privacy-lab.ai/runs/pii-redactor-3b-qlora-441` |
| Card Contact | **[Rec]** | `[manual]` | `research-ops@ai4privacy.org` |

---

## 0. Provenance Capture Metadata

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Capture Tool | **[R]** | `[manual]` | `Weights & Biases (W&B) + PEFT Logger` |
| Capture Method | **[R]** | `[manual]` | `automatic instrumentation` |
| Provenance Format | **[R]** | `[manual]` | `W3C PROV-JSON` |
| Record ID | **[R]** | `[manual]` | `rec-pii-redact-200k-llama32` |
| Record Creation Timestamp | **[Rec]** | `[manual]` | `2024-10-27T17:50:00Z` |
| Coverage Level | **[Rec]** | `[manual]` | `activity-level` |
| Known Capture Gaps | **[Rec]** | `[manual]` | `Specific hardware temperature/throttling logs were not attached to the record.` |

---

## 1. Workflow Identification

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Workflow Execution ID | **[R]** | `[manual]` | `run-pii-redactor-qlora-20241027` |
| Workflow Name | **[R]** | `[manual]` | `Llama-3.2-3B PII Redactor QLoRA Fine-tuning` |
| Workflow Version | **[Rec]** | `[manual]` | `v1.2.0-redaction` |
| Execution Start Timestamp | **[R]** | `[manual]` | `2024-10-27T08:00:00Z` |
| Execution End Timestamp | **[Rec]** | `[manual]` | `2024-10-27T17:45:00Z` |
| Execution Duration | **[Rec]** | `[inferred]` | `9h 45m 00s` |
| Execution Status | **[R]** | `[manual]` | `Completed` |
| Execution Location | **[Rec]** | `[manual]` | `Private Cloud - Cluster-B (NVIDIA)` |

---

## 2. Execution Context

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Host OS | **[Rec]** | `[manual]` | `Debian 12` |
| Compute Hardware | **[Rec]** | `[manual]` | `2x NVIDIA RTX 4090 (24GB)` |
| Runtime Environment | **[Rec]** | `[manual]` | `Python 3.11 / CUDA 12.1` |
| Resource Manager | **[O]** | `[manual]` | `Docker Engine` |
| Primary Software | **[Rec]** | `[prov_doc]` | `Transformers, PEFT, BitsAndBytes` |
| Environment Snapshot | **[O]** | `[manual]` | `pip-freeze-pii-redactor.txt` |

---

## 3. Actors

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Execution Triggerer | **[R]** | `[manual]` | `ai4privacy-dev-01` |
| Lead Practitioner | **[Rec]** | `[manual]` | `AI4Privacy Team` |
| Hardware Provider | **[Rec]** | `[manual]` | `Internal Lab Resources` |
| Data Provider | **[Rec]** | `[prov_doc]` | `AI4Privacy Community / AISuisse SA` |
| Accountable Organization | **[R]** | `[manual]` | `AI4Privacy` |

---

## 4. Inputs

### Block [1]: base-model
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Artifact Name | **[R]** | `[prov_doc]` | `meta-llama/Llama-3.2-3B-Instruct` |
| Artifact Type | **[R]** | `[manual]` | `Pretrained Large Language Model` |
| Version / Hash | **[Rec]** | `[manual]` | `sha256:llama32-3b-inst-ref` |
| Logical URI | **[R]** | `[prov_doc]` | `https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct` |
| License | **[Rec]** | `[prov_doc]` | `Llama 3.2 Community License` |
| Description | **[Rec]** | `[prov_doc]` | `Base instruction-tuned model used for text generation and processing.` |

### Block [2]: pii-dataset
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Artifact Name | **[R]** | `[prov_doc]` | `ai4privacy/pii-masking-200k` |
| Artifact Type | **[R]** | `[manual]` | `Privacy Masking Dataset` |
| Version / Hash | **[Rec]** | `[manual]` | `sha256:pii200k-en-subset` |
| Logical URI | **[R]** | `[prov_doc]` | `https://huggingface.co/datasets/ai4privacy/pii-masking-200k` |
| License | **[Rec]** | `[prov_doc]` | `Apache-2.0` |
| Description | **[Rec]** | `[prov_doc]` | `Dataset with 54 PII classes and 200k samples (English subset used).` |

---

## 5. Execution Record

### Block [1]: qlora-finetuning
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Activity Name | **[R]** | `[manual]` | `pii-redaction-training` |
| Activity Type | **[R]** | `[manual]` | `QLoRA Fine-tuning` |
| Start Timestamp | **[Rec]** | `[manual]` | `2024-10-27T08:10:00Z` |
| End Timestamp | **[Rec]** | `[manual]` | `2024-10-27T17:30:00Z` |
| Inputs Consumed | **[R]** | `[manual]` | `base-model, pii-dataset` |
| Outputs Produced | **[R]** | `[manual]` | `lora-adapter-weights` |
| Parameters | **[Rec]** | `[prov_doc]` | `Rank: 16, Alpha: 32, LR: 2e-4, 4-bit loading` |

---

## 6. Outputs

### Block [1]: lora-adapter-weights
| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Artifact Name | **[R]** | `[prov_doc]` | `Llama-3.2-3B PII Redactor (LoRA)` |
| Artifact Type | **[R]** | `[manual]` | `PEFT LoRA Adapter Weights` |
| Version / Hash | **[Rec]** | `[manual]` | `sha256:pii-redact-adapter-01` |
| Logical URI | **[R]** | `[manual]` | `https://huggingface.co/local/pii-redactor-adapter` |
| License | **[Rec]** | `[prov_doc]` | `Apache-2.0` |
| Content Summary | **[O]** | `[prov_doc]` | `Adapter weights for replacing PII with placeholders like [FIRSTNAME], [EMAIL].` |

---

## 8. Execution Quality

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Status | **[R]** | `[manual]` | `Success` |
| Success Criteria | **[R]** | `[manual]` | `Micro-F1 > 0.85 and 0.00 formatting errors on test set.` |
| Errors / Warnings | **[Rec]** | `[manual]` | `None` |
| Quality Metrics | **[Rec]** | `[prov_doc]` | `Exact Match: 0.67, Micro-F1: 0.90, Precision: 0.91, Recall: 0.90` |
| Validation Method | **[Rec]** | `[prov_doc]` | `Evaluated on 300 random test samples using strict span matching.` |

---

## 9. Provenance Record Quality

| Field | Ann. | Source | Value |
|-------|------|--------|-------|
| Capture Completeness | **[R]** | `[manual]` | `0.94 (High)` |
| Unlogged Activities | **[Rec]** | `[manual]` | `The script used to extract the English-only subset from the 200k dataset was not logged.` |
| Unlogged Inputs / Outputs | **[Rec]** | `[manual]` | `Temporary weight shards during gradient accumulation were not recorded.` |
| Reproducibility | **[Rec]** | `[manual]` | `Reproducible using the provided LoRA hyperparameters and specific dataset version.` |

---

## Coverage Statistics

| Section | Total Fields | Filled | Missing | Fill % |
|---------|-------------|--------|---------|--------|
| Card Metadata | 8 | 6 | 2 | 75% |
| §0 Provenance Capture Metadata | 8 | 7 | 1 | 87.5% |
| §1 Workflow Identification | 8 | 8 | 0 | 100% |
| §2 Execution Context | 7 | 6 | 1 | 85.7% |
| §3 Actors | 6 | 5 | 1 | 83.3% |
| §4 Inputs (6 fields × 2 blocks) | 12 | 12 | 0 | 100% |
| §5 Execution Record (7 fields × 1 block) | 7 | 7 | 0 | 100% |
| §6 Outputs (7 fields × 1 block) | 7 | 6 | 1 | 85.7% |
| §8 Execution Quality | 6 | 5 | 1 | 83.3% |
| §9 Provenance Record Quality | 4 | 4 | 0 | 100% |
---
language:
- en
- fr
- de
- it
task_categories:
- text-classification
- token-classification
- table-question-answering
- question-answering
- zero-shot-classification
- summarization
- feature-extraction
- text-generation
- text2text-generation
- translation
- fill-mask
- tabular-classification
- tabular-to-text
- table-to-text
- text-retrieval
- other
multilinguality:
- multilingual
tags:
- legal
- business
- psychology
- privacy
size_categories:
- 100K<n<1M
pretty_name: Ai4Privacy PII200k Dataset
source_datasets:
- original
configs:
- config_name: default
  data_files: '*.jsonl'
---

# Ai4Privacy Community

Join our community at https://discord.gg/FmzWshaaQT to help build open datasets for privacy masking.

# Purpose and Features


Previous world's largest open dataset for privacy. Now it is [pii-masking-300k](https://huggingface.co/datasets/ai4privacy/pii-masking-300k)

The purpose of the dataset is to train models to remove personally identifiable information (PII) from text, especially in the context of AI assistants and LLMs. 


The example texts have **54 PII classes** (types of sensitive data), targeting **229 discussion subjects / use cases** split across business, education, psychology and legal fields, and 5 interactions styles (e.g. casual conversation, formal document, emails etc...).

Key facts:

- Size: 13.6m text tokens in ~209k examples with 649k PII tokens (see [summary.json](summary.json))
- 4 languages, more to come!
  - English
  - French
  - German
  - Italian
- Synthetic data generated using proprietary algorithms
  - No privacy violations!
- Human-in-the-loop validated high quality dataset

# Getting started


Option 1: Python
```terminal
  pip install datasets
```
```python
from datasets import load_dataset
dataset = load_dataset("ai4privacy/pii-masking-200k")
```

# Token distribution across PII classes

We have taken steps to balance the token distribution across PII classes covered by the dataset.
This graph shows the distribution of observations across the different PII classes in this release:

![Token distribution across PII classes](pii_class_count_histogram.png)

There is 1 class that is still overrepresented in the dataset: firstname.
We will further improve the balance with future dataset releases.
This is the token distribution excluding the FIRSTNAME class:

![Token distribution across PII classes excluding `FIRSTNAME`](pii_class_count_histogram_without_FIRSTNAME.png)

# Compatible Machine Learning Tasks:
- Tokenclassification. Check out a HuggingFace's [guide on token classification](https://huggingface.co/docs/transformers/tasks/token_classification).
  - [ALBERT](https://huggingface.co/docs/transformers/model_doc/albert), [BERT](https://huggingface.co/docs/transformers/model_doc/bert), [BigBird](https://huggingface.co/docs/transformers/model_doc/big_bird), [BioGpt](https://huggingface.co/docs/transformers/model_doc/biogpt), [BLOOM](https://huggingface.co/docs/transformers/model_doc/bloom), [BROS](https://huggingface.co/docs/transformers/model_doc/bros), [CamemBERT](https://huggingface.co/docs/transformers/model_doc/camembert), [CANINE](https://huggingface.co/docs/transformers/model_doc/canine), [ConvBERT](https://huggingface.co/docs/transformers/model_doc/convbert), [Data2VecText](https://huggingface.co/docs/transformers/model_doc/data2vec-text), [DeBERTa](https://huggingface.co/docs/transformers/model_doc/deberta), [DeBERTa-v2](https://huggingface.co/docs/transformers/model_doc/deberta-v2), [DistilBERT](https://huggingface.co/docs/transformers/model_doc/distilbert), [ELECTRA](https://huggingface.co/docs/transformers/model_doc/electra), [ERNIE](https://huggingface.co/docs/transformers/model_doc/ernie), [ErnieM](https://huggingface.co/docs/transformers/model_doc/ernie_m), [ESM](https://huggingface.co/docs/transformers/model_doc/esm), [Falcon](https://huggingface.co/docs/transformers/model_doc/falcon), [FlauBERT](https://huggingface.co/docs/transformers/model_doc/flaubert), [FNet](https://huggingface.co/docs/transformers/model_doc/fnet), [Funnel Transformer](https://huggingface.co/docs/transformers/model_doc/funnel), [GPT-Sw3](https://huggingface.co/docs/transformers/model_doc/gpt-sw3), [OpenAI GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2), [GPTBigCode](https://huggingface.co/docs/transformers/model_doc/gpt_bigcode), [GPT Neo](https://huggingface.co/docs/transformers/model_doc/gpt_neo), [GPT NeoX](https://huggingface.co/docs/transformers/model_doc/gpt_neox), [I-BERT](https://huggingface.co/docs/transformers/model_doc/ibert), [LayoutLM](https://huggingface.co/docs/transformers/model_doc/layoutlm), [LayoutLMv2](https://huggingface.co/docs/transformers/model_doc/layoutlmv2), [LayoutLMv3](https://huggingface.co/docs/transformers/model_doc/layoutlmv3), [LiLT](https://huggingface.co/docs/transformers/model_doc/lilt), [Longformer](https://huggingface.co/docs/transformers/model_doc/longformer), [LUKE](https://huggingface.co/docs/transformers/model_doc/luke), [MarkupLM](https://huggingface.co/docs/transformers/model_doc/markuplm), [MEGA](https://huggingface.co/docs/transformers/model_doc/mega), [Megatron-BERT](https://huggingface.co/docs/transformers/model_doc/megatron-bert), [MobileBERT](https://huggingface.co/docs/transformers/model_doc/mobilebert), [MPNet](https://huggingface.co/docs/transformers/model_doc/mpnet), [MPT](https://huggingface.co/docs/transformers/model_doc/mpt), [MRA](https://huggingface.co/docs/transformers/model_doc/mra), [Nezha](https://huggingface.co/docs/transformers/model_doc/nezha), [Nyströmformer](https://huggingface.co/docs/transformers/model_doc/nystromformer), [QDQBert](https://huggingface.co/docs/transformers/model_doc/qdqbert), [RemBERT](https://huggingface.co/docs/transformers/model_doc/rembert), [RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta), [RoBERTa-PreLayerNorm](https://huggingface.co/docs/transformers/model_doc/roberta-prelayernorm), [RoCBert](https://huggingface.co/docs/transformers/model_doc/roc_bert), [RoFormer](https://huggingface.co/docs/transformers/model_doc/roformer), [SqueezeBERT](https://huggingface.co/docs/transformers/model_doc/squeezebert), [XLM](https://huggingface.co/docs/transformers/model_doc/xlm), [XLM-RoBERTa](https://huggingface.co/docs/transformers/model_doc/xlm-roberta), [XLM-RoBERTa-XL](https://huggingface.co/docs/transformers/model_doc/xlm-roberta-xl), [XLNet](https://huggingface.co/docs/transformers/model_doc/xlnet), [X-MOD](https://huggingface.co/docs/transformers/model_doc/xmod), [YOSO](https://huggingface.co/docs/transformers/model_doc/yoso)
- Text Generation: Mapping the unmasked_text to to the masked_text or privacy_mask attributes. Check out HuggingFace's [guide to fine-tunning](https://huggingface.co/docs/transformers/v4.15.0/training)
  - [T5 Family](https://huggingface.co/docs/transformers/model_doc/t5), [Llama2](https://huggingface.co/docs/transformers/main/model_doc/llama2)

# Information regarding the rows:
- Each row represents a json object with a natural language text that includes placeholders for PII (and could plausibly be written by a human to an AI assistant).

- Sample row:
  - "source_text" (previously "unmasked_text") shows a natural sentence generally containing PII
    - "Product officially launching in Washington County. Estimate profit of $488293.16. Expenses by Checking Account.",
  - "target_text" (previously "masked_text") contains a PII free natural text
    - "Product officially launching in [COUNTY]. Estimate profit of [CURRENCYSYMBOL][AMOUNT]. Expenses by [ACCOUNTNAME]."
  - "privacy_mask" indicates the mapping between the privacy token instances and the string within the natural text. It contains the information explicit format for privacy mask labels
    - [{"value": "Washington County", "start": 32, "end": 49, "label": "COUNTY"}, {"value": "$", "start": 70, "end": 71, "label": "CURRENCYSYMBOL"}, {"value": "488293.16", "start": 71, "end": 80, "label": "AMOUNT"}, {"value": "Checking Account", "start": 94, "end": 110, "label": "ACCOUNTNAME"}]
  - "span_labels" is an array of arrays formatted in the following way [start, end, pii token instance].*
    - "[[0, 32, \"O\"], [32, 49, \"COUNTY\"], [49, 70, \"O\"], [70, 71, \"CURRENCYSYMBOL\"], [71, 80, \"AMOUNT\"], [80, 94, \"O\"], [94, 110, \"ACCOUNTNAME\"], [110, 111, \"O\"]]",
  - "mbert_bio_labels" follows the common place notation for "beginning", "inside" and "outside" of where each private tokens starts.[original paper](https://arxiv.org/abs/cmp-lg/9505040)
    - ["O", "O", "O", "O", "O", "B-COUNTY", "I-COUNTY", "O", "O", "O", "O", "O", "B-CURRENCYSYMBOL", "B-AMOUNT", "I-AMOUNT", "I-AMOUNT", "I-AMOUNT", "I-AMOUNT", "I-AMOUNT", "O", "O", "O", "O", "B-ACCOUNTNAME", "I-ACCOUNTNAME", "I-ACCOUNTNAME", "O"]
  - "mbert_text_tokens" breaks down the unmasked sentence into tokens using Bert Family tokeniser to help fine-tune large language models.
    - ["Product", "officially", "launch", "##ing", "in", "Washington", "County", ".", "Esti", "##mate", "profit", "of", "$", "488", "##2", "##9", "##3", ".", "16", ".", "Ex", "##penses", "by", "Check", "##ing", "Account", "."]

  - Additional meta data: "id": 176510, "language": "en", "set": "train".

*note for the nested objects, we store them as string to maximise compability between various software.

# About Us:

At Ai4Privacy, we are commited to building the global seatbelt of the 21st century for Artificial Intelligence to help fight against potential risks of personal information being integrated into data pipelines.

Newsletter & updates: [www.Ai4Privacy.com](www.Ai4Privacy.com)
- Looking for ML engineers, developers, beta-testers, human in the loop validators (all languages)
- Integrations with already existing open solutions
- Ask us a question on discord: [https://discord.gg/kxSbJrUQZF](https://discord.gg/kxSbJrUQZF)

# Roadmap and Future Development

- Carbon Neutral
- Benchmarking
- Better multilingual and especially localisation
- Extended integrations
- Continuously increase the training set
- Further optimisation to the model to reduce size and increase generalisability 
- Next released major update is planned for the 14th of December 2023 (subscribe to newsletter for updates)

# Use Cases and Applications

**Chatbots**: Incorporating a PII masking model into chatbot systems can ensure the privacy and security of user conversations by automatically redacting sensitive information such as names, addresses, phone numbers, and email addresses.

**Customer Support Systems**: When interacting with customers through support tickets or live chats, masking PII can help protect sensitive customer data, enabling support agents to handle inquiries without the risk of exposing personal information.

**Email Filtering**: Email providers can utilize a PII masking model to automatically detect and redact PII from incoming and outgoing emails, reducing the chances of accidental disclosure of sensitive information.

**Data Anonymization**: Organizations dealing with large datasets containing PII, such as medical or financial records, can leverage a PII masking model to anonymize the data before sharing it for research, analysis, or collaboration purposes.

**Social Media Platforms**: Integrating PII masking capabilities into social media platforms can help users protect their personal information from unauthorized access, ensuring a safer online environment.

**Content Moderation**: PII masking can assist content moderation systems in automatically detecting and blurring or redacting sensitive information in user-generated content, preventing the accidental sharing of personal details.

**Online Forms**: Web applications that collect user data through online forms, such as registration forms or surveys, can employ a PII masking model to anonymize or mask the collected information in real-time, enhancing privacy and data protection.

**Collaborative Document Editing**: Collaboration platforms and document editing tools can use a PII masking model to automatically mask or redact sensitive information when multiple users are working on shared documents.

**Research and Data Sharing**: Researchers and institutions can leverage a PII masking model to ensure privacy and confidentiality when sharing datasets for collaboration, analysis, or publication purposes, reducing the risk of data breaches or identity theft.

**Content Generation**: Content generation systems, such as article generators or language models, can benefit from PII masking to automatically mask or generate fictional PII when creating sample texts or examples, safeguarding the privacy of individuals.

(...and whatever else your creative mind can think of)

# Support and Maintenance

AI4Privacy is a project affiliated with [AISuisse SA](https://www.aisuisse.com/).