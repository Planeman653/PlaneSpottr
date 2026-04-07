# PlaneSpottr v0.1.2

## What's New

### Setup Dialog (New!)
The app now prompts for your API key on first run:
1. Run `PlaneSpottr.exe`
2. Setup dialog appears automatically
3. Enter your FlightAware API key
4. Click "Save and Start"
5. The key is saved - no need to re-enter!

### Bug Fixes
- Fixed `pynavdata` → `onavdata` dependency
- Fixed `QSettings` import for PyQt6 compatibility
- Fixed `flightaware` module import path

### Features
- Setup dialog on first run
- Automatic API key saving
- Clean, modern setup UI with help links

## Features

- **Flight Tracking**: View real-time flights within configurable radius
- **Auto-refresh**: Automatic flight updates (configurable)
- **Settings**: Ctrl+, to open settings dialog
- **Refresh**: Ctrl+R to manually refresh flights
- **Dark Theme**: Comfortable viewing

## Standalone .exe Support

No Python installation required! Just double-click `PlaneSpottr.exe` to run.

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+R   | Refresh flight list |
| Ctrl+,   | Open settings |

## Installation

1. Run `PlaneSpottr.exe`
2. Setup dialog will appear
3. Enter your FlightAware API key
4. Click "Save and Start"
5. The key is saved for all future runs

## Get API Key

Get your free API key at: https://flightaware.com/help/development/get-key

**Takes only 30 seconds!**

## Requirements

**For running:**
- Windows 7 or later
- No Python required
- FlightAware API key (free)

## How to Build

```bash
python build.py
```

Or manually:
```bash
pyinstaller --clean --onefile --windowed --name=PlaneSpottr main.py
```

## Files Included

- `PlaneSpottr.exe` - Standalone executable
- `README.md` - Documentation
- `.env.example` - API key template
- `LICENSE` - MIT License
