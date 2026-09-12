# === Stage 26: Add weekly summary calculations ===
# Project: ClassroomBook
def weekly_summary(books):
    """Return a dict of {day: {room: count}} for the given week."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    summary = {day: {} for day in days}
    for booking in books:
        day = booking["day"]
        if day not in days:
            continue
        room = booking["room"]
        summary[day][room] = summary[day].get(room, 0) + 1
    return summary
