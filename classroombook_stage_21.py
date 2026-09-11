# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ClassroomBook
import json
from pathlib import Path

BOOKS_FILE = Path(__file__).parent / "books.json"
BACKUP_DIR = Path(__file__).parent / "backups"
BACKUP_DIR.mkdir(exist_ok=True)

def archive_completed():
    if not BOOKS_FILE.exists():
        return
    records = json.loads(BOOKS_FILE.read_text())
    now = datetime.now()
    for r in records:
        if r.get("status") in ("completed", "archived") or now.timestamp() - r.get("ts", 0) > 365 * 24 * 3600:
            r["archived"] = True
            r["archive_ts"] = now.timestamp()
    BOOKS_FILE.write_text(json.dumps(records, indent=2))

def restore_backup(days_back=1):
    if not BACKUP_DIR.exists():
        return False
    backups = sorted(BACKUP_DIR.glob("backup_*.json"), reverse=True)
    if not backups:
        return False
    target = backups[0]
    if target.stem.endswith(f"_days_{days_back}"):
        records = json.loads(target.read_text())
        BOOKS_FILE.write_text(json.dumps(records, indent=2))
        target.unlink()
        return True
    return False
