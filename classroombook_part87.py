# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: ClassroomBook
def reports_equal(report_a, report_b):
    normalized_a = _normalize_report(report_a)
    normalized_b = _normalize_report(report_b)
    return normalized_a == normalized_b


def _normalize_report(report):
    normalized = []
    for entry in report:
        normalized.append((entry["room"], entry["teacher"], _slot(entry["start"], entry["end"])))
    normalized.sort()
    return tuple(normalized)


def _slot(start, end):
    return (start["year"], start["month"], start["day"], start["hour"], start["minute"],
            end["year"], end["month"], end["day"], end["hour"], end["minute"])
