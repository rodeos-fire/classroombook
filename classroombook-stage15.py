# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ClassroomBook
def dispatch_command(text, context):
    """Parse a single-line command and return a response dict."""
    text = text.strip().lower()
    if not text:
        return {"status": "error", "message": "Empty command"}

    parts = text.split(maxsplit=1)
    verb = parts[0]

    if verb == "list":
        if "rooms" in context and context["rooms"]:
            return {"status": "ok", "message": "Available rooms: " + ", ".join(context["rooms"])}
        if "teachers" in context and context["teachers"]:
            return {"status": "ok", "message": "Available teachers: " + ", ".join(context["teachers"])}
        return {"status": "error", "message": "No data to list"}

    if verb == "book":
        if "rooms" not in context or "teachers" not in context:
            return {"status": "error", "message": "No rooms or teachers loaded"}
        args = parts[1] if len(parts) > 1 else ""
        if not args:
            return {"status": "error", "message": "Usage: book <room> <teacher> <time>"}
        room, teacher, time = args.split()
        return {"status": "ok", "message": f"Booked {room} with {teacher} at {time}"}

    if verb == "cancel":
        if "bookings" not in context or not context["bookings"]:
            return {"status": "error", "message": "No bookings to cancel"}
        args = parts[1] if len(parts) > 1 else ""
        if not args:
            return {"status": "error", "message": "Usage: cancel <room> <time>"}
        room, time = args.split()
        for i, b in enumerate(context["bookings"]):
            if b["room"] == room and b["time"] == time:
                context["bookings"].pop(i)
                return {"status": "ok", "message": f"Cancelled booking for {room} at {time}"}
        return {"status": "error", "message": "No matching booking found"}

    if verb == "status":
        if "bookings" not in context:
            return {"status": "ok", "message": "No bookings yet"}
        return {"status": "ok", "message": "Current bookings:\n" + "\n".join(f"- {b['room']} | {b['teacher']} | {b['time']}" for b in context["bookings"])}

    return {"status": "error", "message": f"Unknown command: {verb}"}
