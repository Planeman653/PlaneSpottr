# PlaneSpottr

Flight tracker desktop application that displays real-time flight information from the FlightAware API.

## Latest Updates (v0.1.2)

- ✅ Fixed `pynavdata` → `onavdata` dependency issue
- ✅ Fixed `QSettings` import issue for PyQt6 compatibility
- ✅ Fixed `flightaware` module import path

## Features

- Displays nearby flights within a configurable radius
- Real-time flight status updates (en route, delayed, landed, etc.)
- Live flight position, altitude, and ground speed
- Configurable search radius and refresh interval
- Dark theme for comfortable viewing

## ⚠️ IMPORTANT: Setup Required Before Running

The app requires a FlightAware API key. Without it, you'll see:
```
ModuleNotFoundError: No module named 'PyQt6'
```

### Getting Your Free API Key (5 minutes)

1. Go to: **https://flightaware.com/help/development/get-key**
2. Click "Get Key" and complete the quick registration
3. Copy your API key (it's a long string of characters)

### Setting Up the API Key

**For the .exe Application:**

1. Copy `.env.example` to `.env`
   ```
   copy .env.example .env
   ```

2. Edit `.env` and add your API key:
   ```
   FLIGHTAWARE_API_KEY=your_actual_api_key_here
   ```

3. Run the app:
   ```
   PlaneSpottr.exe
   ```

**For Source Code:**

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create `.env` file with API key

3. Run:
   ```bash
   python main.py
   ```

## Build the .exe

```bash
# Install dependencies
pip install pyinstaller PyQt6

# Build the executable
pyinstaller --clean --onefile --windowed --name=PlaneSpottr main.py

# OR run the build script
build.bat
```

Output: `dist/PlaneSpottr.exe` (8.4 MB)

## Usage

- **Ctrl+R**: Refresh flight list
- **Ctrl+,**: Open settings dialog
- Adjust search radius from the toolbar
- Flights auto-refresh based on settings interval

## Troubleshooting

### "No module named 'PyQt6'" Error

This happens when the `.env` file is missing. Make sure:

1. The `.env` file exists in the same folder as `PlaneSpottr.exe`
2. Your API key is correctly set:
   ```
   FLIGHTAWARE_API_KEY=your_actual_api_key_here
   ```

### API Key Not Working

- Verify your API key is correct in `.env`
- Check there are no extra spaces in the key
- The key should look like: `FLIGHTAWARE_API_KEY=1234567890abcdef...`

### App Won't Start

- Check that `.env` file exists
- Verify your API key is valid
- Make sure you're in the folder with `PlaneSpottr.exe`

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
├── build.bat           # Build script
├── main.py             # Application entry point
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env.example        # Template - COPY TO .env
├── .env                # YOUR API KEY (edit this!)
├── api/
│   └── flightaware.py  # FlightAware API client
├── models/
│   └── flight.py       # Flight data model
└── ui/
    ├── flight_widget.py
    └── main_window.py
```

## Distribution Files

| File | Size | Description |
|------|------|-------------|
| `PlaneSpottr.exe` | 8.4 MB | Standalone executable |
| `README.md` | - | This documentation |
| `.env.example` | - | API key template |
| `LICENSE` | - | MIT License |
| `CHANGELOG.md` | - | Release notes |

## How to Share the App

1. Copy `PlaneSpottr.exe` to a USB drive or cloud folder
2. Share the `.env` template with users who need to set up their API key
3. Users just need to:
   - Copy `.env.example` to `.env`
   - Add their API key
   - Double-click to run

## FAQ

**Q: Can I run the app without installing Python?**  
A: Yes! Use `PlaneSpottr.exe` - it includes all Python dependencies.

**Q: What is an .env file?**  
A: It's a configuration file that stores your API key. Create it once and reuse.

**Q: Why do I need an API key?**  
A: FlightAware limits API access. The key identifies you for tracking flights.

**Q: The app won't start. What should I do?**  
A: Make sure the `.env` file exists and has your API key set correctly.

## License

MIT
