# === Stage 57: Add structured result objects for command handlers ===
# Project: ClassroomBook
from dataclasses import dataclass
from typing import Optional


@dataclass
class BookingResult:
    booking_id: str
    room_id: str
    teacher_id: str
    timeslot: str
    status: str = "confirmed"
    conflict: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "booking_id": self.booking_id,
            "room_id": self.room_id,
            "teacher_id": self.teacher_id,
            "timeslot": self.timeslot,
            "status": self.status,
            "conflict": self.conflict,
        }


@dataclass
class RoomInfo:
    room_id: str
    name: str
    capacity: int
    is_available: bool = True

    def to_dict(self) -> dict:
        return {
            "room_id": self.room_id,
            "name": self.name,
            "capacity": self.capacity,
            "is_available": self.is_available,
        }
