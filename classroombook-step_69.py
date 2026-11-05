# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ClassroomBook
def reset_demo_data(db):
    with db.atomic():
        Booking.delete().execute()
        Teacher.delete().execute()
        Room.delete().execute()
        Timeslot.delete().execute()
        TimeslotSlot.delete().execute()
        Timeslot.create(name="Morning", start_time="08:00", end_time="09:30").execute()
        Timeslot.create(name="Afternoon", start_time="13:00", end_time="14:30").execute()
        Timeslot.create(name="Evening", start_time="17:00", end_time="18:00").execute()
        Room.create(name="Room A", capacity=30, subject="Math").execute()
        Room.create(name="Room B", capacity=20, subject="Science").execute()
        Teacher.create(name="Alice", subject="Math").execute()
        Teacher.create(name="Bob", subject="Science").execute()
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
            for ts in list(Timeslot.objects.all()):
                TimeslotSlot.create(timeslot=ts, day=day).execute()
    print("Demo data reset complete.")
