# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ClassroomBook
def upcoming_bookings(bookings, now=None):
    """Return bookings sorted by date ascending; remove any that already ended."""
    if now is None:
        now = datetime.now()
    return sorted(
        [b for b in bookings if b['end'] > now],
        key=lambda b: b['start'],
    )


def upcoming_conflicts(bookings, now=None):
    """Return a list of (booking_a, booking_b) pairs that overlap, ignoring ended ones."""
    if now is None:
        now = datetime.now()
    active = [b for b in bookings if b['end'] > now]
    conflicts = []
    for i in range(len(active)):
        for j in range(i + 1, len(active)):
            a, b = active[i], active[j]
            if a['room'] == b['room'] and a['start'] < b['end'] and b['start'] < a['end']:
                conflicts.append((a, b))
    return conflicts
