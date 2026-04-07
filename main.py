#!/usr/bin/env python3
"""
PlaneSpottr - Flight Tracker Desktop Application

A desktop application that displays real-time flight information
from the FlightAware API for nearby flights.
"""

import sys
import os
import json

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from api.flightaware import FlightAwareAPI
from ui.main_window import MainWindow


class SetupDialog(QDialog):
    """Dialog to set up API key on first run."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PlaneSpottr Setup")
        self.setMinimumSize(400, 200)

        layout = QVBoxLayout(self)

        # Header
        title_label = QLabel("<h2>✈️  PlaneSpottr Setup</h2>")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("padding: 15px; background: #f5f5f5;")
        layout.addWidget(title_label)

        # Instructions
        instructions = QLabel(
            "To use PlaneSpottr, you need a free FlightAware API key.<br/>"
            "<br/>"
            "1. Go to <a href='https://flightaware.com/help/development/get-key'>FlightAware Developer</a><br/>"
            "2. Click 'Get Key' and complete registration<br/>"
            "3. Copy your API key below"
        )
        instructions.setWordWrap(True)
        instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instructions.setStyleSheet("padding: 15px;")
        layout.addWidget(instructions)

        # API Key input
        layout.addStretch()

        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("Enter your FlightAware API key here...")
        self.api_key_input.setFixedSize(300, 40)
        self.api_key_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 2px solid #2196f3;
                border-radius: 5px;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.api_key_input)

        # Buttons
        btn_layout = QHBoxLayout()

        help_button = QPushButton("How to get a key?")
        help_button.clicked.connect(self.show_help)
        help_button.setMinimumWidth(120)
        btn_layout.addWidget(help_button)

        ok_button = QPushButton("Save and Start")
        ok_button.setMinimumWidth(150)
        ok_button.clicked.connect(self.accept)
        btn_layout.addWidget(ok_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.setMinimumWidth(100)
        cancel_button.clicked.connect(self.reject)
        btn_layout.addWidget(cancel_button)

        layout.addLayout(btn_layout)

        self.result_key = None

    def show_help(self):
        """Show help for getting API key."""
        QMessageBox.about(self, "Getting an API Key",
            "<h3>How to Get a Free API Key</h3>"
            "<p>1. Visit <a href='https://flightaware.com/help/development/get-key'>FlightAware Developer</a></p>"
            "<p>2. Click 'Get Key'</p>"
            "<p>3. Fill in your email and name</p>"
            "<p>4. Accept the terms (takes 30 seconds)</p>"
            "<p>5. Copy your API key</p>")

    def get_api_key(self):
        """Get the entered API key."""
        key = self.api_key_input.text().strip()
        self.result_key = key if key and not key.startswith("your_api_key_here") else None
        return self.result_key


def check_api_key():
    """Check if API key is set, prompt if not."""
    # Check for .env file
    env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')

    if not os.path.exists(env_file):
        # No .env file - show setup dialog
        app = QApplication.instance()
        if not app:
            app = QApplication(sys.argv)

        dialog = SetupDialog()
        dialog.exec()

        if dialog.result_key:
            # Save API key to .env
            env_data = {
                "FLIGHTAWARE_API_KEY": dialog.result_key,
                "SEARCH_RADIUS_MILES": "50",
                "AUTO_REFRESH_INTERVAL": "60"
            }
            try:
                with open(env_file, 'w') as f:
                    json.dump(env_data, f)
            except IOError:
                pass

            return dialog.result_key

    # .env exists - load key
    try:
        with open(env_file, 'r') as f:
            data = json.load(f)
            key = data.get('FLIGHTAWARE_API_KEY', '')
            return key
    except (json.JSONDecodeError, IOError):
        pass

    # Invalid .env - show setup dialog
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    dialog = SetupDialog()
    dialog.exec()

    if dialog.result_key:
        env_data = {
            "FLIGHTAWARE_API_KEY": dialog.result_key,
            "SEARCH_RADIUS_MILES": "50",
            "AUTO_REFRESH_INTERVAL": "60"
        }
        try:
            with open(env_file, 'w') as f:
                json.dump(env_data, f)
        except IOError:
            pass

        return dialog.result_key

    return None


def main():
    """Main application entry point."""
    # Get API key (prompts on first run)
    api_key = check_api_key()

    if not api_key:
        print("Error: No API key provided. Exiting...")
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
