# === Stage 34: Add support for multiple local user profiles ===
# Project: ClassroomBook
import os
import json

LOCAL_PROFILES_DIR = os.path.join(os.path.dirname(__file__), "profiles")

def get_profiles():
    """Return a list of local user profile dicts from disk."""
    profiles = []
    if not os.path.isdir(LOCAL_PROFILES_DIR):
        os.makedirs(LOCAL_PROFILES_DIR, exist_ok=True)
        return profiles
    for fname in os.listdir(LOCAL_PROFILES_DIR):
        if fname.endswith(".json"):
            path = os.path.join(LOCAL_PROFILES_DIR, fname)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    profiles.append(json.load(f))
            except (json.JSONDecodeError, OSError):
                pass
    return profiles
