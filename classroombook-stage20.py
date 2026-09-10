# === Stage 20: Add duplicate detection for newly created records ===
# Project: ClassroomBook
def detect_duplicates(rooms, teachers, timeslots, bookings):
    """Check if any newly created records already exist."""
    seen = set()
    for room in rooms:
        for teacher in teachers:
            for timeslot in timeslots:
                key = (room, teacher, timeslot)
                if key in seen:
                    print(f"Duplicate detected: {key}")
                    return False
                seen.add(key)
    return True
