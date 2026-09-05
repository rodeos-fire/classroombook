# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ClassroomBook
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Room:
    name: str
    capacity: int
    equipment: list[str] = field(default_factory=list)


@dataclass
class TimeSlot:
    start: datetime
    end: datetime
    day: str = ""


@dataclass
class Teacher:
    name: str
    email: str
    availability: list[TimeSlot] = field(default_factory=list)


@dataclass
class Booking:
    room: Room
    teacher: Teacher
    time_slot: TimeSlot
    date: datetime
    confirmed: bool = False


@dataclass
class Conflict:
    booking: Booking
    overlap_start: datetime
    overlap_end: datetime
