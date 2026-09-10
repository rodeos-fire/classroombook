# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ClassroomBook
import datetime

class ActivityLog:
    """Compact activity log with timestamps and action names."""

    def __init__(self):
        self._entries = []

    def log(self, action: str, *args):
        """Record an action with a timestamp."""
        self._entries.append(
            {
                "timestamp": datetime.datetime.now().isoformat(),
                "action": action,
                "details": ", ".join(str(a) for a in args),
            }
        )

    def get_log(self) -> list:
        """Return all logged entries."""
        return list(self._entries)

    def clear(self):
        """Clear all log entries."""
        self._entries.clear()
