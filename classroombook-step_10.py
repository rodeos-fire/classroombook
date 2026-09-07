# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ClassroomBook
def case_insensitive_search(self, query, field):
    """Search a field case-insensitively, returning matching records."""
    query_lower = query.lower()
    results = []
    for record in self._records:
        value = getattr(record, field, "")
        if query_lower in value.lower():
            results.append(record)
    return results
