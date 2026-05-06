# Workflow Card: finetuning


---


## 1. Workflow

- **name**: finetuning_GR0_0
- **description**: ML workflow run identified as 'finetuning', consisting of 3 sub-activities.

## 2. Summary

- **execution_id**: finetuning_GR0_0
- **version**: 0
- **started_at**: 2026-05-06T14:17:07.667730 (ISO 8601)
- **ended_at**: 2026-05-06T14:17:53.457425 (ISO 8601)
- **duration**: 45.79s
- **status**: Completed
- **location**: 0
- **user**: ['gabrielepadovani']
- **entrypoint.repository**: ~
- **entrypoint.branch**: ~
- **entrypoint.short_sha**: ~

## 3. Infrastructure

- **host_os**: Darwin  25.3.0
- **compute_hardware**: arm64, 1 cores
- **runtime_environment**: 0
- **resource_manager**: ~
- **primary_software**: Python 3.13.11
- **environment_snapshot**: pipeline2_output/jsons/finetuning_yprov/artifacts_GR0/requirements.txt

## 4. Overview


### 4.1 Run Summary

- **total_activities**: 3
- **status_counts**: finished: 1, unknown: 3
- **exec command**: python /workspace/finetuning_0/artifacts/src/pipeline2/02_finetune_model.py
- **arguments**: ~

**Notable Inputs:**
  - `dlesym_pretrained.pt` — format: file, size: 1973 bytes, source: dlesym_pretrained.pt
  - `prov/finetuning_0/artifacts_GR0/dlesym_pretrained/dlesym_pretrained.pt` — format: file, size: 1973 bytes, source: prov/finetuning_0/artifacts_GR0/dlesym_pretrained/dlesym_pretrained.pt
  - `requirements.txt` — format: file, size: 34 bytes, source: requirements.txt
  - `prov/finetuning_0/artifacts_GR0/./requirements.txt` — format: file, size: 34 bytes, source: prov/finetuning_0/artifacts_GR0/./requirements.txt
  - `src/pipeline2/finetune_model.py` — format: file, size: 4555 bytes, source: src/pipeline2/finetune_model.py
  - `prov/finetuning_0/artifacts_GR0/src/src/pipeline2/finetune_model.py` — format: file, size: 4555 bytes, source: prov/finetuning_0/artifacts_GR0/src/src/pipeline2/finetune_model.py

**Notable Outputs:**
  - `dlesym.pt` — type: Model, size: 1885 bytes, location: dlesym.pt
  - `prov/finetuning_0/artifacts_GR0/dlesym/dlesym.pt` — type: Model, size: 1885 bytes, location: prov/finetuning_0/artifacts_GR0/dlesym/dlesym.pt

**Structure (activity DAG):**
  1. finetune
  2. preprocess
  3. save
- **observations**: ~

### 4.2 Resource Usage

- **cpu**: avg utilization: 15.63%
- **memory**: total: 1.05 TB, avg utilization: 33.72%
- **gpu**: avg memory: ~ MB, avg temp: 0.0 °C
- **disk**: total: 3.80 TB, avg utilization: 4.2%
- **network**: ~

## 5. Activities


#### Activity: `finetune`

- **name**: finetune
- **task_count**: 1
- **started_at**: 2026-05-06T14:17:53.384000 (ISO 8601)
- **ended_at**: 2026-05-06T14:17:53.384000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - gpu_memory_power_finetune: avg=0.00, min=0.00, max=0.00
      - disk_usage_finetune: avg=4.20, min=4.20, max=4.20
      - gpu_power_usage_finetune: avg=0.00, min=0.00, max=0.00
  - **inputs**:
    - `Original_dlesym_pretrained.pt/finetuning_GR0_0`
    - `dlesym_pretrained.pt/finetuning_GR0_0`
    - `era5_redi/finetuning_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/finetune` — provml:Metric, path: prov/finetuning_0/metrics_GR0/cpu_usage_finetune_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/finetune` — provml:Metric, path: prov/finetuning_0/metrics_GR0/memory_usage_finetune_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/finetune` — provml:Metric, path: prov/finetuning_0/metrics_GR0/disk_usage_finetune_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/finetune` — provml:Metric, path: prov/finetuning_0/metrics_GR0/gpu_memory_power_finetune_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/finetune` — provml:Metric, path: prov/finetuning_0/metrics_GR0/gpu_memory_usage_finetune_apple_gpu_GR0.csv

#### Activity: `preprocess`

- **name**: preprocess
- **task_count**: 1
- **started_at**: 2026-05-06T14:17:08.814000 (ISO 8601)
- **ended_at**: 2026-05-06T14:17:08.814000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - gpu_usage_preprocess: avg=2.00, min=2.00, max=2.00
      - gpu_memory_power_preprocess: avg=0.00, min=0.00, max=0.00
      - disk_usage_preprocess: avg=4.20, min=4.20, max=4.20
  - **inputs**:
    - `Original_dlesym_pretrained.pt/finetuning_GR0_0`
    - `dlesym_pretrained.pt/finetuning_GR0_0`
    - `era5_redi/finetuning_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/preprocess` — provml:Metric, path: prov/finetuning_0/metrics_GR0/cpu_usage_preprocess_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/preprocess` — provml:Metric, path: prov/finetuning_0/metrics_GR0/memory_usage_preprocess_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/preprocess` — provml:Metric, path: prov/finetuning_0/metrics_GR0/disk_usage_preprocess_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/preprocess` — provml:Metric, path: prov/finetuning_0/metrics_GR0/gpu_memory_power_preprocess_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/preprocess` — provml:Metric, path: prov/finetuning_0/metrics_GR0/gpu_memory_usage_preprocess_apple_gpu_GR0.csv

#### Activity: `save`

- **name**: save
- **task_count**: 1
- **started_at**: 2026-05-06T14:17:53.389000 (ISO 8601)
- **ended_at**: 2026-05-06T14:17:53.389000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - disk_usage_save: avg=4.20, min=4.20, max=4.20
      - gpu_temperature_save: avg=0.00, min=0.00, max=0.00
      - gpu_usage_save: avg=0.00, min=0.00, max=0.00
  - **inputs**:
    - `Original_dlesym_pretrained.pt/finetuning_GR0_0`
    - `dlesym_pretrained.pt/finetuning_GR0_0`
    - `era5_redi/finetuning_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/save` — provml:Metric, path: prov/finetuning_0/metrics_GR0/cpu_usage_save_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/save` — provml:Metric, path: prov/finetuning_0/metrics_GR0/memory_usage_save_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/save` — provml:Metric, path: prov/finetuning_0/metrics_GR0/disk_usage_save_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/save` — provml:Metric, path: prov/finetuning_0/metrics_GR0/gpu_memory_power_save_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/save` — provml:Metric, path: prov/finetuning_0/metrics_GR0/gpu_memory_usage_save_apple_gpu_GR0.csv

## 6. Significant Artifacts


### Input Artifacts


**Artifact: `dlesym_pretrained.pt`**
- **name**: dlesym_pretrained.pt
- **description**: Input file of size 1973 bytes used by the workflow.
- **reference**: dlesym_pretrained.pt

**Artifact: `prov/finetuning_0/artifacts_GR0/dlesym_pretrained/dlesym_pretrained.pt`**
- **name**: prov/finetuning_0/artifacts_GR0/dlesym_pretrained/dlesym_pretrained.pt
- **description**: Input file of size 1973 bytes used by the workflow.
- **reference**: prov/finetuning_0/artifacts_GR0/dlesym_pretrained/dlesym_pretrained.pt

**Artifact: `requirements.txt`**
- **name**: requirements.txt
- **description**: Input file of size 34 bytes used by the workflow.
- **reference**: requirements.txt

**Artifact: `prov/finetuning_0/artifacts_GR0/./requirements.txt`**
- **name**: prov/finetuning_0/artifacts_GR0/./requirements.txt
- **description**: Input file of size 34 bytes used by the workflow.
- **reference**: prov/finetuning_0/artifacts_GR0/./requirements.txt

**Artifact: `src/pipeline2/finetune_model.py`**
- **name**: src/pipeline2/finetune_model.py
- **description**: Input file of size 4555 bytes used by the workflow.
- **reference**: src/pipeline2/finetune_model.py

**Artifact: `prov/finetuning_0/artifacts_GR0/src/src/pipeline2/finetune_model.py`**
- **name**: prov/finetuning_0/artifacts_GR0/src/src/pipeline2/finetune_model.py
- **description**: Input file of size 4555 bytes used by the workflow.
- **reference**: prov/finetuning_0/artifacts_GR0/src/src/pipeline2/finetune_model.py

### Output Artifacts


**Artifact: `dlesym.pt`**
- **name**: dlesym.pt
- **description**: Output artifact of type 'Model', size 1885 bytes.
- **reference**: dlesym.pt

**Artifact: `prov/finetuning_0/artifacts_GR0/dlesym/dlesym.pt`**
- **name**: prov/finetuning_0/artifacts_GR0/dlesym/dlesym.pt
- **description**: Output artifact of type 'Model', size 1885 bytes.
- **reference**: prov/finetuning_0/artifacts_GR0/dlesym/dlesym.pt
