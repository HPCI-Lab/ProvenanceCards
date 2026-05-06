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
