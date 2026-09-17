# === Stage 40: Add plain text report export ===
# Project: ClassroomBook
def export_plain_text(rooms, bookings):
    """Export a compact plain-text report of rooms and their bookings."""
    lines = []
    lines.append("=" * 60)
    lines.append("ClassroomBook - Plain Text Report")
    lines.append("=" * 60)
    for room in rooms:
        lines.append(f"\nRoom: {room.name}")
        lines.append("-" * 40)
        if room.bookings:
            for b in room.bookings:
                lines.append(f"  {b.date} | {b.start}-{b.end} | Teacher: {b.teacher} | Status: {b.status}")
        else:
            lines.append("  No bookings scheduled.")
    return "\n".join(lines)
