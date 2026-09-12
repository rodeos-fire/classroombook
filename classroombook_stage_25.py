# === Stage 25: Add daily summary calculations ===
# Project: ClassroomBook
def daily_summary(bookings, rooms, timeslots):
    day = bookings[0].date if bookings else None
    if not day:
        return None
    room_usage = {r: 0 for r in rooms}
    for b in bookings:
        if b.date == day and b.room in room_usage:
            room_usage[b.room] += 1
    return day, room_usage
