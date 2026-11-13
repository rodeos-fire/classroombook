# === Stage 83: Add regression tests for the final demo workflow ===
# Project: ClassroomBook
from datetime import datetime, timedelta
from booking import Room, Teacher, Timeslot, Booking, ConflictChecker


def test_demo_workflow_no_conflicts():
    room = Room("A101")
    teacher = Teacher("Ms. Lee")
    checker = ConflictChecker()

    bookings = []
    for i in range(3):
        start = datetime(2025, 1, 6, 9, 0) + timedelta(minutes=30 * i)
        slot = Timeslot(start, timedelta(minutes=45))
        booking = Booking(room, teacher, slot)
        assert checker.add(booking) is True
        bookings.append(booking)

    assert len(checker.conflicts) == 0
    assert len(bookings) == 3


def test_demo_workflow_detects_conflict():
    room = Room("A101")
    teacher = Teacher("Ms. Lee")
    checker = ConflictChecker()

    bookings = []
    for i in range(2):
        start = datetime(2025, 1, 6, 9, 0) + timedelta(minutes=30 * i)
        slot = Timeslot(start, timedelta(minutes=45))
        booking = Booking(room, teacher, slot)
        checker.add(booking)
        bookings.append(booking)

    conflict_start = datetime(2025, 1, 6, 9, 30)
    slot = Timeslot(conflict_start, timedelta(minutes=45))
    booking = Booking(room, teacher, slot)
    assert checker.add(booking) is False
    assert len(checker.conflicts) == 1
