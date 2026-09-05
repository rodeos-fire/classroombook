# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ClassroomBook
def update_booking(booking_id, **kwargs):
    """Update a booking's fields; returns (success, message)."""
    bookings = _load("bookings.json")
    if booking_id not in bookings:
        return False, f"Booking {booking_id} not found."
    record = bookings[booking_id]
    for field, value in kwargs.items():
        if field not in record:
            return False, f"Unknown field '{field}'. Valid: {list(record.keys())}"
        record[field] = value
    _save("bookings.json", bookings)
    return True, f"Booking {booking_id} updated."
