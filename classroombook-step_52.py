# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ClassroomBook
def find_next_available_slot(rooms, timeslots, teachers):
    """Return the earliest (room, slot) pair where the given teacher has no
    existing booking.  If no such slot exists, return None.

    Parameters
    ----------
    rooms : list of Room
        All rooms in the classroom.
    timeslots : list of TimeSlot
        All available time slots.
    teachers : list of Teacher
        Teachers whose bookings must be checked.

    Returns
    -------
    tuple or None
        A (room, timeslot) pair, or None when every room is full for every
        teacher.
    """
    for slot in timeslots:
        for room in rooms:
            for teacher in teachers:
                if room.is_free_for(teacher, slot):
                    return (room, slot)
    return None


def summarize_bookings(rooms, timeslots, teachers):
    """Build a readable summary of every active booking in the classroom.

    The result is a list of strings, each describing one booking in the
    format ``RoomName - TeacherName on Slot``.  Empty slots are omitted.
    """
    lines = []
    for room in rooms:
        for slot in timeslots:
            for teacher in teachers:
                if room.has_booking(teacher, slot):
                    lines.append(
                        f"{room.name} - {teacher.name} on {slot}"
                    )
    return lines


def validate_booking_consistency(rooms, timeslots, teachers):
    """Check that every booking stored in the rooms is still valid.

    A booking is considered invalid if the room no longer has a record
    for the teacher in that slot.  Returns a list of tuples
    ``(room, teacher, slot)`` for every inconsistency found, or an empty
    list when everything is consistent.
    """
    inconsistencies = []
    for room in rooms:
        for teacher in teachers:
            for slot in timeslots:
                if room.has_booking(teacher, slot):
                    if not room.is_free_for(teacher, slot):
                        inconsistencies.append(
                            (room, teacher, slot)
                        )
    return inconsistencies
