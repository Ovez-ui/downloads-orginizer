# 📁 Downloads Auto-Organizer

A lightweight Python script that **watches your Downloads folder** and automatically moves files into tidy subfolders based on their extension — the moment they land.

```
Downloads/
├── report.pdf        →   Documents/report.pdf
├── photo.png         →   Images/photo.png
├── setup.exe         →   Executables/setup.exe
├── archive.zip       →   Archives/archive.zip
└── song.mp3          →   Audio/song.mp3
```

---

## ✨ Features

- **Real-time watching** — uses [watchdog](https://github.com/gorakhargosh/watchdog) to react instantly to new files
- **Handles existing files** — organizes whatever is already in the folder on startup
- **Collision-safe** — appends `_1`, `_2`, … if a file with the same name already exists
- **Temp-file aware** — ignores `.crdownload`, `.part`, `.tmp` files while they're still downloading
- **Fully configurable** — all rules live in `config.py`; no code changes needed for customisation
- **Cross-platform** — works on Windows, macOS, and Linux

---

## 🗂️ Default folder map

| Extension(s) | Subfolder |
|---|---|
| `pdf`, `docx`, `txt`, `md`, … | `Documents` |
| `xls`, `xlsx`, `csv`, … | `Spreadsheets` |
| `ppt`, `pptx`, `key`, … | `Presentations` |
| `jpg`, `png`, `gif`, `svg`, … | `Images` |
| `mp4`, `mkv`, `avi`, … | `Videos` |
| `mp3`, `wav`, `flac`, … | `Audio` |
| `zip`, `rar`, `7z`, `tar`, … | `Archives` |
| `py`, `js`, `html`, `json`, … | `Code` |
| `exe`, `msi`, `apk`, … | `Executables` |
| `ttf`, `otf`, `woff`, … | `Fonts` |
| `epub`, `mobi`, `azw3`, … | `eBooks` |
| *(anything else)* | `Others` |

---

## 🚀 Quick start

### 1. Clone the repo

```bash
git clone https://github.com/Ovez-ui/downloads-organizer.git
cd downloads-organizer
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run

```bash
python organizer.py
```

The script will:
1. Scan and organize all existing files in your Downloads folder
2. Keep watching for new files until you press **Ctrl+C**

---

## ⚙️ Configuration

Open **`config.py`** to customise behaviour:

```python
# Change the watched folder
WATCH_FOLDER = "/path/to/your/folder"
# Or set via environment variable:
#   ORGANIZER_WATCH="/path/to/folder" python organizer.py

# Change log verbosity: DEBUG | INFO | WARNING | ERROR
LOG_LEVEL = "INFO"

# Add or remap extensions
EXTENSION_MAP = {
    "pdf":  "Documents",
    "zip":  "Archives",
    "psd":  "Design",       # ← add your own
    # ...
}

# Folder for unrecognised extensions
UNKNOWN_FOLDER = "Others"
```

You can also use environment variables without editing the file:

```bash
ORGANIZER_WATCH="D:\Downloads" ORGANIZER_LOG_LEVEL=DEBUG python organizer.py
```

---

## 🔄 Run on startup (optional)

### Windows — Task Scheduler

1. Open **Task Scheduler** → *Create Basic Task*
2. Trigger: **At log on**
3. Action: start `pythonw.exe` with argument `C:\path\to\organizer.py`

### macOS — launchd

Create `~/Library/LaunchAgents/com.organizer.downloads.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>             <string>com.organizer.downloads</string>
  <key>ProgramArguments</key>
  <array>
    <string>/path/to/.venv/bin/python</string>
    <string>/path/to/organizer.py</string>
  </array>
  <key>RunAtLoad</key>         <true/>
  <key>KeepAlive</key>         <true/>
</dict>
</plist>
```

Then load it:
```bash
launchctl load ~/Library/LaunchAgents/com.organizer.downloads.plist
```

### Linux — systemd user service

Create `~/.config/systemd/user/downloads-organizer.service`:

```ini
[Unit]
Description=Downloads Auto-Organizer

[Service]
ExecStart=/path/to/.venv/bin/python /path/to/organizer.py
Restart=on-failure

[Install]
WantedBy=default.target
```

```bash
systemctl --user enable --now downloads-organizer
```

---

## 📋 Requirements

- Python 3.10+
- [watchdog](https://github.com/gorakhargosh/watchdog) ≥ 4.0

---

## 📄 License

MIT — do whatever you like with it.
