"""
Downloads Auto-Organizer
Watches a folder and moves files into subfolders based on their extension.
"""

import os
import shutil
import time
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import WATCH_FOLDER, EXTENSION_MAP, UNKNOWN_FOLDER, LOG_LEVEL

# ── Logging setup ──────────────────────────────────────────────────────────────
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("organizer")


# ── Core helper ────────────────────────────────────────────────────────────────
def resolve_destination(file_path: Path, watch_dir: Path) -> Path:
    """Return the target directory for *file_path* based on its extension."""
    suffix = file_path.suffix.lower().lstrip(".")
    folder_name = EXTENSION_MAP.get(suffix, UNKNOWN_FOLDER)
    return watch_dir / folder_name


def safe_move(src: Path, dest_dir: Path) -> None:
    """
    Move *src* into *dest_dir*, creating the directory if needed.
    If a file with the same name already exists, appends a counter suffix.
    """
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name

    # Avoid collision by appending _1, _2, … before the extension
    if dest.exists() and dest != src:
        stem, suffix = src.stem, src.suffix
        counter = 1
        while dest.exists():
            dest = dest_dir / f"{stem}_{counter}{suffix}"
            counter += 1

    shutil.move(str(src), str(dest))
    log.info("Moved  %-40s  →  %s", src.name, dest_dir.name)


def organize_existing(watch_dir: Path) -> None:
    """Move files already present in *watch_dir* when the script starts."""
    log.info("Scanning existing files in %s …", watch_dir)
    moved = 0
    for item in watch_dir.iterdir():
        if item.is_file():
            dest = resolve_destination(item, watch_dir)
            if dest != watch_dir:          # don't move if it would stay put
                safe_move(item, dest)
                moved += 1
    log.info("Initial scan done — %d file(s) moved.", moved)


# ── Watchdog handler ───────────────────────────────────────────────────────────
class DownloadsHandler(FileSystemEventHandler):
    def __init__(self, watch_dir: Path):
        super().__init__()
        self.watch_dir = watch_dir

    def _handle(self, src_path: str) -> None:
        path = Path(src_path)

        # Ignore directories, hidden files, and temp download files
        if path.is_dir():
            return
        if path.name.startswith("."):
            return
        if path.suffix.lower() in {".crdownload", ".part", ".tmp", ".download"}:
            return
        # Only act on direct children of the watched folder
        if path.parent != self.watch_dir:
            return

        # Small delay — let the file finish being written
        time.sleep(0.5)

        dest = resolve_destination(path, self.watch_dir)
        if dest == self.watch_dir:
            return  # already in the right place (unlikely but safe)

        try:
            safe_move(path, dest)
        except FileNotFoundError:
            log.debug("File already gone before we could move it: %s", path.name)
        except PermissionError:
            log.warning("Permission denied — skipping: %s", path.name)
        except Exception as exc:
            log.error("Unexpected error moving %s: %s", path.name, exc)

    # Watchdog fires on_created for new downloads and on_moved for in-place saves
    def on_created(self, event):
        if not event.is_directory:
            self._handle(event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            self._handle(event.dest_path)


# ── Entry point ────────────────────────────────────────────────────────────────
def main() -> None:
    watch_dir = Path(WATCH_FOLDER).expanduser().resolve()

    if not watch_dir.exists():
        log.error("Watch folder does not exist: %s", watch_dir)
        raise SystemExit(1)

    log.info("=== Downloads Auto-Organizer started ===")
    log.info("Watching: %s", watch_dir)

    # Handle files that are already there
    organize_existing(watch_dir)

    # Start the live watcher
    handler = DownloadsHandler(watch_dir)
    observer = Observer()
    observer.schedule(handler, str(watch_dir), recursive=False)
    observer.start()
    log.info("Watcher active. Press Ctrl+C to stop.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log.info("Stopping …")
    finally:
        observer.stop()
        observer.join()
        log.info("Organizer stopped.")


if __name__ == "__main__":
    main()
