"""
config.py — Edit this file to customise the organizer behaviour.
"""

import os
from pathlib import Path

# ── Folder to watch ────────────────────────────────────────────────────────────
# Default: the current user's Downloads folder.
# Override with the ORGANIZER_WATCH env variable, e.g.:
#   ORGANIZER_WATCH="/mnt/data/Downloads" python organizer.py
WATCH_FOLDER: str = os.environ.get(
    "ORGANIZER_WATCH",
    str(Path.home() / "Downloads"),
)

# ── Logging verbosity ──────────────────────────────────────────────────────────
# Options: DEBUG | INFO | WARNING | ERROR
LOG_LEVEL: str = os.environ.get("ORGANIZER_LOG_LEVEL", "INFO")

# ── Fallback folder ────────────────────────────────────────────────────────────
# Files whose extension is not in EXTENSION_MAP land here.
UNKNOWN_FOLDER: str = "Others"

# ── Extension → subfolder map ──────────────────────────────────────────────────
# Keys are lowercase extensions WITHOUT the leading dot.
# Values are subfolder names that will be created inside WATCH_FOLDER.
EXTENSION_MAP: dict[str, str] = {
    # ── Documents ──────────────────────────────────────────────────────────────
    "pdf":   "Documents",
    "doc":   "Documents",
    "docx":  "Documents",
    "odt":   "Documents",
    "rtf":   "Documents",
    "txt":   "Documents",
    "md":    "Documents",
    "tex":   "Documents",
    "wps":   "Documents",

    # ── Spreadsheets ──────────────────────────────────────────────────────────
    "xls":   "Spreadsheets",
    "xlsx":  "Spreadsheets",
    "ods":   "Spreadsheets",
    "csv":   "Spreadsheets",
    "tsv":   "Spreadsheets",

    # ── Presentations ─────────────────────────────────────────────────────────
    "ppt":   "Presentations",
    "pptx":  "Presentations",
    "odp":   "Presentations",
    "key":   "Presentations",

    # ── Images ────────────────────────────────────────────────────────────────
    "jpg":   "Images",
    "jpeg":  "Images",
    "png":   "Images",
    "gif":   "Images",
    "bmp":   "Images",
    "svg":   "Images",
    "webp":  "Images",
    "ico":   "Images",
    "tiff":  "Images",
    "tif":   "Images",
    "heic":  "Images",
    "raw":   "Images",
    "cr2":   "Images",
    "nef":   "Images",

    # ── Videos ────────────────────────────────────────────────────────────────
    "mp4":   "Videos",
    "mkv":   "Videos",
    "avi":   "Videos",
    "mov":   "Videos",
    "wmv":   "Videos",
    "flv":   "Videos",
    "webm":  "Videos",
    "m4v":   "Videos",
    "3gp":   "Videos",
    "ts":    "Videos",

    # ── Audio ─────────────────────────────────────────────────────────────────
    "mp3":   "Audio",
    "wav":   "Audio",
    "flac":  "Audio",
    "aac":   "Audio",
    "ogg":   "Audio",
    "m4a":   "Audio",
    "wma":   "Audio",
    "opus":  "Audio",
    "aiff":  "Audio",

    # ── Archives ──────────────────────────────────────────────────────────────
    "zip":   "Archives",
    "rar":   "Archives",
    "7z":    "Archives",
    "tar":   "Archives",
    "gz":    "Archives",
    "bz2":   "Archives",
    "xz":    "Archives",
    "iso":   "Archives",
    "dmg":   "Archives",
    "pkg":   "Archives",
    "deb":   "Archives",
    "rpm":   "Archives",

    # ── Code & Scripts ────────────────────────────────────────────────────────
    "py":    "Code",
    "js":    "Code",
    "ts":    "Code",
    "jsx":   "Code",
    "tsx":   "Code",
    "html":  "Code",
    "css":   "Code",
    "scss":  "Code",
    "json":  "Code",
    "yaml":  "Code",
    "yml":   "Code",
    "xml":   "Code",
    "sql":   "Code",
    "sh":    "Code",
    "bat":   "Code",
    "ps1":   "Code",
    "java":  "Code",
    "c":     "Code",
    "cpp":   "Code",
    "h":     "Code",
    "rs":    "Code",
    "go":    "Code",
    "rb":    "Code",
    "php":   "Code",
    "swift": "Code",
    "kt":    "Code",
    "lua":   "Code",
    "toml":  "Code",
    "ini":   "Code",
    "env":   "Code",

    # ── Executables & Installers ──────────────────────────────────────────────
    "exe":   "Executables",
    "msi":   "Executables",
    "apk":   "Executables",
    "appimage": "Executables",

    # ── Fonts ─────────────────────────────────────────────────────────────────
    "ttf":   "Fonts",
    "otf":   "Fonts",
    "woff":  "Fonts",
    "woff2": "Fonts",

    # ── eBooks ────────────────────────────────────────────────────────────────
    "epub":  "eBooks",
    "mobi":  "eBooks",
    "azw":   "eBooks",
    "azw3":  "eBooks",
    "djvu":  "eBooks",
    "fb2":   "eBooks",
}
