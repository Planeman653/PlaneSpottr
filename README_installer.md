# PlaneSpottr Installer Guide

## Building the Executable

### Quick Build

Run the following command to create the .exe file:

```bash
create_exe.bat
```

Or build manually with PyInstaller:

```bash
pyinstaller --clean --onefile --windowed --name=PlaneSpottr main.py
```

### Output

After building, you'll find:
- `dist/PlaneSpottr.exe` - The standalone executable
- `dist/README.md` - Documentation
- `dist/PlaneSpottrPortable` (if built as portable)

## Usage

### Running the App

1. **Double-click** `PlaneSpottr.exe`
2. Set your `FLIGHTAWARE_API_KEY` in `.env` file first
3. The app will launch with a dark theme

### Requirements for Users

The .exe includes all dependencies, so end users just need:
- Windows 7 or later
- No Python installation required

## Distribution

The installer is standalone and includes:
- All Python dependencies (PyQt6, requests, etc.)
- Application configuration
- Dark theme
- Real-time flight tracking

## API Key

Before running the app, copy `.env.example` to `.env` and add your FlightAware API key:

```
FLIGHTAWARE_API_KEY=your_api_key_here
```

Get a free API key at: https://flightaware.com/help/development/get-key

## Troubleshooting

- **App won't start**: Make sure .env file exists in the same directory
- **Missing DLL errors**: Run create_exe.bat again to rebuild
- **Dark theme not applying**: Windows compatibility mode may need to be disabled
