# === Stage 42: Add CSV export without external dependencies ===
# Project: ClassroomBook
import csv
from datetime import datetime


def export_to_csv(bookings, filename="classroom_bookings.csv", delimiter=","):
    """Export bookings to a CSV file without external dependencies."""
    if not bookings:
        raise ValueError("No bookings to export")

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Room", "Teacher", "Start", "End", "Date", "Status"])

        for booking in bookings:
            date_str = booking["date"].strftime("%Y-%m-%d") if isinstance(booking["date"], datetime) else str(booking["date"])
            start_str = booking["start"].strftime("%H:%M") if isinstance(booking["start"], datetime) else str(booking["start"])
            end_str = booking["end"].strftime("%H:%M") if isinstance(booking["end"], datetime) else str(booking["end"])

            writer.writerow([
                booking["room"],
                booking["teacher"],
                start_str,
                end_str,
                date_str,
                booking["status"]
            ])

    return filename
