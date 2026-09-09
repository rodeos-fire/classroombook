# === Stage 14: Add file load support with fallback demo data ===
# Project: ClassroomBook
def load_classroom_data():
    """Load classroom data from a JSON file, with fallback demo data."""
    import json
    import os

    data_file = "classroom_data.json"
    if os.path.exists(data_file):
        try:
            with open(data_file, "r") as f:
                return json.load(f)
        except Exception:
            pass

    return {
        "rooms": [
            {"id": 1, "name": "Room 101", "capacity": 30, "equipment": ["projector", "whiteboard"]},
            {"id": 2, "name": "Room 202", "capacity": 20, "equipment": ["whiteboard"]},
            {"id": 3, "name": "Lab A", "capacity": 15, "equipment": ["computers", "projector"]},
        ],
        "teachers": [
            {"id": 1, "name": "Dr. Smith", "subject": "Math"},
            {"id": 2, "name": "Dr. Johnson", "subject": "Science"},
            {"id": 3, "name": "Ms. Lee", "subject": "English"},
        ],
        "timeslots": [
            {"id": 1, "day": "Monday", "time": "09:00-10:00"},
            {"id": 2, "day": "Monday", "time": "10:00-11:00"},
            {"id": 3, "day": "Monday", "time": "11:00-12:00"},
            {"id": 4, "day": "Tuesday", "time": "09:00-10:00"},
            {"id": 5, "day": "Tuesday", "time": "10:00-11:00"},
        ],
        "bookings": [
            {"id": 1, "room_id": 1, "teacher_id": 1, "timeslot_id": 1, "date": "2024-01-15"},
            {"id": 2, "room_id": 2, "teacher_id": 2, "timeslot_id": 4, "date": "2024-01-16"},
        ],
    }
