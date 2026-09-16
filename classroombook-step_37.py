# === Stage 37: Add recommendations for the next useful action ===
# Project: ClassroomBook
class BookingConflictError(Exception):
    """Raised when a new booking overlaps an existing one."""
    def __init__(self, message="Booking conflict detected", details=None):
        super().__init__(message)
        self.details = details or {}

    def __str__(self):
        if self.details:
            return f"{self.args[0]}: {self.details}"
        return self.args[0]

    def __repr__(self):
        return f"BookingConflictError({self.args[0]!r}, details={self.details!r})"
