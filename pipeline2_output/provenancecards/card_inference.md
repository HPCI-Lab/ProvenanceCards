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
