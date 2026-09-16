# === Stage 36: Add templates for quickly creating common records ===
# Project: ClassroomBook
class RecordTemplates:
    """Factory helpers that produce pre-filled common records."""

    @staticmethod
    def new_booking(teacher, room, slot):
        return Booking(teacher, room, slot)

    @staticmethod
    def new_request(teacher, slot):
        return Request(teacher, slot)

    @staticmethod
    def new_cancellation(booking, reason="Teacher cancelled"):
        return Cancellation(booking, reason)

    @staticmethod
    def new_conflict(booking_a, booking_b):
        return Conflict(booking_a, booking_b)
