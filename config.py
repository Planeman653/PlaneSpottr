"""Configuration settings for PlaneSpottr."""

# Default values
DEFAULTS = {
    "search_radius": 50,       # miles
    "refresh_interval": 60,    # seconds
    "location": {
        "latitude": 40.7128,   # NYC
        "longitude": -74.0060,
    },
}

# API settings
API = {
    "base_url": "https://www.flightaware.com/hubs/ANY/dest",
    "max_requests_per_minute": 100,
    "cache_duration": 300,     # 5 minutes
}
