# === Stage 85: Add final readiness report summarizing features and known limits ===
# Project: ClassroomBook
def generate_readiness_report(book):
    rooms = book.get_rooms()
    teachers = book.get_teachers()
    slots = book.get_timeslots()
    bookings = book.get_bookings()

    print("=== ClassroomBook Readiness Report ===")
    print(f"Rooms:        {len(rooms)}")
    print(f"Teachers:     {len(teachers)}")
    print(f"Timeslots:    {len(slots)}")
    print(f"Bookings:     {len(bookings)}")
    print()

    print("Features:")
    print("  - Room management")
    print("  - Teacher management")
    print("  - Timeslot scheduling")
    print("  - Booking creation")
    print("  - Conflict detection")
    print()

    print("Known limits:")
    print("  - No database persistence")
    print("  - No authentication")
    print("  - No user interface")
    print("  - No concurrency control")
    print("  - No notification system")
    print()

    conflicts = book.detect_conflicts()
    if conflicts:
        print(f"WARNING: {len(conflicts)} conflict(s) detected:")
        for c in conflicts:
            print(f"  - {c}")
    else:
        print("No conflicts detected.")
    print("=== End Report ===")
