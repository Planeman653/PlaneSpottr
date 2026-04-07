from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Flight:
    """Represents a flight with all relevant information."""

    flight_number: str
    airline_code: str
    airline_name: str = ""
    aircraft: str = ""
    status: str = "UNKNOWN"  # UNKNOWN, SCHEDULED, BOARDING, ENROUTE, LANDED, CANCELLED, MISSED
    scheduled_departure: datetime = field(default_factory=lambda: datetime.now())
    actual_departure: Optional[datetime] = None
    scheduled_arrival: datetime = field(default_factory=lambda: datetime.now())
    actual_arrival: Optional[datetime] = None
    latitude: float = 0.0
    longitude: float = 0.0
    altitude: int = 0  # feet
    ground_speed: float = 0.0  # knots
    heading: float = 0.0
    origin_airport: str = ""
    destination_airport: str = ""
    departure_delay: int = 0  # minutes
    arrival_delay: int = 0  # minutes
    eta: datetime = field(default_factory=lambda: datetime.now())
    etd: Optional[datetime] = None

    # Cached data from API response
    raw_data: dict = field(default_factory=dict)

    @classmethod
    def from_api_data(cls, response: dict) -> Optional["Flight"]:
        """Create Flight object from API response."""
        if not response or "response" not in response:
            return None

        flights = response["response"].get("data", [])
        if not flights:
            return None

        flight_data = flights[0]  # Get the first flight if multiple

        return cls(
            flight_number=flight_data.get("flight", {}).get("flightNumber", "UNKNOWN"),
            airline_code=flight_data.get("airline", {}).get("iataCode", "??"),
            airline_name=flight_data.get("airline", {}).get("name", ""),
            aircraft=flight_data.get("aircraft", {}).get("tail", ""),
            status=flight_data.get("statusDisplay", "UNKNOWN"),
            scheduled_departure=cls._parse_datetime(
                flight_data.get("eta", {}).get("etaDeparture")
            ),
            actual_departure=cls._parse_datetime(
                flight_data.get("eta", {}).get("actualDeparture")
            ),
            scheduled_arrival=cls._parse_datetime(
                flight_data.get("eta", {}).get("etaArrival")
            ),
            actual_arrival=cls._parse_datetime(
                flight_data.get("eta", {}).get("actualArrival")
            ),
            latitude=float(flight_data.get("latitude", 0)),
            longitude=float(flight_data.get("longitude", 0)),
            altitude=int(flight_data.get("altitude", 0)),
            ground_speed=float(flight_data.get("groundSpeed", 0)),
            heading=float(flight_data.get("heading", 0)),
            origin_airport=flight_data.get("airportOut", {}).get("airport", {}).get("name", ""),
            destination_airport=flight_data.get("airportIn", {}).get("airport", {}).get("name", ""),
            departure_delay=int(flight_data.get("departureDelay", 0)),
            arrival_delay=int(flight_data.get("arrivalDelay", 0)),
            etd=cls._parse_datetime(flight_data.get("eta", {}).get("etaDeparture")),
        )

    @classmethod
    def from_position_data(cls, flight_number: str, airline: str,
                           position_data: dict) -> "Flight":
        """Create Flight object from position-only API data."""
        return cls(
            flight_number=flight_number,
            airline_code=airline.upper(),
            status=position_data.get("status", "UNKNOWN"),
            latitude=float(position_data.get("latitude", 0)),
            longitude=float(position_data.get("longitude", 0)),
            altitude=int(position_data.get("altitude", 0)),
            ground_speed=float(position_data.get("groundSpeed", 0)),
            heading=float(position_data.get("heading", 0)),
            etd=cls._parse_datetime(position_data.get("eta", "ETD")),
        )

    @classmethod
    def _parse_datetime(cls, value: str) -> datetime:
        """Parse datetime string from API."""
        if not value:
            return datetime.now()
        try:
            # Format: 2024-04-07T01:00:00.000
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
            return dt.replace(tzinfo=None)
        except (ValueError, AttributeError):
            return datetime.now()

    def __str__(self) -> str:
        return f"{self.airline_code}{self.flight_number}"

    def __repr__(self) -> str:
        return f"Flight({self.airline_code}{self.flight_number})"

    @property
    def is_delayed(self) -> bool:
        """Check if flight is delayed."""
        if self.departure_delay > 0:
            return True
        return self.scheduled_departure > datetime.now()

    @property
    def delay_minutes(self) -> int:
        """Get delay in minutes."""
        if self.departure_delay > 0:
            return self.departure_delay
        if self.scheduled_departure > datetime.now():
            return int((self.scheduled_departure - datetime.now()).total_seconds() / 60)
        return 0

    def is_en_route(self) -> bool:
        """Check if flight is currently en route."""
        return self.status in ("EN ROUTE", "SCHEDULED")

    def is_landed(self) -> bool:
        """Check if flight has landed."""
        return self.status in ("LANDED", "LANDED AND GATE OPEN", "LANDED AND PULLED IN")
