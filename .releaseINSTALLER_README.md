# PlaneSpottr - Installer

## Quick Start

### Build the .exe

Run this command to create the standalone executable:

```bash
build.bat
```

Or manually:

```bash
pyinstaller --onefile --windowed --name=PlaneSpottr main.py
```

### Output Files

After building, you'll find:
- `dist/PlaneSpottr.exe` - The standalone executable (no Python needed!)
- `dist/README.md` - User documentation
- `dist/.env.example` - API key template

## Files Created

| File | Description |
|------|-------------|
| `build.bat` | Builds the standalone .exe file |
| `create_exe.bat` | Alternative build script |
| `PlaneSpottr.spec` | PyInstaller spec file |
| `build_nsis.bat` | Creates installer with NSIS |
| `build_installer.bat` | Creates MSi installer |
| `README_installer.md` | Installer documentation |
| `USER_GUIDE.md` | User guide for end users |

## How to Use

### For Developers

1. Make sure dependencies are installed:
   ```bash
   pip install pyinstaller
   ```

2. Run the build:
   ```bash
   build.bat
   ```

3. The .exe will be in `dist/PlaneSpottr.exe`

### For End Users

1. Copy `PlaneSpottr.exe` to your desired location
2. Create a `.env` file with your API key
3. Double-click `PlaneSpottr.exe`

## What's Included

The .exe includes:
- All Python dependencies (PyQt6, requests, etc.)
- No Python installation required
- Dark theme
- Real-time flight tracking
- Configurable settings

## Requirements

### For Building
- Python 3.8+
- PyInstaller
- Virtual environment

### For Running
- Windows 7 or later
- No Python required
- Internet connection (for API)

## API Key Setup

Before running the app, create a `.env` file:

```
FLIGHTAWARE_API_KEY=your_api_key_here
```

Get your free API key at: https://flightaware.com/help/development/get-key

## License

MIT License
