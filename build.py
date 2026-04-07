#!/usr/bin/env python3
"""
Build script for PlaneSpottr executable installer.
Creates a PyInstaller bundle with embedded API key prompt.
"""

import os
import sys
import subprocess

# Configuration
BUILD_DIR = 'dist'
NAME = 'PlaneSpottr'
VERSION = '0.1.2'


def main():
    """Main build process."""
    print('=' * 60)
    print(f'PlaneSpottr Build - Version {VERSION}')
    print('=' * 60)
    print()

    # Check PyInstaller
    try:
        subprocess.run([sys.executable, '-m', 'PyInstaller', '--version'], check=True, capture_output=True)
    except Exception as e:
        print(f'Error: PyInstaller not found.')
        print(f'Please install it first: pip install pyinstaller')
        sys.exit(1)

    # Check for existing dist folder
    if os.path.exists(BUILD_DIR):
        print(f'Cleaning existing {BUILD_DIR}/ folder...')
        subprocess.run(['rmdir /s', BUILD_DIR], shell=True)

    # Build command
    print('Building executable...')
    print()

    try:
        subprocess.run(
            [sys.executable, '-m', 'PyInstaller',
             '--name', NAME,
             '--clean',
             '--onefile',
             '--noconsole',
             '--windowed',
             '--hidden-import', 'requests',
             '--hidden-import', 'pandas',
             '--hidden-import', 'numpy',
             '--hidden-import', 'PyQt6',
             '--hidden-import', 'dotenv',
             '--hidden-import', 'onavdata',
             '--add-data', '.env.example;.env',
             'main.py'],
            check=True, capture_output=False
        )
    except subprocess.CalledProcessError as e:
        print(f'Build failed: {e}')
        sys.exit(1)

    # Copy .env.example to dist folder for reference
    if os.path.exists('.env.example'):
        dest_env = os.path.join(BUILD_DIR, '.env.example')
        subprocess.run(['copy', '.env.example', '.env.example'], shell=True)
        print(f'Copied .env.example to {BUILD_DIR}/')

    print()
    print('=' * 60)
    print(f'Build complete! Executable created at:')
    print(f'  {BUILD_DIR}/{NAME}.exe')
    print('=' * 60)
    print()
    print('To install:')
    print('  1. Download PlaneSpottr.exe')
    print('  2. First run will prompt for FlightAware API key')
    print('  3. Key is saved for future use')


if __name__ == '__main__':
    main()
