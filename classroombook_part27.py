# === Stage 27: Add monthly summary calculations ===
# Project: ClassroomBook
def monthly_summary(rooms, bookings):
    """Return a dict: {room_name: {month: count}} for each room's bookings."""
    from collections import defaultdict
    summary = defaultdict(lambda: defaultdict(int))
    for room, bks in rooms.items():
        for bk in bks:
            key = (bk['room'], bk['start']['month'])
            summary[key[0]][key[1]] += 1
    return dict(summary)
