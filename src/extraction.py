import json

from consts import *
from utils import _load_jsonl, _flatten_dict

def detect_schema(source_path: str) -> str:
    """
    Return 'flowcept', 'yprov', or 'unknown' based on the source file name
    and its content.
    """
    path = source_path.lower()
    if path.endswith("_f.jsonl") or path.endswith("_f.json"):
        return "flowcept"
    if path.endswith("_y.json") or path.endswith("_y.jsonl"):
        return "yprov"
    # Heuristic: peek at content
    try:
        with open(source_path) as f:
            first = f.read(500)
        if "yprov:" in first or "prov:startedAtTime" in first:
            return "yprov"
        if "workflow_id" in first or "campaign_id" in first:
            return "flowcept"
    except Exception:
        pass
    return "unknown"

def checklist_for_schema(schema: str) -> list[str]:
    """Return the appropriate provenance checklist for a detected schema."""
    if schema == "flowcept":
        return FLOWCEPT_ALL_KEYS
    if schema == "yprov":
        return YPROV_ALL_KEYS
    return DEFAULT_PROVENANCE_CHECKLIST


# ---------------------------------------------------------------------------
# FlowCept (_F.jsonl) extraction
# ---------------------------------------------------------------------------

def _extract_flowcept(records: list[dict]) -> dict:
    """
    Extract ground-truth provenance attributes from a FlowCept JSONL record set.
    Pulls from the workflow record (record[0]) and all task records.
    """
    attrs = {}
    workflow = next((r for r in records if r.get("type") == "workflow"), records[0])

    # Top-level workflow fields
    for k in FLOWCEPT_WORKFLOW_KEYS:
        if k in workflow:
            attrs[k] = workflow[k]

    # Nested machine_info — flatten and pull known keys
    machine_flat = {}
    for interceptor_id, minfo in workflow.get("machine_info", {}).items():
        machine_flat.update(_flatten_dict(minfo))
    for k in FLOWCEPT_MACHINE_KEYS:
        leaf = k.split(".")[-1]
        # Try dot-notation first, then leaf key
        val = machine_flat.get(k) or machine_flat.get(leaf)
        if val is not None:
            attrs[f"machine.{k}"] = val

    # Summarise tasks
    tasks = [r for r in records if r.get("type") == "task"]
    attrs["total_tasks"] = len(tasks)
    attrs["activity_ids"] = list({t.get("activity_id") for t in tasks if t.get("activity_id")})

    # Process info from first task
    if tasks:
        t0 = tasks[0]
        proc = t0.get("telemetry_at_start", {}).get("process", {})
        for k in ["pid", "executable", "cmd_line", "num_threads"]:
            if k in proc:
                attrs[f"process.{k}"] = proc[k]
        if "generated" in t0 and t0["generated"]:
            attrs["generated_keys"] = list(t0["generated"].keys())

    return attrs


def _flowcept_to_reference(attrs: dict, source_path: str) -> str:
    """Render FlowCept attributes as a readable reference description."""
    lines = [
        f"Source file: {source_path}",
        f"Schema: FlowCept workflow provenance",
        "",
        "## Workflow Identity",
    ]
    for k in ["workflow_id", "campaign_id", "name", "user", "utc_timestamp", "flowcept_version"]:
        if k in attrs:
            lines.append(f"- {k}: {attrs[k]}")

    lines.append("\n## Execution Environment")
    for k, v in attrs.items():
        if k.startswith("machine."):
            lines.append(f"- {k.replace('machine.', '')}: {v}")

    lines.append("\n## Tasks")
    lines.append(f"- total_tasks: {attrs.get('total_tasks', 'unknown')}")
    lines.append(f"- activity_ids: {attrs.get('activity_ids', [])}")

    lines.append("\n## Process")
    for k, v in attrs.items():
        if k.startswith("process."):
            lines.append(f"- {k.replace('process.', '')}: {v}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# yProv4ML (_Y.json) extraction
# ---------------------------------------------------------------------------

def _parse_entity_value(raw: str):
    """Try to parse a prov:value string as Python literal or return as-is."""
    import ast
    try:
        return ast.literal_eval(raw)
    except Exception:
        return raw


def _extract_yprov(data: dict) -> dict:
    """
    Extract ground-truth provenance attributes from a yProv4ML JSON document.
    """
    attrs = {}

    # Agent
    agents = list(data.get("agent", {}).keys())
    if agents:
        attrs["agent"] = agents[0]

    # Main activity (the run_ entry)
    for act_name, act_val in data.get("activity", {}).items():
        if isinstance(act_val, dict) and "yprov:experiment_name" in act_val:
            attrs["activity_name"] = act_name
            for k in YPROV_ACTIVITY_KEYS:
                if k in act_val:
                    v = act_val[k]
                    # Unwrap {$: val, type: xsd:int} pattern
                    if isinstance(v, dict) and "$" in v:
                        v = v["$"]
                    attrs[k] = v
            break

    # Sub-activities (Inspect, Infer, Propose, Generation, apple_gpu/*)
    sub_activities = {}
    for act_name, act_val in data.get("activity", {}).items():
        if isinstance(act_val, dict) and "prov:startedAtTime" in act_val:
            sub_activities[act_name] = act_val.get("prov:startedAtTime")
    if sub_activities:
        attrs["workflow_steps"] = list(sub_activities.keys())

    # Entities: core dataset provenance
    entities = data.get("entity", {})
    for k in YPROV_ENTITY_KEYS:
        if k in entities:
            raw = entities[k].get("prov:value", "")
            attrs[f"entity.{k}"] = _parse_entity_value(raw) if raw else None

    # GPU telemetry entity summary
    gpu_steps = {k for k in entities if k.startswith("apple_gpu/")}
    if gpu_steps:
        attrs["gpu_telemetry_steps"] = sorted(gpu_steps)

    return attrs


def _yprov_to_reference(attrs: dict, source_path: str) -> str:
    """Render yProv4ML attributes as a readable reference description."""
    lines = [
        f"Source file: {source_path}",
        f"Schema: yProv4ML (W3C PROV-DM)",
        "",
        "## Experiment Identity",
    ]
    for k in ["yprov:experiment_name", "yprov:run_id", "yprov:PID", "yprov:global_rank", "agent"]:
        if k in attrs:
            lines.append(f"- {k}: {attrs[k]}")

    lines.append("\n## Timing")
    for k in ["prov:startedAtTime", "prov:endedAtTime"]:
        if k in attrs:
            lines.append(f"- {k}: {attrs[k]}")

    lines.append("\n## Workflow Steps")
    lines.append(f"- steps: {attrs.get('workflow_steps', [])}")

    lines.append("\n## Dataset Provenance")
    for k, v in attrs.items():
        if k.startswith("entity."):
            label = k.replace("entity.", "")
            display = json.dumps(v) if isinstance(v, (list, dict)) else str(v)
            lines.append(f"- {label}: {display[:200]}")

    lines.append("\n## Environment")
    for k in ["yprov:python_version", "yprov:provenance_path", "yprov:artifact_uri"]:
        if k in attrs:
            lines.append(f"- {k}: {attrs[k]}")

    return "\n".join(lines)


def compute_reference_from_source(file: str) -> str:
    meta        = json.load(open(file))
    source_path = meta["input_file"]
    schema      = detect_schema(source_path)

    if schema == "flowcept":
        records = _load_jsonl(source_path)
        attrs   = _extract_flowcept(records)
        return _flowcept_to_reference(attrs, source_path)

    elif schema == "yprov":
        data  = json.load(open(source_path))
        attrs = _extract_yprov(data)
        return _yprov_to_reference(attrs, source_path)

    else:
        raise Exception("Schema not known")


def compute_ground_truth_attrs_from_source(file: str) -> dict:
    meta        = json.load(open(file))
    source_path = meta["input_file"]
    schema      = detect_schema(source_path)

    if schema == "flowcept":
        records = _load_jsonl(source_path)
        return _extract_flowcept(records)
    elif schema == "yprov":
        data = json.load(open(source_path))
        return _extract_yprov(data)
    else:
        raise Exception("Schema not known")

