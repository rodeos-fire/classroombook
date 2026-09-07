# === Stage 11: Add JSON export for the current application state ===
# Project: ClassroomBook
def export_state():
    """Export current application state to a JSON file."""
    import json
    with open("state.json", "w") as f:
        json.dump(state, f, indent=2)
