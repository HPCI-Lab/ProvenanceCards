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
