# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ClassroomBook
# demo.py – ClassroomBook demo scenario

from classroom_book import ClassroomBook

book = ClassroomBook()

# Create rooms
book.add_room("Room 101", capacity=30)
book.add_room("Room 202", capacity=15)
book.add_room("Lab 303", capacity=50)

# Create teachers
book.add_teacher("Alice", "Computer Science")
book.add_teacher("Bob", "Mathematics")
book.add_teacher("Carol", "Physics")

# Create timeslots
book.add_timeslot("Monday 9:00", "Monday 10:00")
book.add_timeslot("Monday 10:00", "Monday 11:00")
book.add_timeslot("Tuesday 9:00", "Tuesday 10:00")

# Book classes
book.book_class("Alice", "Monday 9:00", "Room 101")
book.book_class("Bob", "Monday 10:00", "Room 202")
book.book_class("Carol", "Tuesday 9:00", "Lab 303")

# Try conflicting booking
try:
    book.book_class("Alice", "Monday 9:00", "Room 202")
except ConflictError:
    print("Conflict detected: Alice cannot book Room 202 at Monday 9:00")

# Show schedule
print("\nCurrent Schedule:")
for entry in book.schedule:
    print(f"{entry[0]}: {entry[1]} in {entry[2]}")
