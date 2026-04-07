import requests
import os
from datetime import datetime, timedelta
from typing import Optional
import time
import re


class FlightAwareAPI:
    """Client for FlightAware Flight Tracker API with rate limiting and caching."""

    BASE_URL = "https://www.flightaware.com/hubs/ANY/dest"
    BASE_INFO_URL = "https://flightaware.com/API/flightaware_api.php"
    POSITION_URL = "https://www.flightaware.com/API/FlightAwareAPI.php"

    # Free tier: 100 requests/minute
    MAX_REQUESTS_PER_MINUTE = 100
    CACHE_DURATION = timedelta(minutes=5)

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.request_count = 0
        self.last_request_time = 0
        self._create_cache_dir()

    def _create_cache_dir(self):
        """Create cache directory if it doesn't exist."""
        cache_dir = os.path.join(os.path.expanduser("~"), ".planspottr_cache")
        os.makedirs(cache_dir, exist_ok=True)

    def _get_request_headers(self) -> dict:
        """Get authentication headers for API requests."""
        return {
            "Authorization": f"APIKey {self.api_key}",
            "User-Agent": "PlaneSpottr/1.0"
        }

    def _check_rate_limit(self):
        """Check and enforce rate limits."""
        now = time.time()
        one_minute_ago = now - 60

        # Reset counter if outside the last minute
        if now - self.last_request_time >= 60:
            self.request_count = 0

        # Wait if rate limit exceeded
        if self.request_count >= self.MAX_REQUESTS_PER_MINUTE:
            wait_time = self._calculate_wait_time()
            if wait_time > 0:
                print(f"Rate limit exceeded. Waiting {wait_time:.1f}s...")
                time.sleep(wait_time)
                self.request_count = 0
                self.last_request_time = time.time()

    def _calculate_wait_time(self) -> float:
        """Calculate wait time to next allowed request."""
        one_minute_ago = self.last_request_time - 60
        if self.request_count < self.MAX_REQUESTS_PER_MINUTE:
            return 0.0
        return one_minute_ago - self.last_request_time

    def _make_request(self, url: str, params: dict) -> Optional[dict]:
        """Make API request with rate limiting."""
        self._check_rate_limit()

        try:
            response = requests.get(url, params=params, headers=self._get_request_headers(), timeout=30)

            if response.status_code == 200:
                self.request_count += 1
                self.last_request_time = time.time()
                return response.json()
            else:
                print(f"API Error {response.status_code}: {response.text[:100]}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def get_flight_info(self, flight_number: str, airline: str) -> Optional[dict]:
        """
        Get flight information including status, schedule, and position.

        Args:
            flight_number: Flight number (e.g., "AA123")
            airline: IATA airline code (e.g., "AA", "DL")

        Returns:
            Flight info dictionary or None if failed
        """
        # Decode flight number to get actual flight ID
        flight_id = self._decode_flight_number(flight_number, airline)

        if not flight_id:
            return None

        url = f"{self.BASE_INFO_URL}?type=destination&flightId={flight_id}"
        data = self._make_request(url, {})

        if data and "response" in data:
            return data["response"]
        return None

    def get_nearby_flights(self, latitude: float, longitude: float,
                          radius_miles: float = 50) -> list:
        """
        Get flights within a radius of the given coordinates.

        Args:
            latitude: Latitude coordinate
            longitude: Longitude coordinate
            radius_miles: Search radius in miles

        Returns:
            List of flight info dictionaries
        """
        url = f"{self.BASE_URL}/{round(latitude, 1)}/{round(longitude, 1)}/{radius_miles}"
        data = self._make_request(url, {})

        if data and "response" in data and "flightData" in data["response"]:
            return data["response"]["flightData"]
        return []

    def get_flight_position(self, flight_number: str, airline: str) -> Optional[dict]:
        """
        Get current position for a specific flight.

        Args:
            flight_number: Flight number
            airline: IATA airline code

        Returns:
            Position dictionary with lat/lon or None
        """
        flight_id = self._decode_flight_number(flight_number, airline)

        if not flight_id:
            return None

        url = f"{self.POSITION_URL}?flightId={flight_id}"
        data = self._make_request(url, {})

        if data and "response" in data:
            return data["response"]
        return None

    def decode_waypoint(self, latitude: float, longitude: float) -> Optional[str]:
        """
        Decode ICAO location identifier from coordinates.

        Args:
            latitude: Latitude
            longitude: Longitude

        Returns:
            ICAO identifier or None
        """
        url = f"{self.POSITION_URL}?lat={latitude}&lon={longitude}&type=waypoint"
        data = self._make_request(url, {})

        if data and "response" in data and data["response"]:
            return data["response"][0]
        return None

    def _decode_flight_number(self, flight_number: str, airline: str) -> Optional[str]:
        """
        Convert flight number to flight ID for API requests.

        Args:
            flight_number: The flight number (e.g., "AA123")
            airline: IATA code (e.g., "AA")

        Returns:
            Flight ID or None
        """
        # Try exact match first
        params = {
            "type": "exact",
            "flightId": f"{airline.upper()}{flight_number}"
        }
        data = self._make_request(self.BASE_INFO_URL, params)

        if data and "response" in data and "data" in data["response"]:
            return data["response"]["data"][0]

        # Try as departure
        params = {
            "type": "depart",
            "airlineIATA": airline.upper(),
            "flightNumber": flight_number
        }
        data = self._make_request(self.BASE_INFO_URL, params)

        if data and "response" in data and "data" in data["response"]:
            return data["response"]["data"][0]

        return None


def main():
    """Test the API client."""
    api_key = os.getenv("FLIGHTAWARE_API_KEY", "test")

    if not api_key or api_key.startswith("your_api_key_here"):
        print("Please set FLIGHTAWARE_API_KEY in your .env file")
        return

    api = FlightAwareAPI(api_key)

    # Test getting nearby flights
    flights = api.get_nearby_flights(40.7128, -74.0060, radius_miles=50)
    print(f"Found {len(flights)} nearby flights")

    # Show first flight
    if flights:
        first = flights[0]
        print(f"\nFlight: {first['flights'][0]['flight'].get('flight', {}).get('flightNumber', '')} "
              f"{first['flights'][0]['flight'].get('airline', {}).get('iataCode', '')}")
        print(f"Status: {first['flights'][0]['flight'].get('statusDisplay', 'Unknown')}")
        print(f"Airport: {first['airportOut'].get('airport', {}).get('name', 'Unknown')}")


if __name__ == "__main__":
    main()
