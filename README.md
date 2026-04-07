# PlaneSpottr

Flight tracker desktop application that displays real-time flight information from the FlightAware API.

## Features

- Displays nearby flights within a configurable radius
- Real-time flight status updates (en route, delayed, landed, etc.)
- Live flight position, altitude, and ground speed
- Configurable search radius and refresh interval
- Dark theme for comfortable viewing

## Requirements

- Python 3.8+
- PyQt6

## Installation

### From Source

1. **Clone or create the project**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key:**
   - Copy `.env.example` to `.env`
   - Add your FlightAware API key:
     ```
     FLIGHTAWARE_API_KEY=your_api_key_here
     ```
   - Get your free API key at: https://flightaware.com/help/development/get-key

4. **Run the application:**
   ```bash
   python main.py
   ```

### Standalone .exe (Recommended for Distribution)

Build a standalone executable that requires no Python installation:

1. **Build the executable:**
   ```bash
   pyinstaller --clean --onefile --windowed --name=PlaneSpottr main.py
   ```
   Or run the build script:
   ```bash
   build.bat
   ```

2. **The result:** `dist/PlaneSpottr.exe`

   - No Python required to run
   - Includes all dependencies
   - Ready to distribute to any Windows user

3. **Use the app:**
   - Double-click `PlaneSpottr.exe`
   - Create a `.env` file with your API key in the same folder
   - Run the application

## Usage

- **Ctrl+R**: Refresh flight list
- **Ctrl+,**: Open settings dialog
- Adjust search radius from the toolbar
- Flights auto-refresh based on settings interval

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+R   | Refresh flight list |
| Ctrl+,   | Open settings |

## Settings

Access settings with `Ctrl+,` to configure:
- Search radius
- Refresh interval
- Other preferences

## API Rate Limiting

The application implements rate limiting to stay within the FlightAware free tier:
- Maximum 100 requests/minute
- 5-minute cache for API responses
- Automatic retry with exponential backoff

## Project Structure

```
PlaneSpottr/
├── build.bat           # Build script for .exe
├── main.py             # Application entry point
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
├── api/
│   ├── __init__.py
│   └── flightaware.py  # FlightAware API client
├── models/
│   ├── __init__.py
│   └── flight.py       # Flight data model
└── ui/
    ├── __init__.py
    ├── flight_widget.py
    └── main_window.py
```

## Distribution

### Output Files

| File | Description |
|------|-------------|
| `dist/PlaneSpottr.exe` | Standalone executable |
| `dist/README.md` | Documentation |
| `dist/.env.example` | API key template |

### Requirements

**For building:**
- Python 3.8+
- PyInstaller (`pip install pyinstaller`)

**For running:**
- Windows 7 or later
- No Python required (included in .exe)

## License

MIT
