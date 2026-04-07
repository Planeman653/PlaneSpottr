@echo off
echo =========================================
echo PlaneSpottr - Building Standalone .exe
echo =========================================
echo.

REM Check for virtual environment
if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] Virtual environment not found!
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

REM Clean previous build
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

echo Building PlaneSpottr.exe...
echo.

REM Build with PyInstaller
pyinstaller --clean ^
    --onefile ^
    --windowed ^
    --name=PlaneSpottr ^
    --noconsole ^
    --distpath=dist ^
    main.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Build failed!
    pause
    exit /b 1
)

echo.
echo =========================================
echo Build Complete!
echo =========================================
echo.
echo Your executable is at:
echo   %CD%\dist\PlaneSpottr.exe
echo.
echo You can now:
echo   1. Double-click dist\PlaneSpottr.exe
echo   2. Or distribute the file to others
echo.
echo =========================================
pause
