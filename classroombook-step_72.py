# === Stage 72: Add Markdown report export ===
# Project: ClassroomBook
def export_markdown(bookings, rooms, teachers):
    lines = ["# ClassroomBook Report", "",
             "## Rooms", ""]
    for r in rooms:
        lines.append(f"- {r['name']} (capacity {r['capacity']})")
    lines.append("")
    lines.append("## Teachers", "")
    for t in teachers:
        lines.append(f"- {t['name']} (id {t['teacher_id']})")
    lines.append("")
    lines.append("## Bookings", "")
    for b in bookings:
        conflict = "CONFLICT" if b.get("conflict") else "ok"
        lines.append(
            f"- {b['room']} @ {b['start']}-{b['end']} by {b['teacher']} ({b['subject']}) [{conflict}]")
    lines.append("")
    return "\n".join(lines)
