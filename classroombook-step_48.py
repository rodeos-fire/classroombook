# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ClassroomBook
import unittest
from datetime import datetime, timedelta

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.room = {"name": "Lab 1", "capacity": 10}
        self.teacher = {"name": "Dr. Smith", "email": "smith@uni.edu"}
        self.slot = {"start": datetime(2024, 1, 15, 9, 0), "end": datetime(2024, 1, 15, 10, 0)}

    def test_create_booking(self):
        booking = create_booking(self.room, self.teacher, self.slot)
        self.assertIsNotNone(booking)
        self.assertEqual(booking["room"], self.room)
        self.assertEqual(booking["teacher"], self.teacher)
        self.assertEqual(booking["slot"], self.slot)
        self.assertEqual(booking["status"], "confirmed")

    def test_create_booking_no_conflict(self):
        booking1 = create_booking(self.room, self.teacher, self.slot)
        slot2 = {"start": datetime(2024, 1, 15, 10, 0), "end": datetime(2024, 1, 15, 11, 0)}
        booking2 = create_booking(self.room, {"name": "Dr. Jones"}, slot2)
        self.assertEqual(len(booking1), 1)
        self.assertEqual(len(booking2), 1)

    def test_create_booking_with_conflict(self):
        booking1 = create_booking(self.room, self.teacher, self.slot)
        slot2 = {"start": datetime(2024, 1, 15, 9, 0), "end": datetime(2024, 1, 15, 10, 0)}
        booking2 = create_booking(self.room, {"name": "Dr. Jones"}, slot2)
        self.assertEqual(len(booking2), 0)

    def test_validate_booking(self):
        booking = create_booking(self.room, self.teacher, self.slot)
        self.assertTrue(validate_booking(booking))

    def test_validate_invalid_booking(self):
        booking = {"room": self.room, "teacher": self.teacher, "slot": self.slot, "status": "invalid"}
        self.assertFalse(validate_booking(booking))

if __name__ == "__main__":
    unittest.main()
