# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: ClassroomBook
class BookingReport:
    def __init__(self):
        self.warnings = []
        self.errors = []

    def add_warning(self, message):
        self.warnings.append(message)

    def add_error(self, message):
        self.errors.append(message)

    def report(self):
        lines = ["=== Booking Validation Report ===", ""]
        lines.append("Errors (%d):" % len(self.errors))
        for error in self.errors:
            lines.append("  - " + error)
        lines.append("")
        lines.append("Warnings (%d):" % len(self.warnings))
        for warning in self.warnings:
            lines.append("  - " + warning)
        lines.append("")
        return "\n".join(lines)


def validate_bookings(rooms, teachers, bookings):
    report = BookingReport()
    for booking in bookings:
        for teacher in booking.get("assigned_teachers", []):
            for room in booking.get("assigned_rooms", []):
                if teacher in room.get("allowed_teachers", []):
                    report.add_warning(
                        "Teacher %s assigned to room %s (allowed pairing)."
                        % (teacher, room)
                    )
                else:
                    report.add_error(
                        "Teacher %s not allowed in room %s."
                        % (teacher, room)
                    )
    return report
