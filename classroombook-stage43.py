# === Stage 43: Add CSV import for the primary record type ===
# Project: ClassroomBook
import csv
from pathlib import Path

def load_bookings(file_path):
    """Read bookings from a CSV file and return a list of Booking objects."""
    bookings = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            bookings.append(Booking(
                id=row["id"],
                teacher_id=row["teacher_id"],
                room_id=row["room_id"],
                start_time=row["start_time"],
                end_time=row["end_time"],
            ))
    return bookings
