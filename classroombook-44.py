# === Stage 44: Add backup creation for the data file ===
# Project: ClassroomBook
import shutil
import os

def create_backup(data_file, backup_dir="backups"):
    """Create a timestamped backup of the ClassroomBook data file."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"classroombook_{timestamp}.json")
    shutil.copy2(data_file, backup_path)
    print(f"Backup created at {backup_path}")
    return backup_path
