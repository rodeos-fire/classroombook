# === Stage 89: Add final consistency checks for names, statuses, and dates ===
# Project: ClassroomBook
def validate_consistency(bookings, rooms, teachers):
    room_names = [r['name'] for r in rooms]
    teacher_names = [t['name'] for t in teachers]
    for b in bookings:
        if b['room'] not in room_names:
            raise ValueError(f"Booking {b['id']} references unknown room {b['room']}")
        if b['teacher'] not in teacher_names:
            raise ValueError(f"Booking {b['id']} references unknown teacher {b['teacher']}")
        if b['status'] not in ('confirmed', 'pending', 'cancelled'):
            raise ValueError(f"Booking {b['id']} has invalid status {b['status']}")
        if not isinstance(b['date'], str):
            raise ValueError(f"Booking {b['id']} has non-string date")
        if not isinstance(b['start'], str) or not isinstance(b['end'], str):
            raise ValueError(f"Booking {b['id']} has non-string timeslot")
        if b['start'] >= b['end']:
            raise ValueError(f"Booking {b['id']} has invalid timeslot")
        return True
