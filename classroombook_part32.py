# === Stage 32: Add pagination helpers for long console output ===
# Project: ClassroomBook
def paginate(lines, chunk=40):
    """Yield lines in chunks of `chunk` for console display."""
    for i in range(0, len(lines), chunk):
        yield lines[i:i+chunk]

def truncate_output(text, max_len=2000):
    """Truncate long text with a marker for compact console output."""
    if len(text) <= max_len:
        return text
    return text[:max_len] + "\n\n... (truncated)"
