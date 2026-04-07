@echo off
setlocal enabledelayedexpansion

echo ================================================================
echo PlaneSpottr - Building Installer with NSIS
echo ================================================================
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo Please run: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Check and install NSIS if needed
where nsis >nul 2>nul
if %errorlevel% neq 0 (
    echo [INFO] Installing NSIS...
    pip install nsis
)

REM Clean previous build
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

echo [INFO] Building PlaneSpottr installer...
echo.

REM Build with PyInstaller
pyinstaller --clean ^
    --onefile ^
    --windowed ^
    --name=PlaneSpottr ^
    --noconsole ^
    --distpath=dist ^
    --workpath=build ^
    --specpath=build ^
    --add-data ".env;." ^
    --hidden-import=PyQt6 ^
    --hidden-import=PyQt6.QtCore ^
    --hidden-import=PyQt6.QtGui ^
    --hidden-import=PyQt6.QtWidgets ^
    --hidden-import=PyQt6.QtNetwork ^
    main.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Build failed!
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
echo To run: Double-click PlaneSpottr.exe
echo.

REM Copy additional files
if exist "README.md" copy "README.md" "dist\README.md" >nul 2>&1
if exist ".env.example" copy ".env.example" "dist\.env.example" >nul 2>&1

echo.
echo Also copied:
echo    dist\README.md
echo    dist\.env.example
echo.
echo ================================================================
echo.

REM Show file size
for %%F in ("dist\PlaneSpottr.exe") do @echo File size: %%~zF bytes

echo.
pause
