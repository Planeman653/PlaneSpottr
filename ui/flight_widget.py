from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QGridLayout,
)
from PyQt6.QtGui import QColor, QFont, QPalette, QBrush
from PyQt6.QtCore import Qt


class FlightWidget(QFrame):
    """Widget to display flight information."""

    STATUS_COLORS = {
        "UNKNOWN": QColor(128, 128, 128),     # Gray
        "SCHEDULED": QColor(50, 100, 255),    # Blue
        "BOARDING": QColor(100, 180, 255),    # Light blue
        "EN ROUTE": QColor(50, 200, 100),     # Green
        "LANDED": QColor(50, 200, 100),       # Green
        "DELAYED": QColor(255, 150, 50),      # Orange
        "CANCELLED": QColor(255, 50, 50),     # Red
        "MISSED": QColor(255, 50, 50),        # Red
    }

    def __init__(self, flight, parent=None):
        super().__init__(parent)
        self.flight = flight
        self._setup_ui()
        self._update_display()

    def _setup_ui(self):
        """Set up the widget UI."""
        self.setLineWidth(1)
        self.setStyleSheet(self._get_style_sheet())

        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        # Top row: Flight number and status
        top_layout = QHBoxLayout()

        # Flight number label
        flight_label = QLabel(f"{self.flight.airline_code}{self.flight.flight_number}")
        flight_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        flight_label.setStyleSheet("color: white;")
        top_layout.addWidget(flight_label)

        # Status label
        status_label = QLabel(self._format_status(self.flight.status))
        status_color = self.STATUS_COLORS.get(self.flight.status, QColor(200, 200, 200))
        status_label.setStyleSheet(f"color: {status_color.name()}; font-weight: bold;")
        top_layout.addWidget(status_label)

        # Origin/destination
        if self.flight.origin_airport and self.flight.destination_airport:
            route_layout = QHBoxLayout()
            origin = QLabel(f"→ {self.flight.origin_airport}")
            origin.setStyleSheet("font-size: 10pt; color: #aaa;")
            dest = QLabel(f"→ {self.flight.destination_airport}")
            dest.setStyleSheet("font-size: 10pt; color: #aaa;")
            route_layout.addWidget(origin)
            route_layout.addWidget(dest)
            top_layout.addStretch()
            top_layout.addLayout(route_layout)

        layout.addLayout(top_layout)

        # Grid for flight details
        grid_layout = QGridLayout()

        # Row 1: Position
        pos_layout = QHBoxLayout()
        pos_label = QLabel(f"Lat: {self.flight.latitude:.4f}, Lon: {self.flight.longitude:.4f}")
        pos_label.setStyleSheet("font-size: 8pt; color: #888;")
        pos_layout.addWidget(pos_label)
        pos_layout.addStretch()
        grid_layout.addLayout(pos_layout, 0, 0)

        # Row 2: Speed and Altitude
        speed_layout = QHBoxLayout()
        speed_label = QLabel(f"Speed: {self.flight.ground_speed:.0f} kn")
        speed_label.setStyleSheet("font-size: 10pt;")
        speed_layout.addWidget(speed_label)

        alt_label = QLabel(f"Alt: {self.flight.altitude:,} ft")
        alt_label.setStyleSheet("font-size: 10pt;")
        speed_layout.addWidget(alt_label)

        speed_layout.addStretch()
        grid_layout.addLayout(speed_layout, 0, 1)

        # Row 3: ETA
        eta_layout = QHBoxLayout()
        eta_label = QLabel(f"ETA: {self.flight.scheduled_arrival.strftime('%H:%M:%S')}")
        eta_label.setStyleSheet("font-size: 10pt; font-weight: bold; color: #fff;")
        eta_layout.addWidget(eta_label)
        eta_layout.addStretch()
        grid_layout.addLayout(eta_layout, 0, 2)

        # Row 4: Delay
        delay_layout = QHBoxLayout()
        delay_label = QLabel(f"Delay: {self.flight.delay_minutes} min")
        delay_label.setStyleSheet(self._get_delay_style(self.flight.delay_minutes))
        delay_layout.addWidget(delay_label)
        delay_layout.addStretch()
        grid_layout.addLayout(delay_layout, 0, 3)

        layout.addLayout(grid_layout)

        self.setLayout(layout)

    def _get_style_sheet(self) -> str:
        """Get the widget's style sheet."""
        return """
            QFrame {
                background-color: rgba(40, 40, 45, 0.9);
                border: 2px solid #3a3a40;
                border-radius: 8px;
            }
            QLabel {
                background-color: transparent;
            }
        """

    def _get_delay_style(self, minutes: int) -> str:
        """Get style for delay label."""
        if minutes > 15:
            return "color: #ff5555; font-weight: bold;"
        elif minutes > 0:
            return "color: #ffaa55;"
        return "color: #55ff55;"

    def _format_status(self, status: str) -> str:
        """Format status for display."""
        status_map = {
            "UNKNOWN": "Status Unknown",
            "SCHEDULED": "On Schedule",
            "BOARDING": "Boarding",
            "EN ROUTE": "In Flight",
            "LANDED": "Landed",
            "DELAYED": "Delayed",
            "CANCELLED": "Cancelled",
            "MISSED": "Missed",
        }
        return status_map.get(status, status)

    def update_flight(self, flight: "Flight"):
        """Update the widget with new flight data."""
        self.flight = flight
        self._update_display()

    def _update_display(self):
        """Update widget display with current flight data."""
        # Update flight number
        flight_label = self.findChild(QLabel, None)  # Get first child with "flight" in text
        if flight_label:
            flight_label.setText(f"{self.flight.airline_code}{self.flight.flight_number}")

        # Update status
        status_label = self.findChild(QLabel, None)  # Get status label
        if status_label and "flight number" in flight_label.text():
            status_label.setText(self._format_status(self.flight.status))

        # Rebuild if significant changes
        if flight.flight_number != self.flight.flight_number:
            self._setup_ui()
