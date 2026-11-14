# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: ClassroomBook
def demo_cli():
    from classroombook.core import ClassroomBook
    from classroombook.commands import add_room, add_teacher, add_booking, list_bookings, list_conflicts, cancel_booking
    book = ClassroomBook("Week 1")
    add_room(book, "Room A", 20)
    add_teacher(book, "Alice", "CS101")
    add_teacher(book, "Bob", "CS102")
    add_booking(book, "Room A", "Alice", "CS101", "09:00", "09:45")
    add_booking(book, "Room A", "Bob", "CS102", "09:00", "10:00")
    print("--- Add room, teacher, and bookings ---")
    print(add_room.__doc__)
    print(add_teacher.__doc__)
    print(add_booking.__doc__)
    print("--- List bookings ---")
    print(list_bookings(book))
    print("--- List conflicts ---")
    print(list_conflicts(book))
    print("--- Cancel booking ---")
    print(cancel_booking(book, "Room A", "Alice", "CS101", "09:00", "09:45"))
