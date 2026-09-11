# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ClassroomBook
class Favorite:
    def __init__(self, room_id, teacher_id, timeslot_id):
        self.room_id = room_id
        self.teacher_id = teacher_id
        self.timeslot_id = timeslot_id

    def __repr__(self):
        return f"Favorite(room={self.room_id}, teacher={self.teacher_id}, slot={self.timeslot_id})"


class ClassroomBook:
    def __init__(self):
        self.rooms = []
        self.timeslots = []
        self.teachers = []
        self.bookings = []
        self.favorites = []

    def add_room(self, name):
        self.rooms.append(name)
        return self

    def add_timeslot(self, day, hour):
        self.timeslots.append({"day": day, "hour": hour})
        return self

    def add_teacher(self, name):
        self.teachers.append(name)
        return self

    def book(self, room, teacher, timeslot):
        self.bookings.append({
            "room": room,
            "teacher": teacher,
            "timeslot": timeslot,
        })
        return self

    def conflict(self, room, teacher, timeslot):
        for b in self.bookings:
            if b["room"] == room and b["teacher"] == teacher and b["timeslot"] == timeslot:
                return True
        return False

    def add_favorite(self, room_id, teacher_id, timeslot_id):
        self.favorites.append(Favorite(room_id, teacher_id, timeslot_id))
        return self

    def list_favorites(self):
        return [f for f in self.favorites]
