@echo off
echo ===========================================================================
echo PlaneSpottr - Creating Windows Installer (setup.exe)
echo ===========================================================================
echo.

REM Check for NSIS
where nsis >nul 2>nul
if %errorlevel% neq 0 (
    echo NSIS not found. Installing...
    pip install nsis
)

REM Build the setup file
echo Creating installer...
pyinstaller --clean ^
    --onefile ^
    --name=PlaneSpottr ^
    --icon=icon.ico ^
    --noconsole ^
    --distpath=dist ^
    main.py

if %errorlevel% neq 0 (
    echo.
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo ===========================================================================
echo Installer Created!
echo ===========================================================================
echo.
echo You can now run PlaneSpottr.exe or distribute it.
echo For a more complete installer with setup instructions, see dist/
echo.
pause
