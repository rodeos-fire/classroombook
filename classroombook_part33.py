# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ClassroomBook
# settings.py — classroom booking settings

SETTINGS = {
    "default_duration": 60,  # minutes per timeslot
    "max_bookings": 10,
    "booking_lead_days": 7,
    "allowed_rooms": ["Room A", "Room B", "Room C"],
    "allowed_teachers": ["Mr. Smith", "Ms. Jones", "Mr. Brown"],
    "timezone": "UTC",
}


def update_settings(key, value):
    """Update a single setting by key and return the new value."""
    SETTINGS[key] = value
    return SETTINGS[key]


def get_all_settings():
    """Return a copy of the full settings dictionary."""
    return SETTINGS.copy()
