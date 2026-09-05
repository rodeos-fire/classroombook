# === Stage 4: Implement create operations for the primary records ===
# Project: ClassroomBook
def create_room(name, capacity):
    rooms[name] = {"name": name, "capacity": capacity}

def create_timeslot(hour, minute):
    slot = f"{hour:02d}:{minute:02d}"
    slots.append(slot)

def create_teacher(first, last):
    teacher_id = f"{first}_{last}"
    teachers[teacher_id] = {"first": first, "last": last}

def create_booking(room_name, teacher_id, time_slot):
    if room_name not in rooms:
        print(f"Error: Room '{room_name}' does not exist.")
        return
    if teacher_id not in teachers:
        print(f"Error: Teacher '{teacher_id}' does not exist.")
        return
    if time_slot not in slots:
        print(f"Error: Time slot '{time_slot}' does not exist.")
        return
    key = f"{room_name}_{teacher_id}_{time_slot}"
    bookings[key] = {"room": room_name, "teacher": teacher_id, "slot": time_slot}
