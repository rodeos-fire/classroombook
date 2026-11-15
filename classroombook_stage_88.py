# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: ClassroomBook
def safe_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def safe_bool(value, default=False):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ("true", "yes", "1", "y")
    return default


def fill_defaults(data, schema):
    result = {}
    for key, spec in schema.items():
        if key not in data or data[key] in (None, "", [], {}):
            if "default" in spec:
                result[key] = spec["default"]
            elif "factory" in spec:
                result[key] = spec["factory"]()
            elif spec.get("type") == "int":
                result[key] = safe_int(data.get(key), spec.get("default", 0))
            elif spec.get("type") == "bool":
                result[key] = safe_bool(data.get(key), spec.get("default", False))
            elif spec.get("type") == "list":
                result[key] = []
            elif spec.get("type") == "dict":
                result[key] = {}
            else:
                result[key] = None
        else:
            result[key] = data[key]
    return result


ROOM_SCHEMA = {
    "name": {"type": "str", "default": "Room"},
    "capacity": {"type": "int", "default": 10},
    "location": {"type": "str", "default": ""},
    "equipment": {"type": "list", "default": []},
}


def safe_room(data):
    return fill_defaults(data, ROOM_SCHEMA)


def safe_timeslot(data):
    return fill_defaults(data, {
        "start": {"type": "str", "default": ""},
        "end": {"type": "str", "default": ""},
        "date": {"type": "str", "default": ""},
    })


def safe_teacher(data):
    return fill_defaults(data, {
        "name": {"type": "str", "default": "Teacher"},
        "email": {"type": "str", "default": ""},
        "available": {"type": "bool", "default": True},
    })


def safe_booking(data):
    return fill_defaults(data, {
        "room": {"type": "str", "default": ""},
        "teacher": {"type": "str", "default": ""},
        "start": {"type": "str", "default": ""},
        "end": {"type": "str", "default": ""},
        "date": {"type": "str", "default": ""},
        "confirmed": {"type": "bool", "default": False},
    })
