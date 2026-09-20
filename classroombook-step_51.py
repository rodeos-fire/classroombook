# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ClassroomBook
import unittest
from classroom_book.models import Room, Timeslot, Teacher
from classroom_book.conflict_checker import ConflictChecker


class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        self.rooms = {
            "Room A": Room("Room A", capacity=30),
            "Room B": Room("Room B", capacity=50),
            "Room C": Room("Room C", capacity=20),
        }
        self.slots = {
            "Mon 9am": Timeslot("Mon 9am", "Monday", 9),
            "Mon 10am": Timeslot("Mon 10am", "Monday", 10),
            "Tue 9am": Timeslot("Tue 9am", "Tuesday", 9),
        }
        self.teachers = {
            "Dr. Smith": Teacher("Dr. Smith", "CS"),
            "Prof. Jones": Teacher("Prof. Jones", "Math"),
            "Ms. Lee": Teacher("Ms. Lee", "Physics"),
        }
        self.checker = ConflictChecker(self.rooms, self.slots, self.teachers)

    def test_search_by_room_name(self):
        result = self.checker.search_rooms("Room A")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Room A")

    def test_search_by_capacity(self):
        result = self.checker.search_rooms(min_capacity=25)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(r.capacity >= 25 for r in result))

    def test_search_by_subject(self):
        result = self.checker.search_teachers(subject="CS")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Dr. Smith")

    def test_search_by_day(self):
        result = self.checker.search_slots(day="Monday")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(s.day == "Monday" for s in result))

    def test_search_by_time_range(self):
        result = self.checker.search_slots(start_hour=10, end_hour=12)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Mon 10am")

    def test_search_rooms_exact_match(self):
        result = self.checker.search_rooms("Room X")
        self.assertEqual(len(result), 0)

    def test_search_teachers_by_department(self):
        result = self.checker.search_teachers(department="Math")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Prof. Jones")


if __name__ == "__main__":
    unittest.main()
