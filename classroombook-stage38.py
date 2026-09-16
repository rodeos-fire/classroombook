# === Stage 38: Add data integrity checks for broken references ===
# Project: ClassroomBook
def validate_references(book):
    """Check that all book entries reference valid rooms, timeslots, and teachers."""
    errors = []
    for entry in book.entries:
        if entry.room_id not in book.rooms:
            errors.append(f"{entry.room_id} not in rooms")
        if entry.timeslot_id not in book.timeslots:
            errors.append(f"{entry.timeslot_id} not in timeslots")
        if entry.teacher_id not in book.teachers:
            errors.append(f"{entry.teacher_id} not in teachers")
    return errors
