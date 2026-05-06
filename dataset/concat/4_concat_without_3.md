---
license: other
license_name: nvidia-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
pipeline_tag: text-generation
datasets:
- nvidia/Nemotron-Cascade-2-SFT-Data
- nvidia/Nemotron-Cascade-2-RL-data
language:
- en
- es
- fr
- de
- it
- ja
library_name: transformers
tags:
- nvidia
- pytorch
- mamba2
- moe
- mixture-of-experts
- hybrid
- reasoning
- qlora
- bitsandbytes
- 4bit
base_model:
- nvidia/Nemotron-Cascade-2-30B-A3B
---
# openNemo-Cascade-2-30B-A3B

![openNemo](openNemo.jpg)

**Pure-PyTorch drop-in replacement for NVIDIA's [Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B).**

Removes all external CUDA kernel dependencies (`mamba-ssm`, `causal-conv1d`) and replaces them with native PyTorch operations, making the model fully compatible with **bitsandbytes 4-bit quantization** and **QLoRA fine-tuning** on consumer GPUs.

30B total parameters, 3B active per token. Loads in **17 GB VRAM** with 4-bit quantization.

By **[Empero AI](https://empero.org)**

---

## Why?

NVIDIA's Nemotron-Cascade-2 is a 30B MoE reasoning model that achieves gold medal performance on IMO 2025 and IOI 2025. But the original implementation depends on `mamba-ssm` and `causal-conv1d`, which ship pre-compiled Triton/CUDA kernels that:

- **Break bitsandbytes quantization** — the kernels call `F.linear` directly, colliding with bnb's `__torch_function__` hook on quantized weights
- **Require specific CUDA versions** — kernel compilation failures are common on consumer setups
- **Prevent QLoRA training** — you can't fine-tune what you can't quantize

openNemo Cascade fixes all of that. Same weights, same architecture, pure PyTorch.

## What Changed

| Component | Original (NVIDIA) | openNemo Cascade |
|---|---|---|
| `rmsnorm_fn` | `mamba_ssm.ops.triton.layer_norm` | Pure PyTorch group-wise RMSNorm + SiLU gating |
| `ssd_combined` | `mamba_ssm.ops.triton.ssd_combined` | Chunked SSD scan with einsum contractions |
| `selective_state_update` | `mamba_ssm.ops.triton.selective_state_update` | Pure PyTorch SSM step |
| `causal_conv1d_fn` | `causal_conv1d` package | `nn.Conv1d` with causal padding |
| Forward routing | Fast path (kernels) vs slow path | Optimized torch path only |
| `.model` accessor | Only `.backbone` | `.model` property alias (PEFT/LoRA compatible) |
| Async weight loading | OOM on large MoE models | Auto-disabled for safe 4-bit loading |

**All weight names are preserved** — loads NVIDIA's original checkpoint directly with zero conversion.

## Quickstart

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    "empero-ai/openNemo-Cascade-2-30B-A3B",
    quantization_config=bnb_config,
    trust_remote_code=True,
    device_map="auto",
)

tokenizer = AutoTokenizer.from_pretrained("empero-ai/openNemo-Cascade-2-30B-A3B")

# Thinking mode (reasoning)
messages = [{"role": "user", "content": "Prove that the sum of the first n odd numbers equals n²."}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

output = model.generate(**inputs, max_new_tokens=2048, do_sample=True, temperature=1.0, top_p=0.95)
response = tokenizer.decode(output[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
print(response)
```

No `mamba-ssm` install needed. Just `pip install transformers bitsandbytes` and go.

### Instruct Mode (non-thinking)

```python
# Set enable_thinking=False to skip the <think> reasoning chain
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
```

### QLoRA Fine-Tuning

```python
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=64,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "down_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
```

## Architecture

Nemotron-Cascade-2 is a 52-layer hybrid model with four block types defined by the pattern:

```
M E M E M * E M E M E M * E M E M E M * E M E M E M * E M E M E M * E M E M E M E M * E M E M E M E
```

- **M** — Mamba2 SSM block (23 layers) — chunked structured state-space duality
- **E** — Mixture-of-Experts block (23 layers) — 128 routed experts, top-6 selected per token
- **\*** — Grouped Query Attention block (6 layers) — sparse GQA with 32 heads, 2 KV heads
- **-** — MLP block (not used in Cascade)

| Parameter | Value |
|---|---|
| Total parameters | 30.87B |
| Active parameters per token | ~3B |
| Hidden size | 2,688 |
| MoE layers | 23 |
| Routed experts per layer | 128 |
| Experts selected per token | 6 |
| Expert intermediate size | 1,856 |
| Shared experts per layer | 1 |
| Shared expert intermediate size | 3,712 |
| Mamba2 heads | 64 |
| Mamba2 head dim | 64 |
| SSM state size | 128 |
| Attention heads | 32 (2 KV heads) |
| Max context length | 262,144 tokens |
| Vocabulary size | 131,072 |

### 4-bit Memory Usage

| Setup | VRAM |
|---|---|
| bf16 (full precision) | ~65 GB |
| 4-bit NF4 + double quant | **~17 GB** |
| 4-bit + QLoRA (r=64) | ~19 GB |

## Benchmark Results

From the [original NVIDIA technical report](https://arxiv.org/abs/2603.19220):

| Benchmark | Nemotron-Cascade-2 |
|---|---|
| **IMO 2025** | **35 pts (Gold Medal)** |
| **IOI 2025** | **439.3 (Gold Medal)** |
| AIME 2025 | 92.4 (98.6 with TIR) |
| AIME 2026 | 90.9 (95.0 with TIR) |
| HMMT Feb25 | 94.6 |
| LiveCodeBench v6 | 87.2 (88.4 with TIR) |
| ICPC World Finals 2025 | 10/12 (Gold Medal) |
| ArenaHard v2 | 83.5 |
| SWE Verified (OpenHands) | 50.2 |
| MMLU-Pro | 79.8 |
| GPQA-Diamond | 76.1 |

## Requirements

```
torch>=2.1
transformers>=4.40
bitsandbytes>=0.43  # for 4-bit quantization
peft>=0.10          # optional, for LoRA/QLoRA
```

No `mamba-ssm`. No `causal-conv1d`. No CUDA kernel compilation.

## Technical Notes

### Async Loading Fix

Transformers >=5.0 uses a concurrent-futures weight loading pipeline that materializes bf16 tensors on GPU before bitsandbytes can quantize them. With 6,000+ Linear layers across 128 experts × 23 MoE layers, this causes OOM on GPUs with less than ~65 GB VRAM. openNemo Cascade automatically sets `HF_DEACTIVATE_ASYNC_LOAD=1` at import time to force sequential loading, which lets bnb quantize each tensor in-place. This is transparent to users — just call `from_pretrained` normally.

If you want async loading back (e.g., on a large-memory server), set `HF_DEACTIVATE_ASYNC_LOAD=0` before importing the model.

### Weight Compatibility

All weight names match NVIDIA's original checkpoint exactly. This repo contains the same weights — the only difference is the modeling code. You can also point this modeling code at NVIDIA's original repo:

```python
model = AutoModelForCausalLM.from_pretrained(
    "nvidia/Nemotron-Cascade-2-30B-A3B",  # NVIDIA's weights
    quantization_config=bnb_config,
    trust_remote_code=False,  # use our local code instead
    # ... provide local model code path
)
```

## Files

| File | Description |
|---|---|
| `modeling_nemotron_h.py` | Full model implementation — Mamba2, Attention, MoE, MLP blocks |
| `configuration_nemotron_h.py` | Model config with MoE parameters |
| `__init__.py` | Module exports |

## Citation

```bibtex
@article{Nemotron_Cascade_2,
  title={Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation},
  author={Yang, Zhuolin and Liu, Zihan and Chen, Yang and Dai, Wenliang and Wang, Boxin and Lin, Sheng-Chieh and Lee, Chankyu and Chen, Yangyi and Jiang, Dongfu and He, Jiafan and Pi, Renjie and Lam, Grace and Lee, Nayeon and Bukharin, Alexander and Shoeybi, Mohammad and Catanzaro, Bryan and Ping, Wei},
  year={2026}
}
```

## License

NVIDIA Open Model License — same as the base model.

## Acknowledgments

- Original model: [Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B) by NVIDIA 
- openNemo port: [Empero AI](https://empero.org)
---
license: odc-by
language:
- en
configs:
- config_name: MOPD
  data_files:
  - split: train
    path: MOPD/train.jsonl
- config_name: multi-domain-RL
  data_files:
  - split: train
    path: multi-domain-RL/train.jsonl
- config_name: IF-RL
  data_files:
  - split: train
    path: IF-RL/train.jsonl
- config_name: SWE-RL
  data_files:
  - split: train
    path: SWE-RL/train.jsonl
---

## Dataset Description:

The Nemotron-Cascade-2-RL dataset is a curated reinforcement learning (RL) dataset blend used to train Nemotron-Cascade-2-30B-A3B model. It includes instruction-following RL, multi-domain RL, on-policy distillation, and software engineering RL (SWE-RL) data.

This dataset is ready for commercial use.

The dataset contains the following subset:

### IF-RL

Contains 45,879 training samples for instruction-following RL. Our curation process mainly resolves formatting inconsistencies within the keyword arguments for certain instruction types (e.g., `count_increment_word`). 

This sub dataset is from [nvidia/Nemotron-RL-instruction_following](https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following).

### Multi-domain-RL

Contains 18,147 training samples spanning multi-domain tasks, including Multi-choice Question Answering (MCQA), workplace assistant, and structured output for instruction following.

The datasets are from:
- [nvidia/Nemotron-RL-knowledge-mcqa](https://huggingface.co/datasets/nvidia/Nemotron-RL-knowledge-mcqa) (55%)
- [nvidia/Nemotron-RL-agent-workplace_assistant](https://huggingface.co/datasets/nvidia/Nemotron-RL-agent-workplace_assistant) (30%)
- [nvidia/Nemotron-RL-instruction_following-structured_outputs](https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following-structured_outputs) (15%)

### Multi-domain on-policy distillation

Contains **6171** data instances, covering data sources from AceReason-Math, instruction following, structured outputs, stem MCQA, and Workplace assistant.

| Data Source            | Count |
|------------------------|------:|
| AceReason-Math         | 1853  |
| Instruction Following  | 1854  |
| Workplace              | 610   |
| STEM                   | 927   |
| Structured Outputs     | 927   | 

The datasets are from:
- [nvidia/AceReason-Math](https://huggingface.co/datasets/nvidia/AceReason-Math)
- [nvidia/Nemotron-RL-instruction_following](https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following)
- [nvidia/Nemotron-RL-knowledge-mcqa](https://huggingface.co/datasets/nvidia/Nemotron-RL-knowledge-mcqa) 
- [nvidia/Nemotron-RL-agent-workplace_assistant](https://huggingface.co/datasets/nvidia/Nemotron-RL-agent-workplace_assistant)
- [nvidia/Nemotron-RL-instruction_following-structured_outputs](https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following-structured_outputs)

### SWE-RL

Contains 3,612 training samples for software engineering RL workflows.

The datasets are from:
- [SWE-Gym/SWE-Gym](https://huggingface.co/datasets/SWE-Gym/SWE-Gym) (20%)
- [R2E-Gym/R2E-Gym-Subset](https://huggingface.co/datasets/R2E-Gym/R2E-Gym-Subset) (80%)


## Dataset Creation Date:

Created on: Mar 19, 2026

## License/Terms of Use:

The dataset is governed by the [Open Data Commons Attribution License (ODC-By) v1.0](https://opendatacommons.org/licenses/by/1-0/).

## Intended Usage:

This dataset is intended to be used by the community to train and evaluate RL and instruction-following models. The data may be freely used to train and evaluate.

## Dataset Characterization

**Data Collection Method**  
Hybrid: Human, Synthetic, Automated

**Labeling Method**  
Hybrid: Human, Synthetic, Automated

## Dataset Format

Modality: Text  
Format: JSONL  
Structure: Text + Metadata  

**Columns:**

- Core columns (all subsets):
  - `responses_create_params`: Input payload and generation settings
  - `agent_ref`: Agent metadata used for generation/evaluation
  - `dataset`: Dataset/source identifier (available in subsets that include dataset-level tags)
- Common additional columns (subset-dependent):
  - `prompt`, `instruction_id_list`, `kwargs`, `id`, `category`, `environment_name`, `ground_truth`
  - `pass_rate`, `pass_rate_total`, `pass_rate_passed`
  - `metadata`, `model`, `temperature` (under `responses_create_params`)

## Dataset Quantification


| Subset          | Samples |
| --------------- | ------- |
| MOPD            | 6,171   |
| multi-domain-RL | 18,147  |
| IF-RL           | 45,879  |
| SWE-RL          | 3,612   |
| Total           | 73,809  |


Total Disk Size: ~2.73 GB

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal developer teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

---
license: other
license_name: nvidia-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
configs:
- config_name: math
  data_files:
  - split: train
    path: math/*
- config_name: science
  data_files:
  - split: train
    path: science/*
- config_name: chat
  data_files:
  - split: train
    path: chat/*
- config_name: instruction_following
  data_files:
  - split: train
    path: instruction_following/*
- config_name: safety
  data_files:
  - split: train
    path: safety/*
- config_name: conversational_agent
  data_files:
  - split: train
    path: conversational_agent/*
- config_name: swe
  data_files:
  - split: train
    path: swe/*
- config_name: terminal_agent
  data_files:
  - split: train
    path: terminal_agent/*
---


# Nemotron-Cascade-2-SFT-Data
We release the SFT data used for training [Nemotron-Cascade-2](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B).


## Data sources

#### Math
Our non-proof math prompts are sourced from [Nemotron-Cascade-1-SFT](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-SFT-Stage-2) and [Nemotron-Math-v2](https://huggingface.co/datasets/nvidia/Nemotron-Math-v2), with responses generated by DeepSeek-V3.2, DeepSeek-V3.2-Speciale, and GPT-OSS-120B. For mathematical proofs, prompts are taken from [Nemotron-Math-Proofs-v1](https://huggingface.co/datasets/nvidia/Nemotron-Math-Proofs-v1) and generated using DeepSeek-V3.2-Speciale.


#### Science
We collect science prompts from [Nemotron-Cascade-1-SFT](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-SFT-Stage-2) and [Nemotron-Science-v1](https://huggingface.co/datasets/nvidia/Nemotron-Science-v1), coving physics, chemistry, and biology. Responses are generated by GPT-OSS-120B.


#### General Chat
We source general chat samples from [Nemotron-Cascade-1-SFT](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-SFT-Stage-2) and [Nemotron-Instruction-Following-Chat-v1](https://huggingface.co/datasets/nvidia/Nemotron-Instruction-Following-Chat-v1).


#### Instruction Following
The samples are sourced from [Nemotron-Cascade-1-SFT](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-SFT-Stage-2) and [Nemotron-Instruction-Following-Chat-v1](https://huggingface.co/datasets/nvidia/Nemotron-Instruction-Following-Chat-v1).


#### Safety
The samples are sourced from [Nemotron-SFT-Safety-v1](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Safety-v1).


#### Conversational Agent
The prompts are sourced from [Nemotron-Agentic-v1](https://huggingface.co/datasets/nvidia/Nemotron-Agentic-v1) and [Nemotron-RL-Agentic-Conversational-Tool-Use-Pivot-v1](https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Conversational-Tool-Use-Pivot-v1), with responses generated by Qwen3-235B-A22B-Thinking-2507, Qwen3-32B, Qwen3-235B-A22B-Instruct-2507, and GPT-OSS-120B.


#### Software Engineering Agent
We collect agentless samples from [Nemotron-Cascade-1-SFT-SWE](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-1-SFT-SWE), covering buggy code localization, code repair, and test case generation. Agentic samples are drawn from [SWE-Gym](https://huggingface.co/datasets/SWE-Gym/SWE-Gym), [SWE-rebench](https://huggingface.co/datasets/nebius/SWE-rebench), and [R2E-Gym-Subset](https://huggingface.co/datasets/R2E-Gym/R2E-Gym-Subset).


#### Terminal Agent
The samples are sourced from [Nemotron-Terminal-Corpus](https://huggingface.co/datasets/nvidia/Nemotron-Terminal-Corpus).


## Training

We pack all SFT samples into sequences of up to 256K tokens and train the model in a single stage. Empirically, we find that the SFT model reaches optimal performance after approximately 1.5 epochs.

| Hyperparameters |  |
| :--- | :---: |
| Global Batch Size | 64 |
| Packed Sequence Length | 256K |
| Max Learning Rate | 5e-5 |
| Min Learning Rate | 5e-6 |
| Learning Rate Warmup Steps | 200 |
| Scheduler | cosine |
| Max Steps | 40,000 |
| Optimizer | AdamW  |
| Optimizer Config | beta_1=0.9<br>beta_2=0.98 |
| Weight Decay | 0.1 |
| # of training steps | 33,000 |


## Statistics

| Domain | # Samples |
| :--- | :---: |
| Math | 5,226,364 |
| Science | 2,717,163 |
| General Chat | 13,972,873 |
| Instruction Following | 820,263 |
| Safety | 3,570 |
| Conversational Agent | 822,213 |
| Software Engineering Agent | 439,610 |
| Terminal Agent | 822,213 |


## Release Date
Mar 19, 2026


## License
Your use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).


## Citation
```
@article{Nemotron_Cascade_2,
  title={Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation},
  author={Yang, Zhuolin and Liu, Zihan and Chen, Yang and Dai, Wenliang and Wang, Boxin and Lin, Sheng-Chieh and Lee, Chankyu and Chen, Yangyi and Jiang, Dongfu and He, Jiafan and Pi, Renjie and Lam, Grace and Lee, Nayeon and Bukharin, Alexander and Shoeybi, Mohammad and Catanzaro, Bryan and Ping, Wei},
  year={2026}
}
```

# Workflow Card: Use Case 4 — Nemotron-Cascade-2 General-Purpose Reasoning Fine-Tuning

---

## 1. Workflow

- **name**: opennemo_cascade2_finetuning
- **description**: End-to-end ML workflow that fine-tunes NVIDIA's Nemotron-Cascade-2-30B-A3B (a 30B hybrid MoE/SSM/Attention model) using QLoRA on a blend of SFT and RL datasets to produce openNemo-Cascade-2-30B-A3B — a pure-PyTorch, consumer-GPU-compatible variant that eliminates external CUDA kernel dependencies (mamba-ssm, causal-conv1d), enabling 4-bit quantisation and QLoRA fine-tuning for downstream tasks including reasoning, instruction following, and software engineering.

---

## 2. Summary

- **execution_id**: opennemo_cascade2_finetuning_v0
- **version**: 0
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: Completed
- **location**: ~
- **user**: ~
- **entrypoint.repository**: https://huggingface.co/empero-ai/openNemo-Cascade-2-30B-A3B
- **entrypoint.branch**: ~
- **entrypoint.short_sha**: ~

---

## 3. Infrastructure

- **host_os**: ~
- **compute_hardware**: Consumer GPU with ≥17 GB VRAM (4-bit NF4 quantisation); exact hardware not specified
- **runtime_environment**: ~
- **resource_manager**: ~
- **primary_software**: Python, PyTorch ≥2.1, Hugging Face Transformers ≥4.40, bitsandbytes ≥0.43, PEFT ≥0.10
- **environment_snapshot**: ~

---

## 4. Overview

### 4.1 Run Summary

- **total_activities**: 3
- **status_counts**: finished: 3
- **arguments**: QLoRA rank: 64, LoRA alpha: 32, LoRA dropout: 0.05, target modules: q_proj / k_proj / v_proj / o_proj / up_proj / down_proj, quantisation: 4-bit NF4 + double quant (bitsandbytes), HF_DEACTIVATE_ASYNC_LOAD: 1 (set automatically to prevent OOM during weight loading)

**Notable Inputs:**
  - `nvidia/Nemotron-Cascade-2-SFT-Data` — format: packed sequences (JSONL, up to 256K tokens), domains: Math, Science, General Chat, Instruction Following, Safety, Conversational Agent, SWE, Terminal Agent; total: ~24.8M samples, source: https://huggingface.co/datasets/nvidia/Nemotron-Cascade-2-SFT-Data
  - `nvidia/Nemotron-Cascade-2-RL-data` — format: JSONL (4 subsets: IF-RL 45,879 samples, multi-domain-RL 18,147, MOPD 6,171, SWE-RL 3,612); total: 73,809 samples; created: 19 Mar 2026; source: https://huggingface.co/datasets/nvidia/Nemotron-Cascade-2-RL-data
  - `nvidia/Nemotron-Cascade-2-30B-A3B` — format: BF16 model weights (PyTorch), size: 30.87B total parameters / ~3B active per token, source: https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B

**Notable Outputs:**
  - `openNemo-Cascade-2-30B-A3B` — type: pure-PyTorch fine-tuned model (same weights as base, replaced CUDA kernels with native PyTorch ops), VRAM: ~17 GB at 4-bit NF4, location: https://huggingface.co/empero-ai/openNemo-Cascade-2-30B-A3B

**Structure (activity DAG):**
  1. DataPreparation
  2. ModelFinetuning
  3. ModelEvaluation

- **observations**: The primary engineering contribution of this workflow is replacing all external CUDA kernel dependencies (mamba-ssm triton ops, causal-conv1d) with native PyTorch equivalents, enabling bitsandbytes 4-bit quantisation on consumer GPUs. All weight names are preserved from NVIDIA's original checkpoint, so no weight conversion is required. HF_DEACTIVATE_ASYNC_LOAD=1 is set automatically at import time to prevent OOM on GPUs with <65 GB VRAM during loading of the 6,000+ Linear layers across 128 experts × 23 MoE layers.

### 4.2 Resource Usage

- **cpu**: ~
- **memory**: ~
- **gpu**: ~17 GB VRAM under 4-bit NF4 + double quantisation; ~19 GB with QLoRA (r=64); ~65 GB at full BF16 precision
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
    - `nvidia/Nemotron-Cascade-2-SFT-Data` — multi-domain SFT blend covering Math (~5.2M samples), Science (~2.7M), General Chat (~14M), Instruction Following (~820k), Safety (~3.6k), Conversational Agent (~822k), SWE (~440k), Terminal Agent (~822k); responses generated by DeepSeek-V3.2, GPT-OSS-120B, Qwen3-235B-A22B, and others
    - `nvidia/Nemotron-Cascade-2-RL-data` — curated RL blend of IF-RL (45,879 samples), multi-domain-RL (18,147), MOPD on-policy distillation (6,171), and SWE-RL (3,612); total 73,809 samples; format: JSONL with responses_create_params, agent_ref, and dataset fields; created 19 Mar 2026; license: ODC-By v1.0
  - **outputs**:
    - Prepared SFT sequences packed to 256K tokens and RL training splits, ready for fine-tuning ingestion

#### Activity: `ModelFinetuning`

- **name**: ModelFinetuning
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `nvidia/Nemotron-Cascade-2-30B-A3B` — 52-layer hybrid model (23 Mamba2 SSM blocks, 23 MoE blocks with 128 routed experts / top-6, 6 GQA attention blocks); 30.87B total parameters, ~3B active per token; hidden size 2,688; max context 262,144 tokens; vocabulary 131,072; license: NVIDIA Open Model License
    - Prepared SFT and RL datasets from DataPreparation activity
    - Custom pure-PyTorch modeling code replacing mamba-ssm and causal-conv1d kernel dependencies
  - **outputs**:
    - `openNemo-Cascade-2-30B-A3B` — fine-tuned model with identical weight names to NVIDIA original; CUDA-kernel-free implementation enabling 4-bit NF4 quantisation (~17 GB VRAM) and QLoRA (r=64, ~19 GB VRAM); includes `.model` property alias for PEFT/LoRA compatibility

#### Activity: `ModelEvaluation`

- **name**: ModelEvaluation
- **task_count**: 1
- **started_at**: ~
- **ended_at**: ~
- **duration**: ~
- **status**: success: 1
  - **hosts**: ~
  - **inputs**:
    - `openNemo-Cascade-2-30B-A3B` — fine-tuned model under 4-bit quantisation
    - Standard public benchmarks (IMO 2025, IOI 2025, AIME 2025/2026, HMMT Feb25, LiveCodeBench v6, ArenaHard v2, MMLU-Pro, GPQA-Diamond, SWE Verified, ICPC World Finals 2025)
  - **outputs**:
    - `evaluation_report` — IMO 2025: 35 pts (Gold Medal); IOI 2025: 439.3 (Gold Medal); AIME 2025: 92.4 (98.6 with TIR); AIME 2026: 90.9 (95.0 with TIR); HMMT Feb25: 94.6; LiveCodeBench v6: 87.2 (88.4 with TIR); ICPC World Finals 2025: 10/12 (Gold Medal); ArenaHard v2: 83.5; SWE Verified (OpenHands): 50.2; MMLU-Pro: 79.8; GPQA-Diamond: 76.1

---

## 6. Significant Artifacts

### Input Artifacts

**Artifact: `nvidia/Nemotron-Cascade-2-30B-A3B`**
- **name**: nvidia/Nemotron-Cascade-2-30B-A3B
- **description**: NVIDIA's open 30B hybrid MoE/SSM/Attention reasoning model post-trained from Nemotron-3-Nano-30B-A3B-Base. 52-layer architecture combining Mamba2 SSM blocks, MoE blocks (128 routed experts, top-6), and GQA attention blocks. 30.87B total parameters with ~3B active per token. Supports 262,144-token context. Operates in thinking and instruct modes. Achieves gold medal on IMO 2025 and IOI 2025. License: NVIDIA Open Model License.
- **reference**: https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B

**Artifact: `nvidia/Nemotron-Cascade-2-SFT-Data`**
- **name**: nvidia/Nemotron-Cascade-2-SFT-Data
- **description**: Multi-domain SFT dataset used to train Nemotron-Cascade-2. Covers Math, Science, General Chat, Instruction Following, Safety, Conversational Agent, SWE, and Terminal Agent domains. Sequences packed to 256K tokens. Responses generated by DeepSeek-V3.2, GPT-OSS-120B, Qwen3-235B-A22B-Thinking-2507, and others. License: NVIDIA Open Model License.
- **reference**: https://huggingface.co/datasets/nvidia/Nemotron-Cascade-2-SFT-Data

**Artifact: `nvidia/Nemotron-Cascade-2-RL-data`**
- **name**: nvidia/Nemotron-Cascade-2-RL-data
- **description**: Curated RL training blend of 73,809 samples across four subsets: IF-RL (instruction following, 45,879 samples), multi-domain-RL (MCQA / workplace / structured output, 18,147 samples), MOPD on-policy distillation (6,171 samples), and SWE-RL (software engineering, 3,612 samples). Format: JSONL. Created 19 Mar 2026. License: ODC-By v1.0.
- **reference**: https://huggingface.co/datasets/nvidia/Nemotron-Cascade-2-RL-data

### Output Artifacts

**Artifact: `openNemo-Cascade-2-30B-A3B`**
- **name**: openNemo-Cascade-2-30B-A3B
- **description**: Pure-PyTorch port of Nemotron-Cascade-2-30B-A3B by Empero AI. Replaces all external CUDA kernel dependencies (mamba-ssm triton ops, causal-conv1d) with native PyTorch equivalents, enabling bitsandbytes 4-bit NF4 quantisation (~17 GB VRAM) and QLoRA fine-tuning (r=64, ~19 GB VRAM) on consumer GPUs. Weight names are identical to NVIDIA's original checkpoint. Includes thinking and instruct modes. License: NVIDIA Open Model License.
- **reference**: https://huggingface.co/empero-ai/openNemo-Cascade-2-30B-A3B
