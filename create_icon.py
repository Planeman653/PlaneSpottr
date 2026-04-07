#!/usr/bin/env python3
"""
Create a simple icon for PlaneSpottr
"""
from PyQt6.QtGui import QIcon, QPixmap, QPainter
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication


def create_icon():
    app = QApplication([])

    # Create a simple blue airplane icon
    pixmap = QPixmap(128, 128)
    pixmap.fill(Qt.transparent)

    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing, True)

    # Draw a simple airplane
    painter.setPen(Qt.NoPen)
    painter.setBrush(Qt.blue)

    # Airplane body (simple shape)
    painter.drawEllipse(64, 40, 25, 35)
    painter.drawEllipse(90, 40, 15, 35)
    painter.drawEllipse(38, 40, 15, 35)

    # Wings
    painter.drawEllipse(70, 70, 15, 15)
    painter.drawEllipse(70, 10, 15, 15)

    painter.end()

    # Save as icon.ico
    pixmap.save("icon.ico", "ICO")
    print("Icon created: icon.ico")


if __name__ == "__main__":
    create_icon()
