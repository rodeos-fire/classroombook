# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ClassroomBook
def validate_required(value, field_name):
    if not value:
        raise ValueError(f"{field_name} is required")
    return value

def validate_identifier(identifier, prefix="ID"):
    if not identifier or not re.match(r'^[a-zA-Z0-9_.-]+$', identifier):
        raise ValueError(f"Invalid {prefix}: {identifier!r}")
    return identifier

def validate_short_text(text, max_len=100):
    if not text or not isinstance(text, str):
        raise ValueError("Text must be a non-empty string")
    if len(text) > max_len:
        raise ValueError(f"Text exceeds {max_len} characters")
    return text.strip()

def validate_email(email):
    if not email or not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
        raise ValueError(f"Invalid email: {email!r}")
    return email.lower()

def validate_positive_int(value, name):
    try:
        val = int(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be an integer")
    if val <= 0:
        raise ValueError(f"{name} must be positive")
    return val
