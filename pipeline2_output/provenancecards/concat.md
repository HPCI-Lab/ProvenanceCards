# Workflow Card: redi


---


## 1. Workflow

- **name**: run_pipeline_GR0_0
- **description**: ML workflow run identified as 'redi', consisting of 6 sub-activities.

## 2. Summary

- **execution_id**: run_pipeline_GR0_0
- **version**: 0
- **started_at**: 2026-05-06T14:16:57.403597 (ISO 8601)
- **ended_at**: 2026-05-06T14:17:05.531345 (ISO 8601)
- **duration**: 8.13s
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
- **environment_snapshot**: pipeline2_output/jsons/redi_yprov/artifacts_GR0/requirements.txt

## 4. Overview


### 4.1 Run Summary

- **total_activities**: 6
- **status_counts**: finished: 1, unknown: 6
- **exec command**: python /workspace/run_pipeline_0/artifacts/src/pipeline2/03_run_inferences.py
- **arguments**: ~

**Notable Inputs:**
  - `requirements.txt` — format: file, size: 34 bytes, source: requirements.txt
  - `prov_save_path/run_pipeline_0/artifacts_GR0/./requirements.txt` — format: file, size: 34 bytes, source: prov_save_path/run_pipeline_0/artifacts_GR0/./requirements.txt
  - `src/pipeline2/ai_ready_dataset.py` — format: file, size: 1894 bytes, source: src/pipeline2/ai_ready_dataset.py
  - `prov_save_path/run_pipeline_0/artifacts_GR0/src/src/pipeline2/ai_ready_dataset.py` — format: file, size: 1894 bytes, source: prov_save_path/run_pipeline_0/artifacts_GR0/src/src/pipeline2/ai_ready_dataset.py

**Notable Outputs:**
  - `tmp/train.npz` — type: file, size: 33948134 bytes, location: tmp/train.npz
  - `prov_save_path/run_pipeline_0/artifacts_GR0/tmp/train.npz` — type: file, size: 33948134 bytes, location: prov_save_path/run_pipeline_0/artifacts_GR0/tmp/train.npz
  - `tmp/val.npz` — type: file, size: 3917483 bytes, location: tmp/val.npz
  - `prov_save_path/run_pipeline_0/artifacts_GR0/tmp/val.npz` — type: file, size: 3917483 bytes, location: prov_save_path/run_pipeline_0/artifacts_GR0/tmp/val.npz
  - `tmp/test.npz` — type: file, size: 5219970 bytes, location: tmp/test.npz
  - `prov_save_path/run_pipeline_0/artifacts_GR0/tmp/test.npz` — type: file, size: 5219970 bytes, location: prov_save_path/run_pipeline_0/artifacts_GR0/tmp/test.npz

**Structure (activity DAG):**
  1. OutputGeneration
  2. InputFilesValidation
  3. DomainInference
  4. PipelineCreation
  5. PipelineExecution
  6. PipelineFinalize
- **observations**: ~

### 4.2 Resource Usage

- **cpu**: avg utilization: 21.22%
- **memory**: total: 971.75 GB, avg utilization: 30.37%
- **gpu**: avg memory: ~ MB, avg temp: 0.0 °C
- **disk**: total: 3.80 TB, avg utilization: 4.2%
- **network**: ~

## 5. Activities


#### Activity: `OutputGeneration`

- **name**: OutputGeneration
- **task_count**: 1
- **started_at**: 2026-05-06T14:17:05.418000 (ISO 8601)
- **ended_at**: 2026-05-06T14:17:05.418000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - gpu_temperature_OutputGeneration: avg=0.00, min=0.00, max=0.00
      - memory_usage_OutputGeneration: avg=51.00, min=51.00, max=51.00
      - cpu_usage_OutputGeneration: avg=33.30, min=33.30, max=33.30
  - **inputs**:
    - `era5_subset/run_pipeline_GR0_0`
    - `Original_requirements.txt/run_pipeline_GR0_0`
    - `requirements.txt/run_pipeline_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/OutputGeneration` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/cpu_usage_OutputGeneration_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/OutputGeneration` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/memory_usage_OutputGeneration_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/OutputGeneration` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/disk_usage_OutputGeneration_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/OutputGeneration` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_power_OutputGeneration_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/OutputGeneration` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_usage_OutputGeneration_apple_gpu_GR0.csv

#### Activity: `InputFilesValidation`

- **name**: InputFilesValidation
- **task_count**: 1
- **started_at**: 2026-05-06T14:16:58.421000 (ISO 8601)
- **ended_at**: 2026-05-06T14:16:58.421000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - gpu_memory_usage_InputFilesValidation: avg=11.07, min=11.07, max=11.07
      - memory_usage_InputFilesValidation: avg=49.80, min=49.80, max=49.80
      - gpu_temperature_InputFilesValidation: avg=0.00, min=0.00, max=0.00
  - **inputs**:
    - `era5_subset/run_pipeline_GR0_0`
    - `Original_requirements.txt/run_pipeline_GR0_0`
    - `requirements.txt/run_pipeline_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/InputFilesValidation` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/cpu_usage_InputFilesValidation_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/InputFilesValidation` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/memory_usage_InputFilesValidation_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/InputFilesValidation` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/disk_usage_InputFilesValidation_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/InputFilesValidation` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_power_InputFilesValidation_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/InputFilesValidation` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_usage_InputFilesValidation_apple_gpu_GR0.csv

#### Activity: `DomainInference`

- **name**: DomainInference
- **task_count**: 1
- **started_at**: 2026-05-06T14:16:58.427000 (ISO 8601)
- **ended_at**: 2026-05-06T14:16:58.427000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - gpu_usage_DomainInference: avg=0.00, min=0.00, max=0.00
      - gpu_memory_power_DomainInference: avg=0.00, min=0.00, max=0.00
      - gpu_temperature_DomainInference: avg=0.00, min=0.00, max=0.00
  - **inputs**:
    - `era5_subset/run_pipeline_GR0_0`
    - `Original_requirements.txt/run_pipeline_GR0_0`
    - `requirements.txt/run_pipeline_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/DomainInference` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/cpu_usage_DomainInference_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/DomainInference` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/memory_usage_DomainInference_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/DomainInference` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/disk_usage_DomainInference_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/DomainInference` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_power_DomainInference_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/DomainInference` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_usage_DomainInference_apple_gpu_GR0.csv

#### Activity: `PipelineCreation`

- **name**: PipelineCreation
- **task_count**: 1
- **started_at**: 2026-05-06T14:16:58.438000 (ISO 8601)
- **ended_at**: 2026-05-06T14:16:58.438000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - gpu_power_usage_PipelineCreation: avg=0.00, min=0.00, max=0.00
      - gpu_memory_usage_PipelineCreation: avg=11.07, min=11.07, max=11.07
      - gpu_usage_PipelineCreation: avg=0.00, min=0.00, max=0.00
  - **inputs**:
    - `era5_subset/run_pipeline_GR0_0`
    - `Original_requirements.txt/run_pipeline_GR0_0`
    - `requirements.txt/run_pipeline_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/PipelineCreation` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/cpu_usage_PipelineCreation_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/PipelineCreation` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/memory_usage_PipelineCreation_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/PipelineCreation` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/disk_usage_PipelineCreation_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/PipelineCreation` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_power_PipelineCreation_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/PipelineCreation` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_usage_PipelineCreation_apple_gpu_GR0.csv

#### Activity: `PipelineExecution`

- **name**: PipelineExecution
- **task_count**: 1
- **started_at**: 2026-05-06T14:17:05.401000 (ISO 8601)
- **ended_at**: 2026-05-06T14:17:05.401000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - cpu_usage_PipelineExecution: avg=18.40, min=18.40, max=18.40
      - gpu_memory_usage_PipelineExecution: avg=9.37, min=9.37, max=9.37
      - disk_usage_PipelineExecution: avg=4.20, min=4.20, max=4.20
  - **inputs**:
    - `era5_subset/run_pipeline_GR0_0`
    - `Original_requirements.txt/run_pipeline_GR0_0`
    - `requirements.txt/run_pipeline_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/PipelineExecution` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/cpu_usage_PipelineExecution_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/PipelineExecution` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/memory_usage_PipelineExecution_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/PipelineExecution` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/disk_usage_PipelineExecution_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/PipelineExecution` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_power_PipelineExecution_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/PipelineExecution` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_usage_PipelineExecution_apple_gpu_GR0.csv

#### Activity: `PipelineFinalize`

- **name**: PipelineFinalize
- **task_count**: 1
- **started_at**: 2026-05-06T14:17:05.403000 (ISO 8601)
- **ended_at**: 2026-05-06T14:17:05.403000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - gpu_usage_PipelineFinalize: avg=0.00, min=0.00, max=0.00
      - gpu_memory_usage_PipelineFinalize: avg=9.37, min=9.37, max=9.37
      - gpu_power_usage_PipelineFinalize: avg=0.00, min=0.00, max=0.00
  - **inputs**:
    - `era5_subset/run_pipeline_GR0_0`
    - `Original_requirements.txt/run_pipeline_GR0_0`
    - `requirements.txt/run_pipeline_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/PipelineFinalize` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/cpu_usage_PipelineFinalize_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/PipelineFinalize` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/memory_usage_PipelineFinalize_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/PipelineFinalize` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/disk_usage_PipelineFinalize_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/PipelineFinalize` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_power_PipelineFinalize_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/PipelineFinalize` — provml:Metric, path: prov_save_path/run_pipeline_0/metrics_GR0/gpu_memory_usage_PipelineFinalize_apple_gpu_GR0.csv

## 6. Significant Artifacts


### Input Artifacts


**Artifact: `requirements.txt`**
- **name**: requirements.txt
- **description**: Input file of size 34 bytes used by the workflow.
- **reference**: requirements.txt

**Artifact: `prov_save_path/run_pipeline_0/artifacts_GR0/./requirements.txt`**
- **name**: prov_save_path/run_pipeline_0/artifacts_GR0/./requirements.txt
- **description**: Input file of size 34 bytes used by the workflow.
- **reference**: prov_save_path/run_pipeline_0/artifacts_GR0/./requirements.txt

**Artifact: `src/pipeline2/ai_ready_dataset.py`**
- **name**: src/pipeline2/ai_ready_dataset.py
- **description**: Input file of size 1894 bytes used by the workflow.
- **reference**: src/pipeline2/ai_ready_dataset.py

**Artifact: `prov_save_path/run_pipeline_0/artifacts_GR0/src/src/pipeline2/ai_ready_dataset.py`**
- **name**: prov_save_path/run_pipeline_0/artifacts_GR0/src/src/pipeline2/ai_ready_dataset.py
- **description**: Input file of size 1894 bytes used by the workflow.
- **reference**: prov_save_path/run_pipeline_0/artifacts_GR0/src/src/pipeline2/ai_ready_dataset.py

### Output Artifacts


**Artifact: `tmp/train.npz`**
- **name**: tmp/train.npz
- **description**: Output artifact of type 'file', size 33948134 bytes.
- **reference**: tmp/train.npz

**Artifact: `prov_save_path/run_pipeline_0/artifacts_GR0/tmp/train.npz`**
- **name**: prov_save_path/run_pipeline_0/artifacts_GR0/tmp/train.npz
- **description**: Output artifact of type 'file', size 33948134 bytes.
- **reference**: prov_save_path/run_pipeline_0/artifacts_GR0/tmp/train.npz

**Artifact: `tmp/val.npz`**
- **name**: tmp/val.npz
- **description**: Output artifact of type 'file', size 3917483 bytes.
- **reference**: tmp/val.npz

**Artifact: `prov_save_path/run_pipeline_0/artifacts_GR0/tmp/val.npz`**
- **name**: prov_save_path/run_pipeline_0/artifacts_GR0/tmp/val.npz
- **description**: Output artifact of type 'file', size 3917483 bytes.
- **reference**: prov_save_path/run_pipeline_0/artifacts_GR0/tmp/val.npz

**Artifact: `tmp/test.npz`**
- **name**: tmp/test.npz
- **description**: Output artifact of type 'file', size 5219970 bytes.
- **reference**: tmp/test.npz

**Artifact: `prov_save_path/run_pipeline_0/artifacts_GR0/tmp/test.npz`**
- **name**: prov_save_path/run_pipeline_0/artifacts_GR0/tmp/test.npz
- **description**: Output artifact of type 'file', size 5219970 bytes.
- **reference**: prov_save_path/run_pipeline_0/artifacts_GR0/tmp/test.npz


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

# Workflow Card: inference


---


## 1. Workflow

- **name**: inferences_GR0_0
- **description**: ML workflow run identified as 'inference', consisting of 1 sub-activity.

## 2. Summary

- **execution_id**: inferences_GR0_0
- **version**: 0
- **started_at**: 2026-05-06T14:17:55.596249 (ISO 8601)
- **ended_at**: 2026-05-06T14:17:57.204104 (ISO 8601)
- **duration**: 1.61s
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
- **environment_snapshot**: pipeline2_output/jsons/inference_yprov/artifacts_GR0/requirements.txt

## 4. Overview


### 4.1 Run Summary

- **total_activities**: 1
- **status_counts**: finished: 1, unknown: 1
- **exec command**: python /workspace/inferences_0/artifacts/src/pipeline2/03_run_inferences.py
- **arguments**: ~

**Notable Inputs:**
  - `dlesym_finetuned.pt` — format: file, size: 1965 bytes, source: dlesym_finetuned.pt
  - `prov/inferences_0/artifacts_GR0/dlesym_finetuned/dlesym_finetuned.pt` — format: file, size: 1965 bytes, source: prov/inferences_0/artifacts_GR0/dlesym_finetuned/dlesym_finetuned.pt
  - `input_tensor_0.pt` — format: file, size: 8390234 bytes, source: input_tensor_0.pt
  - `requirements.txt` — format: file, size: 34 bytes, source: requirements.txt
  - `prov/inferences_0/artifacts_GR0/./requirements.txt` — format: file, size: 34 bytes, source: prov/inferences_0/artifacts_GR0/./requirements.txt
  - `src/pipeline2/inferences.py` — format: file, size: 4104 bytes, source: src/pipeline2/inferences.py
  - `prov/inferences_0/artifacts_GR0/src/src/pipeline2/inferences.py` — format: file, size: 4104 bytes, source: prov/inferences_0/artifacts_GR0/src/src/pipeline2/inferences.py

**Notable Outputs:**
  - `dlesym.pt` — type: Model, size: 1885 bytes, location: dlesym.pt
  - `prov/inferences_0/artifacts_GR0/dlesym/dlesym.pt` — type: Model, size: 1885 bytes, location: prov/inferences_0/artifacts_GR0/dlesym/dlesym.pt
  - `output.nc` — type: file, size: 1500 bytes, location: output.nc

**Structure (activity DAG):**
  1. inference
- **observations**: ~

### 4.2 Resource Usage

- **cpu**: avg utilization: 23.5%
- **memory**: total: 1.39 TB, avg utilization: 44.48%
- **gpu**: avg memory: ~ MB, avg temp: 0.0 °C
- **disk**: total: 3.80 TB, avg utilization: 4.2%
- **network**: ~

## 5. Activities


#### Activity: `inference`

- **name**: inference
- **task_count**: 1
- **started_at**: 2026-05-06T14:17:57.131000 (ISO 8601)
- **ended_at**: 2026-05-06T14:17:57.131000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - gpu_usage_inference: avg=54.00, min=54.00, max=54.00
      - gpu_memory_usage_inference: avg=33.86, min=33.86, max=33.86
      - gpu_temperature_inference: avg=0.00, min=0.00, max=0.00
  - **inputs**:
    - `Original_dlesym_finetuned.pt/inference`
    - `dlesym_finetuned.pt/inference`
    - `era5_redi/inferences_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/inference` — provml:Metric, path: prov/inferences_0/metrics_GR0/cpu_usage_inference_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/inference` — provml:Metric, path: prov/inferences_0/metrics_GR0/memory_usage_inference_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/inference` — provml:Metric, path: prov/inferences_0/metrics_GR0/disk_usage_inference_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/inference` — provml:Metric, path: prov/inferences_0/metrics_GR0/gpu_memory_power_inference_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/inference` — provml:Metric, path: prov/inferences_0/metrics_GR0/gpu_memory_usage_inference_apple_gpu_GR0.csv

## 6. Significant Artifacts


### Input Artifacts


**Artifact: `dlesym_finetuned.pt`**
- **name**: dlesym_finetuned.pt
- **description**: Input file of size 1965 bytes used by the workflow.
- **reference**: dlesym_finetuned.pt

**Artifact: `prov/inferences_0/artifacts_GR0/dlesym_finetuned/dlesym_finetuned.pt`**
- **name**: prov/inferences_0/artifacts_GR0/dlesym_finetuned/dlesym_finetuned.pt
- **description**: Input file of size 1965 bytes used by the workflow.
- **reference**: prov/inferences_0/artifacts_GR0/dlesym_finetuned/dlesym_finetuned.pt

**Artifact: `input_tensor_0.pt`**
- **name**: input_tensor_0.pt
- **description**: Input file of size 8390234 bytes used by the workflow.
- **reference**: input_tensor_0.pt

**Artifact: `requirements.txt`**
- **name**: requirements.txt
- **description**: Input file of size 34 bytes used by the workflow.
- **reference**: requirements.txt

**Artifact: `prov/inferences_0/artifacts_GR0/./requirements.txt`**
- **name**: prov/inferences_0/artifacts_GR0/./requirements.txt
- **description**: Input file of size 34 bytes used by the workflow.
- **reference**: prov/inferences_0/artifacts_GR0/./requirements.txt

**Artifact: `src/pipeline2/inferences.py`**
- **name**: src/pipeline2/inferences.py
- **description**: Input file of size 4104 bytes used by the workflow.
- **reference**: src/pipeline2/inferences.py

**Artifact: `prov/inferences_0/artifacts_GR0/src/src/pipeline2/inferences.py`**
- **name**: prov/inferences_0/artifacts_GR0/src/src/pipeline2/inferences.py
- **description**: Input file of size 4104 bytes used by the workflow.
- **reference**: prov/inferences_0/artifacts_GR0/src/src/pipeline2/inferences.py

### Output Artifacts


**Artifact: `dlesym.pt`**
- **name**: dlesym.pt
- **description**: Output artifact of type 'Model', size 1885 bytes.
- **reference**: dlesym.pt

**Artifact: `prov/inferences_0/artifacts_GR0/dlesym/dlesym.pt`**
- **name**: prov/inferences_0/artifacts_GR0/dlesym/dlesym.pt
- **description**: Output artifact of type 'Model', size 1885 bytes.
- **reference**: prov/inferences_0/artifacts_GR0/dlesym/dlesym.pt

**Artifact: `output.nc`**
- **name**: output.nc
- **description**: Output artifact of type 'file', size 1500 bytes.
- **reference**: output.nc

# Workflow Card: analysis


---


## 1. Workflow

- **name**: analysis_GR0_0
- **description**: ML workflow run identified as 'analysis', consisting of 2 sub-activities.

## 2. Summary

- **execution_id**: analysis_GR0_0
- **version**: 0
- **started_at**: 2026-05-06T14:17:59.701598 (ISO 8601)
- **ended_at**: 2026-05-06T14:18:07.202656 (ISO 8601)
- **duration**: 7.50s
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
- **environment_snapshot**: pipeline2_output/jsons/analysis_yprov/artifacts_GR0/requirements.txt

## 4. Overview


### 4.1 Run Summary

- **total_activities**: 2
- **status_counts**: finished: 1, unknown: 2
- **exec command**: python /workspace/analysis_0/artifacts/src/pipeline2/04_analysis.py
- **arguments**: ~

**Notable Inputs:**
  - `input_tensor.pt` — format: file, size: 1612 bytes, source: input_tensor.pt
  - `requirements.txt` — format: file, size: 34 bytes, source: requirements.txt
  - `prov/analysis_0/artifacts_GR0/./requirements.txt` — format: file, size: 34 bytes, source: prov/analysis_0/artifacts_GR0/./requirements.txt
  - `src/pipeline2/analysis.py` — format: file, size: 5048 bytes, source: src/pipeline2/analysis.py
  - `prov/analysis_0/artifacts_GR0/src/src/pipeline2/analysis.py` — format: file, size: 5048 bytes, source: prov/analysis_0/artifacts_GR0/src/src/pipeline2/analysis.py

**Notable Outputs:**
  - `results.csv` — type: file, size: 1500 bytes, location: results.csv

**Structure (activity DAG):**
  1. elaboration
  2. analysis
- **observations**: ~

### 4.2 Resource Usage

- **cpu**: avg utilization: 22.05%
- **memory**: total: 1.07 TB, avg utilization: 34.38%
- **gpu**: avg memory: ~ MB, avg temp: 0.0 °C
- **disk**: total: 3.80 TB, avg utilization: 4.2%
- **network**: ~

## 5. Activities


#### Activity: `elaboration`

- **name**: elaboration
- **task_count**: 1
- **started_at**: 2026-05-06T14:18:06.548000 (ISO 8601)
- **ended_at**: 2026-05-06T14:18:06.548000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - memory_usage_elaboration: avg=51.60, min=51.60, max=51.60
      - gpu_memory_usage_elaboration: avg=14.15, min=14.15, max=14.15
      - gpu_temperature_elaboration: avg=0.00, min=0.00, max=0.00
  - **inputs**:
    - `input_tensor_0/analysis_GR0_0`
    - `input_tensor_1/analysis_GR0_0`
    - `input_tensor_2/analysis_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/elaboration` — provml:Metric, path: prov/analysis_0/metrics_GR0/cpu_usage_elaboration_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/elaboration` — provml:Metric, path: prov/analysis_0/metrics_GR0/memory_usage_elaboration_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/elaboration` — provml:Metric, path: prov/analysis_0/metrics_GR0/disk_usage_elaboration_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/elaboration` — provml:Metric, path: prov/analysis_0/metrics_GR0/gpu_memory_power_elaboration_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/elaboration` — provml:Metric, path: prov/analysis_0/metrics_GR0/gpu_memory_usage_elaboration_apple_gpu_GR0.csv

#### Activity: `analysis`

- **name**: analysis
- **task_count**: 1
- **started_at**: 2026-05-06T14:18:07.119000 (ISO 8601)
- **ended_at**: 2026-05-06T14:18:07.119000 (ISO 8601)
- **duration**: 0:00:00
- **status**: success: 1
  - **hosts**:
    - host: `~`, tasks: 1
      - gpu_memory_usage_analysis: avg=20.06, min=20.06, max=20.06
      - gpu_usage_analysis: avg=15.00, min=15.00, max=15.00
      - memory_usage_analysis: avg=51.70, min=51.70, max=51.70
  - **inputs**:
    - `input_tensor_0/analysis_GR0_0`
    - `input_tensor_1/analysis_GR0_0`
    - `input_tensor_2/analysis_GR0_0`
  - **outputs**:
    - `apple_gpu/cpu_usage/analysis` — provml:Metric, path: prov/analysis_0/metrics_GR0/cpu_usage_analysis_apple_gpu_GR0.csv
    - `apple_gpu/memory_usage/analysis` — provml:Metric, path: prov/analysis_0/metrics_GR0/memory_usage_analysis_apple_gpu_GR0.csv
    - `apple_gpu/disk_usage/analysis` — provml:Metric, path: prov/analysis_0/metrics_GR0/disk_usage_analysis_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_power/analysis` — provml:Metric, path: prov/analysis_0/metrics_GR0/gpu_memory_power_analysis_apple_gpu_GR0.csv
    - `apple_gpu/gpu_memory_usage/analysis` — provml:Metric, path: prov/analysis_0/metrics_GR0/gpu_memory_usage_analysis_apple_gpu_GR0.csv

## 6. Significant Artifacts


### Input Artifacts


**Artifact: `input_tensor.pt`**
- **name**: input_tensor.pt
- **description**: Input file of size 1612 bytes used by the workflow.
- **reference**: input_tensor.pt

**Artifact: `requirements.txt`**
- **name**: requirements.txt
- **description**: Input file of size 34 bytes used by the workflow.
- **reference**: requirements.txt

**Artifact: `prov/analysis_0/artifacts_GR0/./requirements.txt`**
- **name**: prov/analysis_0/artifacts_GR0/./requirements.txt
- **description**: Input file of size 34 bytes used by the workflow.
- **reference**: prov/analysis_0/artifacts_GR0/./requirements.txt

**Artifact: `src/pipeline2/analysis.py`**
- **name**: src/pipeline2/analysis.py
- **description**: Input file of size 5048 bytes used by the workflow.
- **reference**: src/pipeline2/analysis.py

**Artifact: `prov/analysis_0/artifacts_GR0/src/src/pipeline2/analysis.py`**
- **name**: prov/analysis_0/artifacts_GR0/src/src/pipeline2/analysis.py
- **description**: Input file of size 5048 bytes used by the workflow.
- **reference**: prov/analysis_0/artifacts_GR0/src/src/pipeline2/analysis.py

### Output Artifacts


**Artifact: `results.csv`**
- **name**: results.csv
- **description**: Output artifact of type 'file', size 1500 bytes.
- **reference**: results.csv
