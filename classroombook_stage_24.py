# === Stage 24: Add grouped summaries by category or status ===
# Project: ClassroomBook
def grouped_booking_summary(bookings):
    """Summarize bookings by category or status."""
    from collections import Counter
    categories = Counter(b["category"] for b in bookings)
    statuses = Counter(b["status"] for b in bookings)
    return {"by_category": dict(categories), "by_status": dict(statuses)}
