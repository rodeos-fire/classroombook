# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: ClassroomBook
def main():
    rooms = {"A101": Room("A101", "Lecture Hall"), "B202": Room("B202", "Seminar Room")}
    teachers = {"t1": Teacher("t1", "Alice"), "t2": Teacher("t2", "Bob")}
    slots = [Slot("09:00", "10:00"), Slot("11:00", "12:00")]

    bookings = []

    b1 = Book("t1", "A101", slots[0], "Intro to Python")
    bookings.append(b1)
    print("Booked:", b1.key)

    b2 = Book("t1", "A101", slots[1], "Data Structures")
    bookings.append(b2)
    print("Booked:", b2.key)

    b3 = Book("t2", "A101", slots[0], "Advanced Topics")
    if b3.is_conflict(bookings):
        print("Conflict detected for booking:", b3.key)
    else:
        bookings.append(b3)
        print("Booked:", b3.key)

    b4 = Book("t1", "B202", slots[0], "Backup Session")
    if b4.is_conflict(bookings):
        print("Conflict detected for booking:", b4.key)
    else:
        bookings.append(b4)
        print("Booked:", b4.key)

    for b in bookings:
        print(b.key, "| Room:", b.room_id, "| Teacher:", b.teacher_id,
              "| Time:", b.slot.start, "-", b.slot.end, "| Title:", b.title)


if __name__ == "__main__":
    main()
