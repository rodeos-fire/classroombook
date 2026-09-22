# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ClassroomBook
def colorize(text, color):
    """Return ANSI-colored text. Falls back to plain text if unsupported."""
    codes = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "bold": "\033[1m",
        "reset": "\033[0m",
    }
    if color not in codes:
        return text
    return f"{codes[color]}{text}{codes['reset']}"
