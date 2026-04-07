@echo off
echo Building PlaneSpottr.exe...

REM Check for virtual environment
if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found!
    echo Please run: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Check for pyinstaller
python -m pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing PyInstaller...
    python -m pip install pyinstaller
)

REM Build
pyinstaller --clean --onefile --windowed --name=PlaneSpottr --noconsole main.py

if %errorlevel% neq 0 (
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo SUCCESS!
echo Your executable is at: dist\PlaneSpottr.exe
echo.
echo Run this to start the app:
echo dist\PlaneSpottr.exe
echo.

pause
