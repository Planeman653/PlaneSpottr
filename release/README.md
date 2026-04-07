# PlaneSpottr

Flight tracker desktop application that displays real-time flight information from the FlightAware API.

## Features

- Displays nearby flights within a configurable radius
- Real-time flight status updates (en route, delayed, landed, etc.)
- Live flight position, altitude, and ground speed
- Configurable search radius and refresh interval
- Dark theme for comfortable viewing

## ⚠️ IMPORTANT: Before First Run

You MUST create a `.env` file with your FlightAware API key!

### Step 1: Get a Free API Key

1. Go to: **https://flightaware.com/help/development/get-key**
2. Click "Get Key" and complete the registration
3. Copy your API key

### Step 2: Set Up API Key

**For Source Code:**

```bash
# Copy the template file
copy .env.example .env

# Edit .env and add your API key
notepad .env

# Replace with your actual key
FLIGHTAWARE_API_KEY=your_actual_api_key_here
```

**For the .exe Application:**

1. Copy `.env.example` to `.env` in the same folder as `PlaneSpottr.exe`
2. Edit `.env` and add your API key
3. Double-click `PlaneSpottr.exe`

### Step 3: Run the Application

```bash
python main.py
# OR
PlaneSpottr.exe
```

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
   - Add your FlightAware API key

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

3. **To use:**
   - Create a `.env` file with your API key
   - Double-click `PlaneSpottr.exe`

## Usage

- **Ctrl+R**: Refresh flight list
- **Ctrl+,**: Open settings dialog
- Adjust search radius from the toolbar
- Flights auto-refresh based on settings interval

## Troubleshooting

### "No module named 'PyQt6'" Error

Make sure you have:
1. Installed dependencies: `pip install -r requirements.txt`
2. PyQt6 is in your Python environment

### API Key Not Working

- Verify your API key is correct in `.env`
- Check that there are no extra spaces in the key
- The key format is: `FLIGHTAWARE_API_KEY=xxxxxxxxxxxxxxxx`

### App Won't Start

- Check that `.env` file exists in the same folder
- Verify your API key is valid

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
├── .env.example        # Environment template - COPY TO .env
├── .env                # YOUR API KEY HERE (DO NOT SHARE)
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
|------|------|
| `dist/PlaneSpottr.exe` | Standalone executable |
| `dist/README.md` | This documentation |
| `dist/.env.example` | API key template |
| `dist/CHANGELOG.md` | Release notes |

### Requirements

**For building:**
- Python 3.8+
- PyInstaller

**For running:**
- Windows 7 or later
- No Python required (included in .exe)
- `.env` file with API key (required before first run)

## FAQ

**Q: What is an .env file?**  
A: It's a configuration file that stores your API key. The app reads `FLIGHTAWARE_API_KEY` from it.

**Q: Why do I need an API key?**  
A: The FlightAware API is rate-limited. The key identifies you and allows the app to track flights.

**Q: Can I share the .exe without the API key?**  
A: The .exe doesn't include an API key (for security). Users need to create their own `.env` file.

## License

MIT
