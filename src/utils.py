
import json

def _load_jsonl(path: str) -> list[dict]:
    """Load a .jsonl file into a list of dicts, skipping blank lines."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return records

def _flatten_dict(d: dict, prefix: str = "", sep: str = ".") -> dict:
    """Recursively flatten a nested dict into dot-notation keys."""
    out = {}
    for k, v in d.items():
        key = f"{prefix}{sep}{k}" if prefix else k
        if isinstance(v, dict):
            out.update(_flatten_dict(v, key, sep))
        else:
            out[key] = v
    return out

