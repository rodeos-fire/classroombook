# === Stage 60: Add saved views for frequently used filters ===
# Project: ClassroomBook
class SavedView:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}

    def apply(self, rooms, timeslots, teachers):
        result = []
        for room in rooms:
            for ts in timeslots:
                if self.filters.get("room") and room.name != self.filters["room"]:
                    continue
                if self.filters.get("timeslot") and ts.name != self.filters["timeslot"]:
                    continue
                if self.filters.get("teacher") and not any(
                    t.name == self.filters["teacher"] for t in teachers
                ):
                    continue
                result.append({"room": room, "timeslot": ts})
        return result
