# === Stage 73: Add a lightweight HTML report export ===
# Project: ClassroomBook
def export_html_report(bookings, rooms, teachers):
    """Write a compact HTML report of all bookings to bookings.html."""
    with open("bookings.html", "w", encoding="utf-8") as f:
        f.write("<html><head><title>ClassroomBook Report</title>")
        f.write("<style>table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:6px}</style></head>")
        f.write("<body><h1>ClassroomBook Report</h1>")
        f.write("<p>Total bookings: %d</p>" % len(bookings))
        f.write("<table><tr><th>Room</th><th>Teacher</th><th>Start</th><th>End</th><th>Status</th></tr>")
        for b in bookings:
            status = "OK" if not b["conflict"] else "CONFLICT"
            f.write("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
                    % (b["room"], b["teacher"], b["start"], b["end"], status))
        f.write("</table></body></html>")
