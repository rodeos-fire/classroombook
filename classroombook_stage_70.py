# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ClassroomBook
def confirm(prompt):
    return input(prompt).strip().lower() in ("y", "yes")

def clear_state():
    if not confirm("This will clear all data. Continue? (y/N): "):
        print("Aborted.")
        return
    rooms.clear()
    timeslots.clear()
    teachers.clear()
    bookings.clear()
    print("All data cleared.")
