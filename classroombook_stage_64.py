# === Stage 64: Add validation for relationship references ===
# Project: ClassroomBook
def validate_references(book):
    errors = []
    for room in book.rooms:
        for booking in room.bookings:
            if booking.teacher_id not in [t.id for t in book.teachers]:
                errors.append(f"Booking in room {room.id} references unknown teacher {booking.teacher_id}")
            for reservation in room.reservations:
                if reservation.teacher_id not in [t.id for t in book.teachers]:
                    errors.append(f"Reservation in room {room.id} references unknown teacher {reservation.teacher_id}")
    for booking in [b for room in book.rooms for b in room.bookings]:
        if not booking.start <= booking.end:
            errors.append(f"Booking {booking.id} has start after end")
    for reservation in [r for room in book.rooms for r in room.reservations]:
        if not reservation.start <= reservation.end:
            errors.append(f"Reservation {reservation.id} has start after end")
    return errors
