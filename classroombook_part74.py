# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ClassroomBook
def compare_snapshots(before, after):
    before = normalize_rooms(before)
    after = normalize_rooms(after)
    removed = [k for k in before if k not in after]
    added = [k for k in after if k not in before]
    changed = {}
    for k in before.keys() & after.keys():
        if before[k] != after[k]:
            changed[k] = {"before": before[k], "after": after[k]}
    return {"removed": removed, "added": added, "changed": changed}
