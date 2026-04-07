# PlaneSpottr - User Guide

## Getting Started

### First Time Setup

1. **Copy API Key File**
   - Copy `.env.example` to `.env`
   - Add your FlightAware API key:
     ```
     FLIGHTAWARE_API_KEY=your_api_key_here
     ```
   - Get a free API key at https://flightaware.com/help/development/get-key

2. **Run the App**
   - Double-click `PlaneSpottr.exe`
   - The app will launch with a dark theme
   - Configure settings via Ctrl+,

### Controls

- **Ctrl+R**: Refresh flight list
- **Ctrl+,**: Open settings dialog
- **Adjust radius**: Use toolbar to change search radius
- **Auto-refresh**: Flights update based on settings interval

## Features

- Real-time flight tracking from FlightAware API
- Dark theme for comfortable viewing
- Live position, altitude, and ground speed
- Configurable search radius
- Rate limiting to stay within free tier limits

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+R   | Refresh flight list |
| Ctrl+,   | Open settings |

## Settings

Access settings with Ctrl+, to configure:
- Search radius
- Refresh interval
- Other preferences

## Troubleshooting

### App won't start
- Make sure `.env` file exists in the same folder as `PlaneSpottr.exe`
- Verify API key is set correctly

### Missing DLL errors
- Run `build.bat` again to rebuild the executable

### API rate limit
- The app automatically implements rate limiting
- Automatic retry with exponential backoff

## Technical Details

- Python 3.8+ (not required - included in installer)
- PyQt6-based interface
- FlightAware API integration
- Rate-limited to 100 requests/minute

## Support

For issues or questions:
1. Check this guide
2. Verify `.env` file configuration
3. Review FlightAware API documentation
