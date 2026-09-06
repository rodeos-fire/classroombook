# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ClassroomBook
def format_room(room):
    return f"[{room.name}] {room.capacity} seats, {room.description}"

def format_timeslot(slot):
    return f"{slot.start} - {slot.end}"

def format_booking(booking):
    conflict = " (CONFLICT)" if booking.is_conflict else ""
    return (f"[{booking.room.name}] {format_timeslot(booking.time_slot)} "
            f"Teacher: {booking.teacher.name}{conflict}")
