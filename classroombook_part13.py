# === Stage 13: Add file save support using a configurable path ===
# Project: ClassroomBook
import os, json

SAVE_PATH = os.getenv("CLASSROOMBOOK_SAVE", "classroombook.json")

def save_book(book):
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(book, f, indent=2, default=str)
    return SAVE_PATH

def load_book(path=None):
    p = path or SAVE_PATH
    if not os.path.exists(p):
        return {"rooms": [], "timeslots": [], "teachers": [], "bookings": []}
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)
