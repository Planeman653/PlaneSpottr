# PlaneSpottr

Flight tracker desktop application that displays real-time flight information from the FlightAware API.

## Latest Updates (v0.1.2)

- ✅ Fixed `pynavdata` → `onavdata` dependency issue
- ✅ Fixed `QSettings` import issue for PyQt6 compatibility  
- ✅ Fixed `flightaware` module import path
- ✅ Added setup dialog for API key on first run

## Features

- Displays nearby flights within a configurable radius
- Real-time flight status updates (en route, delayed, landed, etc.)
- Live flight position, altitude, and ground speed
- Configurable search radius and refresh interval
- Dark theme for comfortable viewing

## Getting Started

### ⚡ Quick Start (5 minutes)

1. **Get a free API key** from [FlightAware Developer](https://flightaware.com/help/development/get-key)
2. **Download** `PlaneSpottr.exe` (from releases or build locally)
3. **Run** `PlaneSpottr.exe`
4. **Enter your API key** in the setup dialog
5. **Track flights!**

## Build the .exe (Developer)

```bash
# Install dependencies
pip install -r requirements.txt

# Build the executable
python build.py
# OR manually:
pyinstaller --onefile --windowed --name=PlaneSpottr --add-data ".env.example;." main.py
```

Output: `dist/PlaneSpottr.exe` (~8-12 MB)

## Usage

### First Time - Setup Dialog

1. **Download and run** `PlaneSpottr.exe`
2. **On first run**, a setup dialog will appear
3. **Enter your FlightAware API key** (see [Getting Started](#getting-started-quick-start-5-minutes) above)
4. Click "Save and Start"
5. **The key is saved** for all future runs - no need to re-enter!

### After Setup

- **Ctrl+R**: Refresh flight list
- **Ctrl+,**: Open settings dialog  
- Adjust search radius from the toolbar
- Flights auto-refresh based on settings interval

## Troubleshooting

### "No module named 'PyQt6'" Error

This means the app needs its dependencies installed. Rebuild with:

```bash
pip install pyinstaller PyQt6 requests pandas numpy onavdata
python build.py
```

### Need API Key?

1. Get free key from [FlightAware Developer](https://flightaware.com/help/development/get-key)
2. First run will show setup dialog
3. Enter your API key and click "Save"

### API Key Not Working

- Verify your API key is correct in `.env`
- Check there are no extra spaces in the key
- The key should look like: `FLIGHTAWARE_API_KEY=1234567890abcdef...`

### App Won't Start

- Check that `.env` file exists (created automatically on first run)
- Verify your API key is valid
- Make sure you're in the folder with `PlaneSpottr.exe`

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
├── build.py           # Build script for .exe
├── build.bat          # Windows batch build script
├── build_installer.bat # Create installer
├── main.py            # Application entry point (prompts for API key)
├── requirements.txt   # Python dependencies
├── .env.example       # API key template
├── .env               # YOUR API KEY (auto-created on first run)
├── api/
│   └── flightaware.py # FlightAware API client
├── models/
│   └── flight.py      # Flight data model
└── ui/
    ├── flight_widget.py
    └── main_window.py
```

## Distribution Files

| File | Size | Description |
|------|------|-------------|
| `PlaneSpottr.exe` | 8-12 MB | Standalone executable with setup dialog |
| `README.md` | - | This documentation |
| `.env.example` | - | API key template |
| `LICENSE` | - | MIT License |

## How to Share the App

1. **Build** the executable (`python build.py`)
2. **Copy** `PlaneSpottr.exe` to a USB drive or cloud folder
3. **Share** the file - no Python installation needed!

## FAQ

**Q: Can I run the app without installing Python?**  
A: Yes! Use `PlaneSpottr.exe` - it includes all Python dependencies.

**Q: What is an .env file?**  
A: It's automatically created on first run to store your API key.

**Q: Why do I need an API key?**  
A: FlightAware requires authentication. Get a free key in 30 seconds.

**Q: The app won't start. What should I do?**  
A: First run will show a setup dialog. Enter your API key and click "Save".

**Q: Can I share the app with friends?**  
A: Yes! Just share the `.exe` file. Each user needs their own API key.

## License

MIT
