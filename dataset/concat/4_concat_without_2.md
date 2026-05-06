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

---
library_name: transformers
license: other
license_name: nvidia-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
pipeline_tag: text-generation
language:
- en
tags:
- nvidia
- nemotron-cascade-2
- reasoning
- general-purpose
- SFT
- RL
---

# Nemotron-Cascade-2-30B-A3B

<p align="center">

[![Technical Report](https://img.shields.io/badge/2603.19220-Technical_Report-blue)](https://arxiv.org/abs/2603.19220)
[![SFT Dataset](https://img.shields.io/badge/🤗-SFT_Datset-blue)](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-2-SFT-Data)
[![RL Dataset](https://img.shields.io/badge/🤗-RL_Datset-blue)](https://huggingface.co/datasets/nvidia/Nemotron-Cascade-2-RL-data)
[![Models](https://img.shields.io/badge/🤗-Models-blue)](https://huggingface.co/collections/nvidia/nemotron-cascade-2)
</p>

<img src="fig/nemotron-cascade-2-results.png" alt="main_fig" style="width: 1000px; max-width: 100%;" />


## Introduction
We're excited to introduce [Nemotron-Cascade-2-30B-A3B](https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B), an open 30B MoE model with 3B activated parameters that delivers strong reasoning and agentic capabilities. It is post-trained from the [Nemotron-3-Nano-30B-A3B-Base](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16). Nemotron-Cascade-2-30B-A3B achieves ***gold medal*** performance in both the 2025 International Mathematical Olympiad (IMO) and the International Olympiad in Informatics (IOI). It operates in both **thinking** and **instruct** (non-thinking) modes.


## Benchmark Results

<table style="width: 100%; border-collapse: collapse; font-family: sans-serif;">
  <thead>
    <tr style="color: #76B900; text-align: center;">
      <th style="padding: 8px; color: #76B900; text-align: left;">Benchmark</th>
      <th style="padding: 8px; color: #76B900; text-align: center">Nemotron-3-Nano-30B-A3B</th>
      <th style="padding: 8px; color: #76B900; text-align: center">Nemotron-3-Super-120B-A12B</th>
      <th style="padding: 8px; color: #76B900; text-align: center">Qwen3.5-35B-A3B</th>
      <th style="padding: 8px; color: #76B900; text-align: center">Nemotron-Cascade-2-30B-A3B</th>
    </tr>
  </thead>
  <tbody style="text-align: center;">
    <tr style="text-align: left; font-weight: bold;">
      <td colspan="5" style="padding: 8px; color: #76B900">Math</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">IMO 2025</td>
      <td>-</td><td>-</td><td>-</td><td>🏅 <b>35 pts</b></td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">IMO AnswerBench</td>
      <td>70.4‡</td><td>77.2‡</td><td>74.8‡</td><td>79.3</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">IMO ProofBench</td>
      <td>-</td><td>-</td><td>-</td><td>72.9</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">AIME 2025</td>
      <td>89.1</td><td>90.2</td><td>91.9‡</td><td>92.4 (98.6)†</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">AIME 2026</td>
      <td>89.9‡</td><td>89.8‡</td><td>91.1‡</td><td>90.9 (95.0)†</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">HMMT Feb25</td>
      <td>84.6‡</td><td>93.7</td><td>89.0</td><td>94.6</td>
    </tr>
    <tr style="text-align: left; font-weight: bold;">
      <td colspan="5" style="padding: 8px; color: #76B900">Code Reasoning</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">IOI 2025</td>
      <td>-</td><td>-</td><td>348.6‡</td><td>🏅 <b>439.3</b></td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">ICPC World Finals 2025</td>
      <td>-</td><td>-</td><td>-</td><td>🏅 <b>10/12</b></td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">LiveCodeBench v6 (2408-2505)</td>
      <td>68.3</td><td>78.7</td><td>74.6</td><td>87.2 (88.4)†</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">LiveCodeBenchPro 25Q2 (Easy)</td>
      <td>54.5‡</td><td>81.7‡</td><td>81.1‡</td><td>87.0 (89.3)†</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">LiveCodeBenchPro 25Q2 (Med)</td>
      <td>3.50‡</td><td>23.2‡</td><td>17.8‡</td><td>27.6 (36.8)†</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">SciCode</td>
      <td>33.3</td><td>42.1</td><td>38.0</td><td>36.4</td>
    </tr>
    <tr style="text-align: left; font-weight: bold;">
      <td colspan="5" style="padding: 8px; color: #76B900">Knowledge & STEM</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">MMLU-Redux</td>
      <td>-</td><td>-</td><td>93.3</td><td>86.3</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">MMLU-Pro</td>
      <td>78.3</td><td>83.7</td><td>85.3</td><td>79.8</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">GPQA-Diamond</td>
      <td>73.0</td><td>79.2</td><td>84.2</td><td>76.1</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">HLE (no tool)</td>
      <td>10.6</td><td>18.3</td><td>22.4</td><td>17.7</td>
    </tr>
    <tr style="text-align: left; font-weight: bold;">
      <td colspan="5" style="padding: 8px; color: #76B900">Alignment & Instruction Following</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">ArenaHard v2 (Avg.)</td>
      <td>67.7</td><td>-</td><td>65.4‡</td><td>83.5</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">&nbsp;&nbsp;– Hard Prompt</td>
      <td>72.1</td><td>73.9</td><td>64.5‡</td><td>88.2</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">&nbsp;&nbsp;– Creative Writing</td>
      <td>63.2</td><td>-</td><td>66.3‡</td><td>78.7</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">IFBench (prompt)</td>
      <td>71.5</td><td>72.6</td><td>70.2</td><td>82.9</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">Scale AI Multi-Challenge</td>
      <td>38.5</td><td>55.2</td><td>60.0</td><td>45.3</td>
    </tr>
    <tr style="text-align: left; font-weight: bold;">
      <td colspan="5" style="padding: 8px; color: #76B900">Long Context & Context Learning</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">AA-LCR</td>
      <td>35.9</td><td>58.3</td><td>58.5</td><td>39.1</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">LongBench v2</td>
      <td>39.6</td><td>-</td><td>59.0</td><td>40.3</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">NIAH@1M (RULER Subset)</td>
      <td>94.8</td><td>98.3</td><td>94.3‡</td><td>99.0</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">CL-Bench</td>
      <td>12.0‡</td><td>-</td><td>15.5‡</td><td>12.2</td>
    </tr>
    <tr style="text-align: left; font-weight: bold;">
      <td colspan="5" style="padding: 8px; color: #76B900">Agentic</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">BFCL v4</td>
      <td>53.8</td><td>-</td><td>67.3</td><td>52.9</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">𝜏²-Bench</td>
      <td>49.0</td><td>61.2</td><td>81.2</td><td>58.9</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">Terminal Bench 2.0</td>
      <td>8.5</td><td>31.0</td><td>40.5</td><td>21.1</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">SWE Verified (OpenHands)</td>
      <td>38.8</td><td>60.5</td><td>69.2</td><td>50.2</td>
    </tr>
    <tr style="text-align: left; font-weight: bold;">
      <td colspan="5" style="padding: 8px; color: #76B900">Multilingual</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">MMLU-ProX</td>
      <td>59.5</td><td>79.4</td><td>81.0</td><td>72.5</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 4px 8px;">WMT24++ (en -> xx)</td>
      <td>86.2</td><td>86.7</td><td>87.6‡</td><td>84.1</td>
    </tr>
  </tbody>
</table>

<p style="margin-top:12px;font-size:11px;opacity:0.7">
* † Numbers in brackets refers to Tool-Integrated Reasoning (TIR) results.<br>
* ‡ For the baseline models, we use official numbers when available, otherwise evaluate them using the recommended settings.<br>
</p>


## Quick Start

- Nemotron-Cascade-2-30B-A3B follows the ChatML template and supports both thinking and instruct (non-thinking) modes. Reasoning content is enclosed within `<think>` and `</think>` tags. To activate the instruct (non-thinking) mode, we prepend `<think></think>` to the beginning of the assistant’s response. 

- Nemotron-Cascade-2-30B-A3B does not currently support OpenCode; it primarily supports OpenHands for agentic coding and SWE tasks.

- To reduce the context length in a multi-turn conversation, when the previous user turn involves thinking mode, only the final summary of the model's output will be added to the conversation history.

- Note that we do not define a separate `tool` role for tool responses; instead, we place them under the `user` role and warp them with `<tool_response>` and `</tool_response>`.

- We recommend setting the sampling parameters to temperature = 1.0 and top_p = 0.95.


### vLLM setup

Requires vLLM version >= 0.17.1. The following will create API endpoints at `http://localhost:8000/v1`:

- **Standard version**: Use the following command to create an API endpoint with a maximum context length of 262,144 tokens.

    ```shell
    vllm serve nvidia/Nemotron-Cascade-2-30B-A3B --port 8000 --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --max-model-len 262144 --reasoning-parser nemotron_v3 --mamba-ssm-cache-dtype float32 --port 8000 --trust_remote_code
    ```

- **Tool Call**: Use the following command to enable tool support.

    ```shell
    vllm serve nvidia/Nemotron-Cascade-2-30B-A3B --port 8000 --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --max-model-len 262144 --reasoning-parser nemotron_v3 --mamba-ssm-cache-dtype float32 --port 8000 --trust_remote_code --enable-auto-tool-choice --tool-call-parser qwen3_coder
    ```


### Chat Template

```python
from transformers import AutoTokenizer

model_name = 'nvidia/Nemotron-Cascade-2-30B-A3B'
tokenizer = AutoTokenizer.from_pretrained(model_name)

'''
single-turn example
'''
messages = [
  {"role": "system", "content": "You are a helpful and harmless assistant.\n\nYou are not allowed to use any tools"},
  {"role": "user", "content": "calculate 1+1?"}
]

# thinking mode
prompt_thinking = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=True)
# prompt_thinking = '<|im_start|>system\nYou are a helpful and harmless assistant.\n\nYou are not allowed to use any tools<|im_end|>\n<|im_start|>user\ncalculate 1+1?<|im_end|>\n<|im_start|>assistant\n<think>\n'

# instruct mode
prompt_instruct = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
# prompt_instruct = '<|im_start|>system\nYou are a helpful and harmless assistant.\n\nYou are not allowed to use any tools<|im_end|>\n<|im_start|>user\ncalculate 1+1?<|im_end|>\n<|im_start|>assistant\n<think></think>'

'''
multi-turn example
'''
messages = [
    {"role": "system", "content": "You are a helpful and harmless assistant.\n\nYou are not allowed to use any tools"},
    {"role": "user", "content": "calculate 1+1?"},
    {"role": "assistant", "content": "<think>THINKING_CONTENT</think>\nTo calculate \\(1 + 1\\):\n\n1. **Identify the operation**: This is a basic addition problem involving two integers.\n2. **Perform the addition**:  \n   \\(1 + 1 = 2\\).\n\n**Result**: \\(\\boxed{2}\\)",},
    {"role": "user", "content": "what about 2+2"}
]

# thinking mode
prompt_thinking = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=True)
# prompt_thinking = '<|im_start|>system\nYou are a helpful and harmless assistant.\n\nYou are not allowed to use any tools<|im_end|>\n<|im_start|>user\ncalculate 1+1?<|im_end|>\n<|im_start|>assistant\n<think></think>\nTo calculate \\(1 + 1\\):\n\n1. **Identify the operation**: This is a basic addition problem involving two integers.\n2. **Perform the addition**:  \n   \\(1 + 1 = 2\\).\n\n**Result**: \\(\\boxed{2}\\)<|im_end|>\n<|im_start|>user\nwhat about 2+2<|im_end|>\n<|im_start|>assistant\n<think>\n'

# instruct mode
prompt_instruct = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
# prompt_instruct = '<|im_start|>system\nYou are a helpful and harmless assistant.\n\nYou are not allowed to use any tools<|im_end|>\n<|im_start|>user\ncalculate 1+1?<|im_end|>\n<|im_start|>assistant\n<think></think>\nTo calculate \\(1 + 1\\):\n\n1. **Identify the operation**: This is a basic addition problem involving two integers.\n2. **Perform the addition**:  \n   \\(1 + 1 = 2\\).\n\n**Result**: \\(\\boxed{2}\\)<|im_end|>\n<|im_start|>user\nwhat about 2+2<|im_end|>\n<|im_start|>assistant\n<think></think>'
```

### Python Tool Use

```python
model_name = 'nvidia/Nemotron-Cascade-2-30B-A3B'
tokenizer = AutoTokenizer.from_pretrained(model_name)

SYSTEM_PROMPT = """# Tools

You have access to the following functions:

<tools>
<function>
<name>stateful_python_code_exec</name>
<description>Call this function to execute Python code in a stateful Jupyter notebook environment. Python will respond with the output of the execution or time out after 120.0 seconds.</description>
<parameters>
<parameter>
<name>code</name>
<type>string</type>
<description>Code to execute</description>
</parameter>
<required>["code"]</required>
</parameters>
</function>
</tools>

If you choose to call a function ONLY reply in the following format with NO suffix:

<tool_call>
<function=example_function_name>
<parameter=example_parameter_1>
value_1
</parameter>
<parameter=example_parameter_2>
This is the value for the second parameter
that can span
multiple lines
</parameter>
</function>
</tool_call>

<IMPORTANT>
Reminder:
- Function calls MUST follow the specified format: an inner <function=...></function> block must be nested within <tool_call></tool_call> XML tags
- Required parameters MUST be specified
- You may provide optional reasoning for your function call in natural language BEFORE the function call, but NOT after
- If there is no function call available, answer the question like normal with your current knowledge and do not tell the user about function calls
</IMPORTANT>"""

messages = [
  {"role": "system", "content": SYSTEM_PROMPT},
  {"role": "user", "content": "Solve the following math problem. Put your answer inside \\boxed{}.\n\nIn a school with 2008 students, each student is a member of certain committees. Each committee has at most 1004 members, and every two students are in at least one common committee. Determine the smallest possible number of committees in the school."}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=True)
print(prompt)
```

### Agentic Usage

```python
model_name = 'nvidia/Nemotron-Cascade-2-30B-A3B'
tokenizer = AutoTokenizer.from_pretrained(model_name)

SYSTEM_PROMPT = """You are a customer service agent that helps the user.  The policy that determines how you should respond to requests from users is described below between the <policy> and </policy> tags.

In each turn you can either:
- Send a message to the user.
- Make a tool call.
You cannot do both at the same time.

<policy>
_NEED_TO_ADD_POLICY_HERE_
</policy>

Try to be helpful and always follow the policy.

# Tools

You have access to the following functions:

<tools>
<function>
<name>_NEED_TO_ADD_FUNCTION_NAME_1_</name>
<description>_FUNCTION_DESCRIPTION_</description>
<parameters>
<parameter>
<name>_NEED_TO_ADD_PARAMETER_NAME_1_</name>
<type>_PARAMETER_TYPE_</type>
<description>_PARAMETER_DESCRIPTION_</description>
<title>_PARAMETER_TITLE_</title>
</parameter>
<parameter>
<name>_NEED_TO_ADD_PARAMETER_NAME_2_</name>
<type>_PARAMETER_TYPE_</type>
<description>_PARAMETER_DESCRIPTION_</description>
<title>_PARAMETER_TITLE_</title>
</parameter>
...... (_MORE_PARAMETERS_TO_ADD_)
<parameters>
</function>
...... (_MORE_FUNCTIONS_TO_ADD_)
</tools>
"""

messages = [
  {"role": "system", "content": SYSTEM_PROMPT},
  {"role": "user", "content": "Hello, I'm calling regarding my upcoming stay at your hotel. My guest ID is G90920 and booking ID is B11246 for a Deluxe room on June 5th. I'm traveling with three 6-month-old triplets and need to request three infant cribs for our room. It's currently 30 hours before check-in—could you please confirm if this is feasible and if there are quiet room options available for families with infants?"}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=True)
print(prompt)
```

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
