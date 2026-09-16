# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ClassroomBook
def repair_classroom_book(book):
    """Repair simple data integrity issues in a ClassroomBook instance."""
    repaired = 0
    try:
        if not book.rooms:
            book.rooms = {}
            repaired += 1
    except Exception:
        book.rooms = {}
        repaired += 1

    try:
        if not book.teachers:
            book.teachers = {}
            repaired += 1
    except Exception:
        book.teachers = {}
        repaired += 1

    try:
        if not book.timeslots:
            book.timeslots = {}
            repaired += 1
    except Exception:
        book.timeslots = {}
        repaired += 1

    try:
        if not book.bookings:
            book.bookings = []
            repaired += 1
    except Exception:
        book.bookings = []
        repaired += 1

    try:
        if not book.conflicts:
            book.conflicts = []
            repaired += 1
    except Exception:
        book.conflicts = []
        repaired += 1

    try:
        if hasattr(book, 'history') and not book.history:
            book.history = []
            repaired += 1
    except Exception:
        if hasattr(book, 'history'):
            book.history = []
            repaired += 1

    return repaired
