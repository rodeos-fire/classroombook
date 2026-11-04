# === Stage 67: Add a function that returns key project metrics ===
# Project: ClassroomBook
def get_project_metrics(rooms, timeslots, teachers, bookings):
    total_rooms = len(rooms)
    total_timeslots = len(timeslots)
    total_teachers = len(teachers)
    total_bookings = len(bookings)
    occupied_slots = sum(1 for b in bookings for s in b.get("timeslots", []))
    conflict_count = 0
    for b in bookings:
        for s in b.get("timeslots", []):
            for other in bookings:
                if other is b:
                    continue
                for o in other.get("timeslots", []):
                    if s["room"] == o["room"] and s["timeslot"] == o["timeslot"]:
                        conflict_count += 1
    utilization = (occupied_slots / (total_rooms * total_timeslots) * 100) if (total_rooms * total_timeslots) else 0
    return {
        "total_rooms": total_rooms,
        "total_timeslots": total_timeslots,
        "total_teachers": total_teachers,
        "total_bookings": total_bookings,
        "occupied_slots": occupied_slots,
        "conflict_count": conflict_count,
        "utilization_percent": round(utilization, 2)
    }
