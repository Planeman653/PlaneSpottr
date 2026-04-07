@echo off
setlocal enabledelayedexpansion

echo ================================================================
echo PlaneSpottr - Creating Standalone Executable Installer
echo ================================================================
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo Please run: pip install -r requirements.txt
    echo Then run this script again.
    pause
    exit /b 1
)

REM Check if pyinstaller is installed
python -m pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Installing PyInstaller...
    python -m pip install pyinstaller
)

REM Create output directory
if not exist "dist" mkdir dist

echo [INFO] Building PlaneSpottr.exe...
echo.

REM Build with PyInstaller
pyinstaller ^
    --clean ^
    --onefile ^
    --windowed ^
    --name=PlaneSpottr ^
    --noconsole ^
    --noconfirm ^
    --distpath=dist ^
    --workpath=build ^
    --specpath=build ^
    --add-data ".env;." ^
    --hidden-import=PyQt6 ^
    --hidden-import=PyQt6.QtCore ^
    --hidden-import=PyQt6.QtGui ^
    --hidden-import=PyQt6.QtWidgets ^
    --hidden-import=PyQt6.QtNetwork ^
    --icon=icon.ico ^
    main.py 2>&1

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Build failed!
    echo Please check the error messages above.
    pause
    exit /b 1
)

echo.
echo ================================================================
echo Build Complete!
echo ================================================================
echo.
echo Your executable is ready at:
echo    %CD%\dist\PlaneSpottr.exe
echo.
echo To run the app:
echo    1. Double-click PlaneSpottr.exe
echo    2. Set your FLIGHTAWARE_API_KEY in .env file first
echo.
echo File size: %~z0 bytes
echo.
echo ================================================================
echo.

REM Copy README and license if they exist
if exist "README.md" (
    copy "README.md" "dist\README.md" >nul 2>&1
)
if exist "LICENSE" (
    copy "LICENSE" "dist\LICENSE" >nul 2>&1
)

REM Create a batch file with instructions
echo @echo off > dist\start.bat
echo echo Starting PlaneSpottr... >> dist\start.bat
echo start "PlaneSpottr" "%~dp0PlaneSpottr.exe" >> dist\start.bat
echo exit >> dist\start.bat

echo.
echo Also created: dist\start.bat (double-click to run)
echo.

REM Ask if user wants to create an installer
echo Do you want to create an MSI installer? (Y/N)
set /p CREATE_MSI=

if /i "%CREATE_MSI%"=="Y" (
    echo Creating installer...
    echo [NOTE] Installing NSIS if not present...
    pip install nsis 2>&1 | findstr /i /v "^already\|^success"
    pyinstaller --dist-name=PlaneSpottr --dist-dir=dist --clean main.py
    echo.
    echo Installer created: dist\PlaneSpottr.exe
)

echo.
echo Build finished!
pause
