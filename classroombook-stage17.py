# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ClassroomBook
def dry_run(command):
    """Simulate a command without mutating state; return (success, message)."""
    commands = {
        "book": lambda: _dry_book(),
        "release": lambda: _dry_release(),
        "cancel": lambda: _dry_cancel(),
        "list": lambda: _dry_list(),
        "search": lambda: _dry_search(),
    }
    if command not in commands:
        return False, f"Unknown command for dry-run: {command}"
    return commands[command]()


def _dry_book():
    room, teacher, date, time_slot = _parse_args()
    if not _is_slot_free(room, teacher, date, time_slot):
        return False, f"Slot {time_slot} on {date} in room {room} is already booked."
    return True, f"Would book {room} for {teacher} on {date} {time_slot}."


def _dry_release():
    room, teacher, date, time_slot = _parse_args()
    if not _is_slot_free(room, teacher, date, time_slot):
        return True, f"Would release {room} for {teacher} on {date} {time_slot}."
    return False, f"Slot {time_slot} on {date} in room {room} is already free; nothing to release."


def _dry_cancel():
    booking_id = _parse_args()[0]
    booking = _find_booking(booking_id)
    if not booking:
        return False, f"No booking found with id {booking_id}."
    return True, f"Would cancel booking {booking_id}."


def _dry_list():
    return True, _display_bookings()


def _dry_search():
    query = _parse_args()[0]
    results = _search_bookings(query)
    if not results:
        return False, f"No bookings match '{query}'."
    return True, f"Found {len(results)} matching booking(s):\n" + _display_bookings(results)
