# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ClassroomBook
import json

def load_book(filename, strict=False):
    """Load a ClassroomBook from a JSON file.

    Returns the dictionary if it is valid.
    Raises ValueError with a friendly message on any problem.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise ValueError(f"File not found: {filename}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Malformed JSON in {filename}: {e}")

    if not isinstance(data, dict):
        raise ValueError("JSON root must be an object (dictionary).")

    required = {"rooms": list, "timeslots": list, "teachers": list}
    for key, expected in required.items():
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
        if not isinstance(data[key], expected):
            raise ValueError(f"Key '{key}' must be a list, got {type(data[key]).__name__}.")

    if strict:
        extra = set(data.keys()) - set(required)
        if extra:
            raise ValueError(f"Unexpected keys in strict mode: {sorted(extra)}")

    return data
