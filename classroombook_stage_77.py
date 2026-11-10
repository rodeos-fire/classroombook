# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: ClassroomBook
def find_conflicts(bookings, start, end):
    """Return a list of booking objects that overlap the given timeslot."""
    conflicts = []
    for booking in bookings:
        if booking["start"] < end and booking["end"] > start:
            conflicts.append(booking)
    return conflicts


def is_available(bookings, start, end):
    """Return True if no booking overlaps the proposed timeslot."""
    return len(find_conflicts(bookings, start, end)) == 0


def format_timeslot(start, end):
    """Return a human-readable string like '09:00 - 10:00'."""
    return f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}"


def find_available_slot(rooms, teachers, start, end):
    """Return the first room that is free during the timeslot, else None."""
    for room in rooms:
        if is_available(room["bookings"], start, end):
            return room
    return None


def format_booking(booking):
    """Return a compact summary of a booking record."""
    return (
        f"{booking['title']} | "
        f"{format_timeslot(booking['start'], booking['end'])} | "
        f"{booking.get('room', 'unassigned')} | "
        f"{booking.get('teacher', 'unassigned')}"
    )


def count_conflicts(bookings):
    """Return the total number of conflicting pairs across all bookings."""
    total = 0
    for i in range(len(bookings)):
        for j in range(i + 1, len(bookings)):
            if booking["start"] < booking["end"] and booking["end"] > booking["start"]:
                total += 1
    return total
