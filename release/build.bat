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

echo [INFO] Building PlaneSpottr.exe...
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
echo File size: %~z0 bytes
echo.
echo To run:
echo   1. Double-click dist\PlaneSpottr.exe
echo   2. Make sure .env file with API key exists
echo.
echo =========================================
echo.

REM Copy README and other files to dist
if exist "README.md" (
    copy "README.md" "dist\README.md"
)
if exist ".env.example" (
    copy ".env.example" "dist\.env.example"
)
if exist "CHANGELOG.md" (
    copy "CHANGELOG.md" "dist\CHANGELOG.md"
)
if exist "LICENSE" (
    copy "LICENSE" "dist\LICENSE"
)
if exist "USER_GUIDE.md" (
    copy "USER_GUIDE.md" "dist\USER_GUIDE.md"
)
if exist "INSTALLER_README.md" (
    copy "INSTALLER_README.md" "dist\INSTALLER_README.md"
)

echo Documentation copied to dist folder
echo.
echo To create a release:
echo   1. Edit dist\README.md with your release notes
echo   2. Upload to GitHub Releases page
echo.
pause
