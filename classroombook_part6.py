# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ClassroomBook
def delete_booking(bookings, booking_id, confirm=False):
    """Delete a booking by ID with optional confirmation."""
    if not confirm:
        print(f"⚠️  Booking {booking_id} will be deleted. Type 'yes' to confirm.")
        user_input = input("Delete? (yes/no): ").strip().lower()
        if user_input != "yes":
            print("Cancelling delete.")
            return bookings
    try:
        bookings.remove(booking_id)
        print(f"✅ Booking {booking_id} deleted.")
        return bookings
    except ValueError:
        print(f"❌ Booking {booking_id} not found.")
        return bookings
