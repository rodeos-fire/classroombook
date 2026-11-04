# === Stage 66: Add export of a short status dashboard ===
# Project: ClassroomBook
def export_status_dashboard(rooms, bookings):
    status = {}
    for room in rooms:
        room_id = room["id"]
        booked = sum(1 for b in bookings if b["room_id"] == room_id)
        total = len(rooms)
        status[room_id] = {"booked": booked, "free": total - booked, "utilization": round(booked / total, 2)}
    total_bookings = len(bookings)
    dashboard = {"total_rooms": total, "total_bookings": total_bookings, "rooms": status}
    with open("status_dashboard.json", "w") as f:
        import json
        json.dump(dashboard, f, indent=2)
    return dashboard
