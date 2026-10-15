"""File Organizer: categorises files, logs moves, and can undo the last run."""

import json
import shutil
from pathlib import Path
from datetime import datetime

LOG_FILE = "organizer_log.json"
CATEGORIES = {
    "Images": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"},
    "Audio": {".mp3", ".wav", ".aac", ".m4a", ".flac"},
    "Video": {".mp4", ".mov", ".avi", ".mkv", ".webm"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".c", ".cpp"}
}


def category_for(path):
    """Return a category folder based on the file extension."""
    suffix = path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if suffix in extensions:
            return category
    return "Others"


def unique_destination(destination):
    """Avoid overwriting by adding a numeric suffix if the path exists."""
    if not destination.exists():
        return destination
    counter = 1
    while True:
        candidate = destination.with_name(f"{destination.stem}_{counter}{destination.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def organize(folder):
    """Move files into category folders and record original/destination paths."""
    folder = folder.resolve()
    if not folder.is_dir():
        print("That folder does not exist.")
        return
    actions = []
    # Snapshot files before creating/moving category folders.
    files = [p for p in folder.iterdir() if p.is_file() and p.name != LOG_FILE]
    for source in files:
        category = category_for(source)
        target_folder = folder / category
        target_folder.mkdir(exist_ok=True)
        destination = unique_destination(target_folder / source.name)
        try:
            shutil.move(str(source), str(destination))
            actions.append({"source": str(source), "destination": str(destination)})
            print(f"{source.name} -> {category}/{destination.name}")
        except OSError as error:
            print(f"Could not move {source.name}: {error}")
    log = {"time": datetime.now().isoformat(timespec="seconds"), "actions": actions}
    Path(LOG_FILE).write_text(json.dumps(log, indent=4), encoding="utf-8")
    print(f"Organized {len(actions)} file(s). Log saved to {LOG_FILE}.")


def undo_last():
    """Move files from the most recent log back to their original paths."""
    log_path = Path(LOG_FILE)
    if not log_path.exists():
        print("No organizer log found.")
        return
    try:
        log = json.loads(log_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Cannot read log: {error}")
        return
    restored = 0
    for action in reversed(log.get("actions", [])):
        source = Path(action["source"])
        destination = Path(action["destination"])
        if not destination.exists():
            print(f"Skipped missing file: {destination}")
            continue
        if source.exists():
            print(f"Skipped because original path is occupied: {source}")
            continue
        try:
            source.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(destination), str(source))
            restored += 1
            print(f"Restored {source.name}")
        except OSError as error:
            print(f"Could not restore {source.name}: {error}")
    print(f"Undo finished. Restored {restored} file(s).")


def main():
    """Display the menu and request a folder path."""
    while True:
        print("\n=== File Organizer ===\n1 Organize a folder\n2 Undo last organization\n0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            folder = input("Folder path (use a TEST folder first): ").strip().strip('"')
            organize(Path(folder).expanduser())
        elif choice == "2":
            undo_last()
        elif choice == "0":
            break
        else:
            print("Choose a valid option.")


if __name__ == "__main__":
    main()
