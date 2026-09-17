# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ClassroomBook
def load_lines(path):
    """Load a line-based text file into a list of stripped strings."""
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]
