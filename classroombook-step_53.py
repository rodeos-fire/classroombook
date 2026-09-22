# === Stage 53: Add command help text and usage examples ===
# Project: ClassroomBook
HELP_TEXT = (
    "Usage: python ClassroomBook.py <command> [args]\n"
    "Commands:\n"
    "  add-room      Add a new room with optional name and capacity\n"
    "  list-rooms    Show all registered rooms\n"
    "  add-teacher   Register a teacher with optional name and subject\n"
    "  list-teachers Show all registered teachers\n"
    "  add-slot      Add a timeslot (e.g. Mon 09:00-10:00)\n"
    "  list-slots    Show all defined timeslots\n"
    "  book          Book a room for a slot, optionally with teacher\n"
    "  cancel        Cancel a booking by room and slot\n"
    "  conflicts     Check all bookings for overlapping conflicts\n"
    "  status        Show current booking status summary\n"
    "  help          Show this help message\n"
)
