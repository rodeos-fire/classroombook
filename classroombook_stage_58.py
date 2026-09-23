# === Stage 58: Add bulk update behavior for selected records ===
# Project: ClassroomBook
def bulk_update(self, updates: dict, ids: list) -> list:
        """Update multiple records at once.
        
        Args:
            updates: dict mapping column_name to new value.
            ids: list of primary keys to update.
        
        Returns:
            List of updated records.
        """
        if not updates or not ids:
            return []
        
        updated = []
        for record in self._records:
            if record["id"] in ids:
                for col, value in updates.items():
                    if col in record and record[col] != value:
                        record[col] = value
                updated.append(dict(record))
        return updated
