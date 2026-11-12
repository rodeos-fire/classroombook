# === Stage 81: Add final README text as a module string with usage examples ===
# Project: ClassroomBook
class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f"Room({self.name}, {self.capacity})"


class Teacher:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Teacher({self.name})"


class TimeSlot:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlaps(self, other):
        return self.start < other.end and other.start < self.end

    def __repr__(self):
        return f"TimeSlot({self.start}, {self.end})"


class Booking:
    def __init__(self, room, teacher, timeslot):
        self.room = room
        self.teacher = teacher
        self.timeslot = timeslot

    def overlaps(self, other):
        return self.timeslot.overlaps(other.timeslot)

    def __repr__(self):
        return (f"Booking({self.room.name}, {self.teacher.name}, "
                f"{self.timeslot.start}-{self.timeslot.end})")


class ClassroomBook:
    def __init__(self):
        self.rooms = []
        self.teachers = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_booking(self, room, teacher, timeslot):
        for existing in self.bookings:
            if existing.overlaps(self.__make(timeslot)) and \
               (existing.room is room or existing.teacher is teacher):
                raise ValueError("Conflict detected")
        self.bookings.append(self.__make(timeslot))

    def __make(self, timeslot):
        return Booking(room, teacher, timeslot)


book = ClassroomBook()
book.add_room(Room("A101", 40))
book.add_teacher(Teacher("Ms. Lee"))
book.add_booking(Room("A101", 40), Teacher("Ms. Lee"), TimeSlot("09:00", "10:00"))
print(book.bookings)
