# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ClassroomBook
def bulk_delete_bookings(bookings, confirm_flag):
    if not confirm_flag:
        print("Bulk delete requires confirmation. Use confirm_flag=True to proceed.")
        return bookings
    deleted_count = sum(1 for b in bookings if b.status == "booked")
    for b in bookings:
        if b.status == "booked":
            b.status = "deleted"
    print(f"Bulk deleted {deleted_count} bookings.")
    return bookings
