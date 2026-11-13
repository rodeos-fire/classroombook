# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: ClassroomBook
def _compact_timeslots(rooms, timeslots):
    merged = {}
    for room in rooms:
        merged[room.id] = {ts for ts in timeslots.get(room.id, set())}
    return merged


def _find_conflicts(bookings, rooms, timeslots):
    for i in range(len(bookings)):
        for j in range(i + 1, len(bookings)):
            b1, b2 = bookings[i], bookings[j]
            if b1.room_id == b2.room_id and b1.time_slot == b2.time_slot:
                return [b1, b2]
    return []


def _validate_booking(booking, rooms, timeslots):
    if booking.room_id not in rooms:
        raise ValueError("Unknown room")
    if booking.time_slot not in timeslots.get(booking.room_id, set()):
        raise ValueError("Time slot not available for room")
    if booking.teacher_id not in [t.id for t in rooms[booking.room_id].teachers]:
        raise ValueError("Teacher not assigned to room")
