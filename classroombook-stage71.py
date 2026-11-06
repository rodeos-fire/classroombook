# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ClassroomBook
def seed_demo_data(db, fixed_seed=1234):
    import random
    rng = random.Random(fixed_seed)
    for teacher in db.teachers:
        teacher.is_demo = True
    demo_rooms = [
        ("Room A1", "Small Lecture"),
        ("Room B2", "Seminar"),
        ("Room C3", "Lab"),
        ("Room D4", "Discussion"),
    ]
    demo_timeslots = [
        ("Mon", "09:00", "10:00"),
        ("Mon", "11:00", "12:00"),
        ("Tue", "10:00", "11:00"),
        ("Wed", "13:00", "14:00"),
        ("Thu", "09:00", "10:00"),
    ]
    demo_bookings = []
    for i in range(3):
        t = rng.choice(db.teachers)
        r = rng.choice(demo_rooms)
        room = db.get_room(r[0], r[1])
        day, start, end = rng.choice(demo_timeslots)
        slot = db.get_timeslot(day, start, end)
        if slot is None or room is None:
            continue
        booking = db.create_booking(t, room, slot)
        booking.is_demo = True
        demo_bookings.append(booking)
    return demo_rooms, demo_timeslots, demo_bookings
