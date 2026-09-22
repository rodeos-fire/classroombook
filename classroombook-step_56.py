# === Stage 56: Add compact error classes for domain failures ===
# Project: ClassroomBook
class ConflictError(Exception):
    pass

class RoomAlreadyBookedError(Exception):
    pass

class TeacherBusyError(Exception):
    pass

class InvalidTimeSlotError(Exception):
    pass

class NoAvailableRoomError(Exception):
    pass

class DuplicateBookingError(Exception):
    pass
