# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ClassroomBook
class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

class Timeslot:
    def __init__(self, day, hour, minute):
        self.day = day
        self.hour = hour
        self.minute = minute

class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

rooms = [Room("Room A", 30), Room("Room B", 50), Room("Room C", 100)]
timeslots = [Timeslot("Monday", 9, 0), Timeslot("Monday", 10, 0), Timeslot("Monday", 11, 0)]
teachers = [Teacher("Dr. Smith", ["Math"]), Teacher("Prof. Jones", ["Physics"]), Teacher("Dr. Lee", ["Chemistry"])]
