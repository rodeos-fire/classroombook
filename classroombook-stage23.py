# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ClassroomBook
class Tag:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Tag({self.name!r})"
    def __eq__(self, other):
        return isinstance(other, Tag) and self.name == other.name
    def __hash__(self):
        return hash(self.name)

def add_tag(tags, name):
    if not isinstance(name, Tag):
        name = Tag(name)
    if name not in tags:
        tags.append(name)
    return tags

def remove_tag(tags, name):
    if not isinstance(name, Tag):
        name = Tag(name)
    if name in tags:
        tags.remove(name)
    return tags

def tag_summary(tags):
    return {t.name: 0 for t in tags}
