# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ClassroomBook
def filter_bookings(bookings, status=None, category=None, owner=None, tag=None):
    results = bookings
    if status is not None:
        results = [b for b in results if b.get("status") == status]
    if category is not None:
        results = [b for b in results if b.get("category") == category]
    if owner is not None:
        results = [b for b in results if b.get("owner") == owner]
    if tag is not None:
        results = [b for b in results if tag in b.get("tags", [])]
    return results
