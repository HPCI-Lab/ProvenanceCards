---
license: llama3.2
datasets:
- avaliev/chat_doctor
language:
- en
base_model:
- meta-llama/Llama-3.2-3B-Instruct
pipeline_tag: text-generation
library_name: transformers
tags:
- Llama-3.2
- 3B
- Llama-Doctor
- Instruct
- Llama-Cpp
- meta
- pytorch
- safetensors
- Doctor-Llama
---

## Llama-Doctor-3.2-3B-Instruct Modelfile

The **Llama-Doctor-3.2-3B-Instruct** model is designed for **text generation** tasks, particularly in contexts where instruction-following capabilities are needed. This model is a fine-tuned version of the base **Llama-3.2-3B-Instruct** model and is optimized for understanding and responding to user-provided instructions or prompts. The model has been trained on a specialized dataset, **avaliev/chat_doctor**, to enhance its performance in providing conversational or advisory responses, especially in medical or technical fields.

| File Name          { Chat Doctor }                    | Size       | Description                          | Upload Status  |
|----------------------------------------|------------|--------------------------------------|----------------|
| `.gitattributes`                       | 1.57 kB    | Git attributes file                  | Uploaded       |
| `README.md`                            | 263 Bytes  | README file                          | Uploaded       |
| `config.json`                          | 1.03 kB    | Model configuration                  | Uploaded       |
| `generation_config.json`               | 248 Bytes  | Generation configuration             | Uploaded       |
| `pytorch_model-00001-of-00002.bin`     | 4.97 GB    | PyTorch model file (part 1 of 2)     | Uploaded (LFS) |
| `pytorch_model-00002-of-00002.bin`     | 1.46 GB    | PyTorch model file (part 2 of 2)     | Uploaded (LFS) |
| `pytorch_model.bin.index.json`         | 21.2 kB    | Index for PyTorch model              | Uploaded       |
| `special_tokens_map.json`              | 477 Bytes  | Special tokens map                   | Uploaded       |
| `tokenizer.json`                       | 17.2 MB    | Tokenizer file                       | Uploaded (LFS) |
| `tokenizer_config.json`                | 57.4 kB    | Tokenizer configuration              | Uploaded       |

| Model Type | Size | Context Length | Link |
|------------|------|----------------|------|
| GGUF | 3B | - | [🤗 Llama-Doctor-3.2-3B-Instruct-GGUF](https://huggingface.co/prithivMLmods/Llama-Doctor-3.2-3B-Instruct-GGUF) |

### Key Use Cases:
1. **Conversational AI**: Engage in dialogue, answering questions, or providing responses based on user instructions.
2. **Text Generation**: Generate content, summaries, explanations, or solutions to problems based on given prompts.
3. **Instruction Following**: Understand and execute instructions, potentially in complex or specialized domains like medical, technical, or academic fields.

The model leverages a **PyTorch-based architecture** and comes with various files such as configuration files, tokenizer files, and special tokens maps to facilitate smooth deployment and interaction.

### Intended Applications:
- **Chatbots** for customer support or virtual assistants.
- **Medical Consultation Tools** for generating advice or answering medical queries (given its training on the **chat_doctor** dataset).
- **Content Creation** tools, helping generate text based on specific instructions.
- **Problem-solving Assistants** that offer explanations or answers to user queries, particularly in instructional contexts.
---
license: apache-2.0
task_categories:
- question-answering
language:
- en
tags:
- medical
pretty_name: ChatDoctor
size_categories:
- 100K<n<1M
---
This dataset was formed from the three data sources from the ChatDoctor work.

100k real conversations between patients and doctors from HealthCareMagic.com HealthCareMagic-100k. - ADDED

10k real conversations between patients and doctors from icliniq.com icliniq-10k. - ADDED

5k generated conversations between patients and physicians from ChatGPT GenMedGPT-5k and disease database. - NOT ADDED (because of the data created by LLM, but you could add it manually)


data sample:
```json
{'instruction': "If you are a doctor, please answer the medical questions based on the patient's description.",
 'input': "I woke up this morning feeling the whole room is spinning when i was sitting down. I went to the bathroom walking unsteadily, as i tried to focus i feel nauseous. I try to vomit but it wont come out.. After taking panadol and sleep for few hours, i still feel the same.. By the way, if i lay down or sit down, my head do not spin, only when i want to move around then i feel the whole world is spinning.. And it is normal stomach discomfort at the same time? Earlier after i relieved myself, the spinning lessen so i am not sure whether its connected or coincidences.. Thank you doc!",
 'output': "Hi, Thank you for posting your query. The most likely cause for your symptoms is benign paroxysmal positional vertigo (BPPV), a type of peripheral vertigo. In this condition, the most common symptom is dizziness or giddiness, which is made worse with movements. Accompanying nausea and vomiting are common. The condition is due to problem in the ear, and improves in a few days on own. Betahistine tablets would help relieve your symptoms. Doing vestibular rehabilitation or adaptation exercises would prevent the recurrence of these symptoms. An ENT evaluation would also help. I hope it helps. Best wishes, Chat Doctor. "}
```

```
@article{li2023chatdoctor,
  title={ChatDoctor: A Medical Chat Model Fine-Tuned on a Large Language Model Meta-AI (LLaMA) Using Medical Domain Knowledge},
  author={Li, Yunxiang and Li, Zihan and Zhang, Kai and Dan, Ruilong and Jiang, Steve and Zhang, You},
  journal={Cureus},
  volume={15},
  number={6},
  year={2023},
  publisher={Cureus}
}
```
# Workflow Card: Use Case 1 — ChatDoctor Medical LLM Fine-Tuning

---

## 1. Workflow

- **name**: chatdoctor_llama32_finetuning
- **description**: End-to-end ML workflow that fine-tunes Meta's Llama-3.2-3B-Instruct on the ChatDoctor medical conversation dataset to produce a specialised medical dialogue model (Llama-Doctor-3.2-3B-Instruct) capable of answering patient queries in a conversational, instruction-following style.

---

## 2. Summary

- **execution_id**: chatdoctor_llama32_finetuning_v0
- **version**: 0
- **started_at**: ~ 
- **ended_at**: ~
- **duration**: ~
- **status**: Completed
- **location**: ~
- **user**: ~
- **entrypoint.repository**: https://huggingface.co/prithivMLmods/Llama-Doctor-3.2-3B-Instruct
- **entrypoint.branch**: ~
- **entrypoint.short_sha**: ~

---

## 3. Infrastructure

- **host_os**: ~
- **compute_hardware**: ~
- **runtime_environment**: ~
- **resource_manager**: ~
- **primary_software**: Python, PyTorch, Hugging Face Transformers (≥4.43.0), safetensors
- **environment_snapshot**: ~

---

## 4. Overview

### 4.1 Run Summary

- **total_activities**: 3
- **status_counts**: finished: 3
- **arguments**: ~

**Notable Inputs:**
  - `avaliev/chat_doctor` — format: HuggingFace dataset (instruction-following JSON), size: 110 000 conversations (100k HealthCareMagic + 10k iCliniq), source: https://huggingface.co/datasets/avaliev/chat_doctor
  - `meta-llama/Llama-3.2-3B-Instruct` — format: safetensors model weights (PyTorch), size: ~6.43 GB (two-shard BF16), source: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct

**Notable Outputs:**
  - `Llama-Doctor-3.2-3B-Instruct` — type: fine-tuned language model (safetensors + GGUF), size: ~6.43 GB, location: https://huggingface.co/prithivMLmods/Llama-Doctor-3.2-3B-Instruct

**Structure (activity DAG):**
  1. DataPreparation
  2. ModelFinetuning
  3. ModelEvaluation

- **observations**: Only the HealthCareMagic-100k and iCliniq-10k splits were used; the 5k ChatGPT-generated GenMedGPT-5k split was deliberately excluded due to the LLM-origin of its content. The resulting model targets conversational medical QA, chatbot, and advisory applications.

### 4.2 Resource Usage

- **cpu**: ~
- **memory**: ~
- **gpu**: Training utilised H100-80GB GPU cluster (Meta's production infrastructure for the base model pretraining; fine-tuning hardware not specified)
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
    - `HealthCareMagic-100k` — 100 000 real patient–doctor conversations from HealthCareMagic.com; format: instruction/input/output JSON triples
    - `iCliniq-10k` — 10 000 real patient–doctor conversations from iCliniq.com; format: instruction/input/output JSON triples
  - **outputs**:
    - `avaliev/chat_doctor` — merged, deduplicated instruction-tuning dataset of 110 000 examples ready for supervised fine-tuning

#### Activity: `ModelFinetuning`

- **name**: ModelFinetuning
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `meta-llama/Llama-3.2-3B-Instruct` — pretrained base model; PyTorch BF16 safetensors, 3.21B parameters, 128k context, Llama 3.2 Community License
    - `avaliev/chat_doctor` — 110 000-example instruction-tuning dataset
  - **outputs**:
    - `Llama-Doctor-3.2-3B-Instruct` — fine-tuned model weights; BF16 safetensors (two-shard, ~6.43 GB) + GGUF variant; architecture identical to base model

#### Activity: `ModelEvaluation`

- **name**: ModelEvaluation
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `Llama-Doctor-3.2-3B-Instruct` — fine-tuned model to be assessed
  - **outputs**:
    - `evaluation_report` — qualitative assessment of instruction-following and medical response quality; quantitative benchmark results not published

---

## 6. Significant Artifacts

### Input Artifacts

**Artifact: `meta-llama/Llama-3.2-3B-Instruct`**
- **name**: meta-llama/Llama-3.2-3B-Instruct
- **description**: Pretrained Llama 3.2 instruction-tuned text model with 3.21B parameters. Auto-regressive transformer trained on up to 9T tokens (data cutoff December 2023) using SFT and RLHF. Supports multilingual text generation with 128k context length.
- **reference**: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct

**Artifact: `avaliev/chat_doctor`**
- **name**: avaliev/chat_doctor
- **description**: Medical instruction-tuning dataset combining 100k HealthCareMagic and 10k iCliniq real patient–doctor conversations, formatted as instruction/input/output triples for supervised fine-tuning. License: Apache-2.0.
- **reference**: https://huggingface.co/datasets/avaliev/chat_doctor

### Output Artifacts

**Artifact: `Llama-Doctor-3.2-3B-Instruct`**
- **name**: Llama-Doctor-3.2-3B-Instruct
- **description**: Fine-tuned Llama 3.2 3B model specialised for medical conversational QA. Distributed as BF16 safetensors (two shards: 4.97 GB + 1.46 GB) and a GGUF variant. Intended for chatbot, medical consultation, and content-generation applications.
- **reference**: https://huggingface.co/prithivMLmods/Llama-Doctor-3.2-3B-Instruct
