# === Stage 35: Add active user switching and user-specific records ===
# Project: ClassroomBook
# Step 35: Active user switching and user-specific records
import getpass
from datetime import datetime

active_user = getpass.getuser()

# Store user-specific records in a file
record_file = f"records_{active_user}.json"

def save_record(record):
    with open(record_file, "a") as f:
        f.write(f"{datetime.now().isoformat()},{record}\n")

def read_records():
    try:
        with open(record_file, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

# Example usage:
save_record("Booked room 101 for math class")
records = read_records()
for r in records:
    print(r.strip())
