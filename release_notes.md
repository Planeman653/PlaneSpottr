# PlaneSpottr v0.0.0

## What's New

### Initial Release

**PlaneSpottr** is a flight tracking desktop application that displays real-time flight information from the FlightAware API.

### Features

- Real-time flight tracking for nearby flights
- Dark theme UI
- Configurable search radius and refresh interval
- Keyboard shortcuts (Ctrl+R, Ctrl+,:)
- Rate limiting to stay within FlightAware free tier

### Standalone .exe Support

No Python installation required! Just double-click `PlaneSpottr.exe` to run.

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+R   | Refresh flight list |
| Ctrl+,   | Open settings |

### How to Use

1. Download `PlaneSpottr.exe` from the releases page
2. Create a `.env` file with your FlightAware API key
3. Double-click to run

### How to Build

```bash
pyinstaller --clean --onefile --windowed --name=PlaneSpottr main.py
```

Or run `build.bat`

### Files Included

- `PlaneSpottr.exe` - Standalone executable
- `README.md` - Documentation
- `.env.example` - API key template
- `LICENSE` - MIT License
- `CHANGELOG.md` - Version history

## Requirements

**For building:**
- Python 3.8+
- PyInstaller

**For running:**
- Windows 7 or later
- No Python required

## Installation

1. Copy `.env.example` to `.env`
2. Add your FlightAware API key
3. Run `PlaneSpottr.exe`

## Get API Key

Get your free API key at: https://flightaware.com/help/development/get-key
