#!/usr/bin/env python3
"""
PlaneSpottr - Flight Tracker Desktop Application

A desktop application that displays real-time flight information
from the FlightAware API for nearby flights.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from api.flightaware import FlightAwareAPI
from ui.main_window import MainWindow


def main():
    """Main application entry point."""
    # Load API key from environment
    api_key = os.getenv("FLIGHTAWARE_API_KEY")

    if not api_key or api_key.startswith("your_api_key_here"):
        print("Error: FLIGHTAWARE_API_KEY environment variable not set")
        print("Please copy .env.example to .env and add your API key")
        print("Then run: python main.py")
        sys.exit(1)

    # Create QApplication with dark theme
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Set application info
    app.setApplicationName("PlaneSpottr")
    app.setApplicationVersion("1.0.0")

    # Create main window
    window = MainWindow(FlightAwareAPI(api_key))

    # Set window properties
    window.setWindowTitle("PlaneSpottr - Flight Tracker")
    window.setGeometry(100, 100, 700, 500)

    # Show window
    window.show()

    # Run event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
