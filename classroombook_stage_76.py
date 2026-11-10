# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: ClassroomBook
def handle_sigint(signum, frame):
    print()
    print("Booking cancelled. Goodbye.")
    sys.exit(0)


try:
    while True:
        main()
except KeyboardInterrupt:
    print()
    print("Booking cancelled. Goodbye.")
    sys.exit(0)
