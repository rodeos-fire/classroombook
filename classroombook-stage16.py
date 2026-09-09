# === Stage 16: Add argparse support for the most common commands ===
# Project: ClassroomBook
import argparse

def main():
    parser = argparse.ArgumentParser(description="ClassroomBook CLI")
    sub = parser.add_subparsers(dest="command")

    book_parser = sub.add_parser("book", help="Book a room")
    book_parser.add_argument("room", help="Room name")
    book_parser.add_argument("date", help="Date (YYYY-MM-DD)")
    book_parser.add_argument("start", help="Start time (HH:MM)")
    book_parser.add_argument("end", help="End time (HH:MM)")
    book_parser.add_argument("--teacher", default=None, help="Optional teacher name")

    show_parser = sub.add_parser("show", help="Show bookings")
    show_parser.add_argument("room", nargs="?", default=None, help="Optional room filter")

    conflict_parser = sub.add_parser("conflicts", help="Show conflicts")
    conflict_parser.add_argument("date", nargs="?", default=None, help="Optional date filter")

    args = parser.parse_args()
    print(f"ClassroomBook command: {args.command}")
    if hasattr(args, "room"):
        print(f"Room: {args.room}")
    if hasattr(args, "date"):
        print(f"Date: {args.date}")
    if hasattr(args, "start"):
        print(f"Start: {args.start}")
    if hasattr(args, "end"):
        print(f"End: {args.end}")
    if hasattr(args, "teacher"):
        print(f"Teacher: {args.teacher}")

if __name__ == "__main__":
    main()
