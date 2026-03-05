
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

def _load_md(path : str) -> list[dict]: 
    return open(path, "r").readlines()

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


def _parse_md_sections(text: str) -> dict[str, list[str]]:
    """
    Split a markdown document into sections keyed by their ## header title.
    Lines before the first header are stored under the key '__preamble__'.
    Returns {section_title: [raw_lines_without_leading_dash_space]}.
    """
    sections: dict[str, list[str]] = {}
    current = "__preamble__"
    for line in text:
        stripped = line.strip()
        if stripped.startswith("## "):
            current = stripped[3:].strip()
            sections.setdefault(current, [])
        elif stripped.startswith("- ") and current != "__preamble__":
            sections.setdefault(current, []).append(stripped[2:])   # drop "- "
        elif stripped and current == "__preamble__":
            sections.setdefault(current, []).append(stripped)
    return sections

def _parse_kv_line(line: str) -> tuple[str, str] | None:
    """
    Parse a 'key: value' line (already stripped of the leading '- ').
    Returns (key, raw_value_string) or None if no ': ' separator is found.

    Splits on the FIRST ':' followed by a space so that namespace-prefixed
    keys like 'yprov:experiment_name' or 'prov:startedAtTime' are kept
    intact as the key.
    """
    sep = ": "
    idx = line.find(sep)
    if idx == -1:
        return None
    return line[:idx].strip(), line[idx + len(sep):].strip()

def _coerce_value(raw: str):
    """
    Try to recover a Python object from a raw string value.
    Handles:
      - Python repr lists/dicts  e.g. "['a', 'b']"  or "{'k': 1}"
      - JSON fragments            e.g. '["a", "b"]'
      - Plain strings / numbers
    Values truncated at 200 chars (from the reference renderer) are
    returned as strings — we can't safely reconstruct partial objects.
    """
    import ast
    stripped = raw.strip()
    # Looks like a list or dict — try ast first (handles Python repr)
    if stripped and stripped[0] in ("[", "{"):
        try:
            return ast.literal_eval(stripped)
        except Exception:
            pass
        try:
            return json.loads(stripped)
        except Exception:
            pass
        # Partial / truncated — return as-is
        return stripped
    # Plain numbers
    for cast in (int, float):
        try:
            return cast(stripped)
        except ValueError:
            pass
    return stripped

def _kv_lines_to_dict(lines: list[str]) -> dict:
    """Parse a list of 'key: value' strings into a dict, coercing values."""
    result = {}
    for line in lines:
        parsed = _parse_kv_line(line)
        if parsed:
            k, v = parsed
            result[k] = _coerce_value(v)
    return result

