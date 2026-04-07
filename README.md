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

## Usage

- **Ctrl+R**: Refresh flight list
- **Ctrl+,**: Open settings dialog
- Adjust search radius from the toolbar
- Flights auto-refresh based on settings interval

## Project Structure

```
PlaneSpottr/
├── main.py              # Application entry point
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
├── api/
│   ├── __init__.py
│   └── flightaware.py   # FlightAware API client
├── models/
│   ├── __init__.py
│   └── flight.py        # Flight data model
└── ui/
    ├── __init__.py
    ├── flight_widget.py # Flight display widget
    └── main_window.py   # Main application window
```

## API Rate Limiting

The application implements rate limiting to stay within the FlightAware free tier:
- Maximum 100 requests/minute
- 5-minute cache for API responses
- Automatic retry with exponential backoff

## License

MIT
