import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QFrame, QGridLayout, QToolBar, QStatusBar, QComboBox,
    QSettings, QDialog, QFormLayout, QLineEdit, QSpinBox,
)
from PyQt6.QtGui import QAction, QKeySequence, QFont, QPixmap
from PyQt6.QtCore import Qt, QTimer
from flightaware import FlightAwareAPI
from models.flight import Flight
from ui.flight_widget import FlightWidget


class SettingsDialog(QDialog):
    """Dialog for application settings."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setMinimumWidth(350)

        layout = QFormLayout(self)

        # API Key
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("Enter FlightAware API key")
        self.api_key_input.setText(os.getenv("FLIGHTAWARE_API_KEY", ""))
        layout.addRow("API Key:", self.api_key_input)

        # Search radius
        self.radius_input = QSpinBox()
        self.radius_input.setMinimum(10)
        self.radius_input.setMaximum(200)
        self.radius_input.setValue(50)
        layout.addRow("Search Radius (miles):", self.radius_input)

        # Refresh interval
        self.refresh_input = QSpinBox()
        self.refresh_input.setMinimum(10)
        self.refresh_input.setMaximum(600)
        self.refresh_input.setValue(60)
        layout.addRow("Refresh Interval (seconds):", self.refresh_input)

        # Buttons
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addStretch()
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addRow(btn_layout)

    def get_values(self):
        """Get saved settings."""
        return {
            "api_key": self.api_key_input.text(),
            "radius": self.radius_input.value(),
            "refresh": self.refresh_input.value(),
        }


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self, flight_api: FlightAwareAPI, parent=None):
        super().__init__(parent)
        self.flight_api = flight_api
        self.settings = QSettings()
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.refresh_flights)

        self._setup_ui()
        self._load_settings()
        self._search_nearby_flights()

    def _setup_ui(self):
        """Set up the main window UI."""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Title
        title_label = QLabel("✈️  PlaneSpottr - Flight Tracker")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2196f3; padding: 10px;")
        layout.addWidget(title_label)

        # Scrollable area for flight list
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(10, 0, 10, 10)

        # Flight list container
        flight_list_layout = QVBoxLayout()
        self.flight_widgets = []  # Store references for updates

        # Add flights to layout as they're loaded
        def add_flight(flight):
            widget = FlightWidget(flight)
            self.flight_widgets.append(widget)
            flight_list_layout.addWidget(widget)

        # Add flights as we get them
        add_flight = add_flight

        self.flight_list = flight_list_layout

        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area, stretch=1)

        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.addAction("Refresh", self.refresh_flights, QKeySequence.Shortcut("Ctrl+R"))
        toolbar.addWidget(QLabel("Search Radius:"))
        self.radius_combo = QComboBox(toolbar)
        self.radius_combo.addItems(["10 miles", "50 miles", "100 miles", "200 miles"])
        self.radius_combo.currentTextChanged.connect(self.on_radius_changed)
        toolbar.addWidget(self.radius_combo)
        toolbar.addWidget(QLabel("&Settings:"))
        toolbar.addAction("Settings", self.show_settings, QKeySequence.Shortcut("Ctrl+,"))
        layout.addWidget(toolbar, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

        # Connect timer for auto-refresh
        self.refresh_timer.start(int(self.settings.value("refresh", 60) or 60))

    def _load_settings(self):
        """Load settings from QSettings."""
        refresh_interval = self.settings.value("refresh", 60)
        if refresh_interval:
            self.refresh_timer.setInterval(int(refresh_interval))
        self.radius_combo.setCurrentText(f"{self.settings.value('radius', 50)} miles")

    def on_radius_changed(self, radius: str):
        """Handle radius combo change."""
        radius_map = {"10 miles": 10, "50 miles": 50, "100 miles": 100, "200 miles": 200}
        self.radius_combo.currentIndexChanged.connect(lambda: self.refresh_flights())

    def show_settings(self):
        """Show settings dialog."""
        dialog = SettingsDialog(self)
        result = dialog.exec()
        if result == 1:  # Accepted
            values = dialog.get_values()
            self.settings.setValue("api_key", values["api_key"])
            self.settings.setValue("radius", values["radius"])
            self.settings.setValue("refresh", values["refresh"])
            self.refresh_timer.setInterval(values["refresh"])

            # Update API key for future requests
            if values["api_key"]:
                self.flight_api.api_key = values["api_key"]

    def refresh_flights(self):
        """Refresh flight data."""
        try:
            self.status_bar.showMessage("Refreshing flights...", 3000)

            # Get nearby flights
            radius = self.radius_combo.currentText().replace(" miles", "")
            flights = self.flight_api.get_nearby_flights(
                40.7128, -74.0060,  # Default to NYC
                radius=int(radius)
            )

            # Update or clear flight widgets
            self.flight_list.clear()
            self.flight_widgets.clear()

            for flight_data in flights:
                flight = Flight.from_api_data(flight_data)
                add_flight(flight)

            # Scroll to top
            scroll = self.findChild(QScrollArea)
            if scroll:
                scroll.verticalScrollBar().scrollToTop()

            self.status_bar.showMessage(f"Found {len(flights)} flights", 5000)

        except Exception as e:
            self.status_bar.showMessage(f"Error: {str(e)}", 5000)

    def _search_nearby_flights(self):
        """Initial search for nearby flights."""
        self.refresh_flights()

    def on_position_change(self, flight: Flight):
        """Handle flight position update."""
        # Find and update the corresponding widget
        for widget in self.flight_widgets:
            if widget.flight.flight_number == flight.flight_number:
                widget.update_flight(flight)
                break

    def closeEvent(self, event):
        """Cleanup on close."""
        self.refresh_timer.stop()
        event.accept()
