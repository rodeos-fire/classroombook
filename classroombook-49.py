# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ClassroomBook
import unittest
from classroom_book import ClassroomBook

class TestUpdateDelete(unittest.TestCase):
    def setUp(self):
        self.cb = ClassroomBook()
        self.cb.add_room("Room A")
        self.cb.add_teacher("Alice")
        self.cb.add_timeslot("Mon", "9am")

    def test_update_existing_booking(self):
        self.cb.create_booking("Alice", "Room A", "Mon", "9am", "Lecture")
        self.cb.update_booking("Alice", "Room A", "Mon", "9am", "Seminar")
        self.assertEqual(self.cb.get_booking("Alice", "Room A", "Mon", "9am").type, "Seminar")

    def test_update_nonexistent_booking_returns_false(self):
        result = self.cb.update_booking("Nobody", "Room A", "Mon", "9am", "Lecture")
        self.assertFalse(result)

    def test_delete_existing_booking(self):
        self.cb.create_booking("Alice", "Room A", "Mon", "9am", "Lecture")
        self.assertTrue(self.cb.delete_booking("Alice", "Room A", "Mon", "9am"))
        self.assertIsNone(self.cb.get_booking("Alice", "Room A", "Mon", "9am"))

    def test_delete_nonexistent_booking(self):
        self.assertFalse(self.cb.delete_booking("Nobody", "Room A", "Mon", "9am"))

    def test_update_conflicts_with_self(self):
        self.cb.create_booking("Alice", "Room A", "Mon", "9am", "Lecture")
        with self.assertRaises(ValueError):
            self.cb.update_booking("Alice", "Room A", "Mon", "9am", "Lecture")

    def test_delete_conflicts_with_self(self):
        self.cb.create_booking("Alice", "Room A", "Mon", "9am", "Lecture")
        with self.assertRaises(ValueError):
            self.cb.delete_booking("Alice", "Room A", "Mon", "9am")

    def test_update_preserves_other_bookings(self):
        self.cb.create_booking("Alice", "Room A", "Mon", "9am", "Lecture")
        self.cb.create_booking("Bob", "Room B", "Mon", "9am", "Seminar")
        self.cb.update_booking("Alice", "Room A", "Mon", "9am", "Seminar")
        self.assertEqual(self.cb.get_booking("Bob", "Room B", "Mon", "9am").type, "Seminar")

    def test_delete_preserves_other_bookings(self):
        self.cb.create_booking("Alice", "Room A", "Mon", "9am", "Lecture")
        self.cb.create_booking("Bob", "Room B", "Mon", "9am", "Seminar")
        self.cb.delete_booking("Alice", "Room A", "Mon", "9am")
        self.assertEqual(self.cb.get_booking("Bob", "Room B", "Mon", "9am").type, "Seminar")

if __name__ == "__main__":
    unittest.main()
