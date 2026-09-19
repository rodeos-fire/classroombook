# === Stage 45: Add restore from backup with validation ===
# Project: ClassroomBook
import json, os

BACKUP_FILE = "classroom_book_backup.json"

def validate_booking_data(data):
    required = {"rooms": list, "timeslots": list, "teachers": list}
    for key, expected in required.items():
        if key not in data or not isinstance(data[key], expected):
            return False, f"Missing or invalid field: {key}"
    for room in data["rooms"]:
        if not isinstance(room, dict) or "name" not in room or "capacity" not in room:
            return False, "Each room must have 'name' and 'capacity'"
    for ts in data["timeslots"]:
        if not isinstance(ts, dict) or "start" not in ts or "end" not in ts:
            return False, "Each timeslot must have 'start' and 'end'"
    for teacher in data["teachers"]:
        if not isinstance(teacher, dict) or "name" not in teacher:
            return False, "Each teacher must have 'name'"
    return True, None

def restore_from_backup():
    if not os.path.exists(BACKUP_FILE):
        print(f"No backup found at {BACKUP_FILE}")
        return None
    with open(BACKUP_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Backup file is corrupted")
            return None
    valid, msg = validate_booking_data(data)
    if not valid:
        print(f"Backup validation failed: {msg}")
        return None
    print("Backup restored successfully")
    return data
