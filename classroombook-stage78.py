# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: ClassroomBook
def _extract_room_names(bookings, room_filter=None):
    names = []
    for b in bookings:
        r = b.get("room")
        if r and (room_filter is None or r.lower() == room_filter.lower()):
            names.append(r)
    return names


def _find_free_timeslot(bookings, teacher, start, end, duration, exclude=None):
    slots = _generate_timeslots(start, end, duration)
    for s in slots:
        if s["teacher"] != teacher and (exclude is None or s["id"] not in exclude):
            if not _has_conflict(s, bookings):
                return s
    return None


def _generate_timeslots(start, end, duration):
    slots = []
    current = start
    while current < end:
        finish = _add_duration(current, duration)
        if finish > end:
            break
        slots.append({"id": current.strftime("%Y%m%dT%H%M%S"), "start": current, "end": finish, "teacher": None})
        current = finish
    return slots


def _add_duration(ts, duration):
    return ts + timedelta(minutes=duration)


def _has_conflict(slot, bookings):
    for b in bookings:
        if b.get("teacher") == slot["teacher"]:
            if _time_overlaps(slot["start"], slot["end"], b["start"], b["end"]):
                return True
    return False


def _time_overlaps(s1, e1, s2, e2):
    return s1 < e2 and s2 < e1
