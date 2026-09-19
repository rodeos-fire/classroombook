# === Stage 46: Add a schema version field and migration helper ===
# Project: ClassroomBook
SCHEMA_VERSION = 2


def migrate_to_v2(db):
    """Migrate existing data from v1 schema to v2 by adding a version column.

    This assumes the existing table already has the required columns (id,
    room_id, time_slot_id, teacher_id, status). We add a 'version' column
    and set it to SCHEMA_VERSION for all rows. This is a no-op migration
    that ensures forward compatibility.
    """
    cursor = db.cursor()
    cursor.execute("ALTER TABLE classroom_bookings ADD COLUMN IF NOT EXISTS version INTEGER DEFAULT 1")
    cursor.execute("UPDATE classroom_bookings SET version = %s", (SCHEMA_VERSION,))
    db.commit()
    return True
