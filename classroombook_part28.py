# === Stage 28: Add overdue item detection based on due dates ===
# Project: ClassroomBook
from datetime import datetime, timedelta

def is_overdue(due_date_str, today=None):
    if today is None:
        today = datetime.now().date()
    due = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    return due < today
