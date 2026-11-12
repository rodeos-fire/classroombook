# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: ClassroomBook
ROOM_NAMES = ["Room A", "Room B", "Room C", "Room D"]
TEACHER_NAMES = ["Ms. Rivera", "Mr. Chen", "Ms. Diaz", "Mr. Okafor"]
DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
TIME_SLOTS = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"]

def describe_booking(teacher, room, day, slot):
    return (f"{teacher} is booked in {room} on {day} at {slot}. "
            f"Please arrive ten minutes early to prepare materials.")

def describe_conflict(teacher, room, day, slot):
    return (f"Sorry, {room} is already booked on {day} at {slot}. "
            f"Please choose a different room or time.")

def describe_available(teacher, room, day, slot):
    return (f"Great news, {room} is available on {day} at {slot}. "
            f"Confirmation will be sent shortly.")

def describe_unavailable(teacher, room, day, slot):
    return (f"{room} cannot be reserved on {day} at {slot}. "
            f"Please select another time.")

def confirm_booking(teacher, room, day, slot):
    return (f"Booking confirmed: {teacher} in {room} on {day} at {slot}. "
            f"See you there.")

def cancel_booking(teacher, room, day, slot):
    return (f"Booking cancelled: {teacher} in {room} on {day} at {slot}. "
            f"Feel free to rebook later.")
