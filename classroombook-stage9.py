# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ClassroomBook
def sort_entries(self, sort_key='date'):
    """Sort bookings by title, date, priority, or last update."""
    keys = {
        'title': lambda b: (b.title, b.date, b.priority, b.updated),
        'date': lambda b: (b.date, b.priority, b.updated),
        'priority': lambda b: (b.priority, b.date, b.updated),
        'updated': lambda b: (b.updated, b.date, b.priority),
    }
    if sort_key not in keys:
        raise ValueError(f"Unknown sort key: {sort_key}. Use title, date, priority, or updated.")
    self.bookings.sort(key=keys[sort_key])
