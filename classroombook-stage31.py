# === Stage 31: Add compact table rendering for long lists ===
# Project: ClassroomBook
def render_compact_table(rows: list[dict[str, str]], columns: list[str]) -> str:
    """Render a compact multi-row table as a grid of strings."""
    if not rows:
        return "(empty)"
    widths = [max(len(col) for _, col in zip(rows, columns)) + 2 for _ in columns]
    lines = ["  ".join(col.ljust(w) for col, w in zip(rows[0], widths))]
    for row in rows[1:]:
        lines.append("  ".join(col.ljust(w) for col, w in zip(row, widths)))
    return "\n".join(lines)
