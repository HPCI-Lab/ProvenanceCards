
# FlowCept: keys that carry meaningful provenance from the workflow record
FLOWCEPT_WORKFLOW_KEYS = [
    "workflow_id",        # unique workflow run identifier
    "campaign_id",        # groups multiple workflow runs
    "name",               # workflow step name (Inspect, Infer, Propose, …)
    "user",               # OS user who executed the workflow
    "sys_name",           # host OS name
    "flowcept_version",   # FlowCept library version
    "utc_timestamp",      # workflow start timestamp (UTC epoch)
]

# FlowCept: keys from the nested machine_info block
FLOWCEPT_MACHINE_KEYS = [
    "platform.system",      # OS (Darwin, Linux, …)
    "platform.node",        # hostname
    "platform.release",     # OS release string
    "platform.machine",     # hardware architecture (arm64, x86_64, …)
    "platform.processor",   # processor type
    "cpu.brand_raw",        # CPU brand string (e.g. Apple M1 Max)
    "cpu.arch",             # CPU architecture class (ARM_8, …)
    "cpu.count",            # number of logical CPU cores
    "cpu.python_version",   # Python version string
    "memory.virtual.total", # total RAM in bytes
    "disk.total",           # total disk capacity in bytes
    "disk.used",            # disk space in use
]

# FlowCept: keys from each task record
FLOWCEPT_TASK_KEYS = [
    "task_id",        # unique task identifier
    "activity_id",    # logical activity name (e.g. _sample_file)
    "workflow_id",    # back-reference to parent workflow
    "started_at",     # task start timestamp (epoch)
    "status",         # completion status
    "used",           # data inputs consumed by the task
    "generated",      # data outputs produced by the task
]

# FlowCept: process-level keys inside telemetry_at_start.process
FLOWCEPT_PROCESS_KEYS = [
    "process.pid",          # process ID
    "process.executable",   # Python interpreter path
    "process.cmd_line",     # full command line used to launch the job
    "process.num_threads",  # thread count at task start
]

# All FlowCept keys flattened (used as the default checklist for _F.jsonl)
FLOWCEPT_ALL_KEYS = (
    FLOWCEPT_WORKFLOW_KEYS
    + FLOWCEPT_MACHINE_KEYS
    + FLOWCEPT_TASK_KEYS
    + FLOWCEPT_PROCESS_KEYS
)

# yProv4ML: keys from the main activity block
YPROV_ACTIVITY_KEYS = [
    "yprov:experiment_name",  # human-readable experiment label
    "yprov:run_id",           # integer run counter
    "yprov:python_version",   # Python version used during the run
    "yprov:PID",              # process UUID
    "yprov:global_rank",      # distributed rank (0 = master)
    "yprov:provenance_path",  # directory where provenance files are written
    "yprov:artifact_uri",     # URI of the run's artifact directory
    "yprov:experiment_dir",   # root experiment directory
    "prov:startedAtTime",     # ISO-8601 run start time
    "prov:endedAtTime",       # ISO-8601 run end time
]

# yProv4ML: entity keys (dataset-level provenance, stored as prov:value strings)
YPROV_ENTITY_KEYS = [
    "files",            # list of input files (path, name, suffix, size)
    "total_size",       # total input data size in bytes
    "formats",          # list of file extensions present
    "file_count",       # number of input files
    "modality",         # data modality (gridded, tabular, image, unknown, …)
    "likely_domain",    # inferred scientific/application domain
    "has_labels",       # whether labelled targets were detected
    "has_splits",       # whether train/test splits exist
    "sparsity",         # sparsity estimate (if applicable)
    "suggested_format", # recommended storage format (npz, parquet, …)
    "output_format",    # format chosen for the output artefact
    "pipeline_steps",   # ordered list of recommended ML pipeline steps
    "confidence",       # confidence level of the domain inference
    "notes",            # free-text notes / warnings from the discovery run
    "sample_data",      # sample of data structure / first-item keys
]

# yProv4ML: GPU telemetry entity prefixes (apple_gpu/metric/step)
YPROV_GPU_METRIC_KEYS = [
    "apple_gpu/cpu_usage",
    "apple_gpu/memory_usage",
    "apple_gpu/disk_usage",
    "apple_gpu/gpu_memory_power",
    "apple_gpu/gpu_memory_usage",
    "apple_gpu/gpu_usage",
    "apple_gpu/gpu_power_usage",
    "apple_gpu/gpu_temperature",
]

# All yProv keys flattened (used as the default checklist for _Y.json)
YPROV_ALL_KEYS = YPROV_ACTIVITY_KEYS + YPROV_ENTITY_KEYS

# Generic fallback (used when format cannot be detected)
DEFAULT_PROVENANCE_CHECKLIST = list(dict.fromkeys(
    FLOWCEPT_WORKFLOW_KEYS + YPROV_ACTIVITY_KEYS + YPROV_ENTITY_KEYS
))
