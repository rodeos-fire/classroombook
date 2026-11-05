# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ClassroomBook
def generate_changelog(activity_log):
    """Build a compact changelog from a list of {date, author, message} entries.

    Groups entries by date and prefixes each line with the author name,
    keeping the output short and chronological. Returns a list of strings.
    """
    grouped = {}
    for entry in activity_log:
        grouped.setdefault(entry.get('date', 'unknown'), []).append(entry)

    changelog = []
    for date in sorted(grouped):
        lines = grouped[date]
        lines.sort(key=lambda e: e.get('timestamp', ''))
        author = lines[0].get('author', 'unknown')
        prefix = f"{date} [{author}]"
        for entry in lines:
            message = entry.get('message', '')
            changelog.append(f"{prefix}: {message}" if message else prefix)
    return changelog
