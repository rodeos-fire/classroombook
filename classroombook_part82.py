# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: ClassroomBook
def end_to_end_demo():
    from classroombook import Room, TimeSlot, Teacher, Booking, ConflictChecker

    rooms = [Room("A101", 40), Room("B202", 30)]
    teachers = [Teacher("Ms. Ada"), Teacher("Mr. Ben")]

    checker = ConflictChecker(rooms, teachers)

    checker.add(Booking("Ms. Ada", "A101", "09:00", "10:00"))
    checker.add(Booking("Mr. Ben", "A101", "09:30", "10:30"))

    result = checker.check()
    print("Conflict found:", result.conflict)
    print("Conflicting booking:", result.conflict.booking)
    print("Conflicting room:", result.conflict.room)

    checker.add(Booking("Ms. Ada", "B202", "11:00", "12:00"))
    print("No conflict:", checker.check().conflict is None)

    checker.add(Booking("Mr. Ben", "B202", "11:30", "12:30"))
    print("Conflict found:", checker.check().conflict)

    checker.add(Booking("Ms. Ada", "B202", "13:00", "14:00"))
    print("No conflict:", checker.check().conflict is None)

    print("Total bookings:", checker.count())
