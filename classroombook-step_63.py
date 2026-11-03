# === Stage 63: Add relationships between records where useful ===
# Project: ClassroomBook
class Booking:
    def __init__(self, teacher, room, start, end):
        self.teacher = teacher
        self.room = room
        self.start = start
        self.end = end

    def overlaps(self, other):
        if self.teacher is other.teacher:
            return self.start < other.end and other.start < self.end
        if self.room is other.room:
            return self.start < other.end and other.start < self.end
        return False


class ClassroomBook:
    def __init__(self):
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)
        for other in self.bookings:
            if other is not booking and booking.overlaps(other):
                raise ValueError("Time conflict between bookings")

    def find_conflicts(self):
        conflicts = []
        for i, a in enumerate(self.bookings):
            for b in self.bookings[i + 1:]:
                if a.overlaps(b):
                    conflicts.append((a, b))
        return conflicts
