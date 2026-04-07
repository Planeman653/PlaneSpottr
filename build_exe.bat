@echo off
echo ============================================
echo PlaneSpottr - Building Executable Installer
echo ============================================
echo.

REM Activate virtual environment if it exists
if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
) else (
    echo Virtual environment not found. Please run 'pip install' first.
    pause
    exit /b 1
)

REM Check if pyinstaller is installed
python -m pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo PyInstaller not found. Installing...
    python -m pip install pyinstaller
)

REM Build the executable
echo Building PlaneSpottr executable...
pyinstaller --onefile ^
    --windowed ^
    --name=PlaneSpottr ^
    --icon=icon.ico ^
    --noconsole ^
    --add-data ".env;." ^
    --hidden-import=PyQt6 ^
    --hidden-import=PyQt6.QtCore ^
    --hidden-import=PyQt6.QtGui ^
    --hidden-import=PyQt6.QtWidgets ^
    --hidden-import=PyQt6.QtNetwork ^
    main.py

if %errorlevel% neq 0 (
    echo.
    echo Build failed! Check the error messages above.
    pause
    exit /b 1
)

echo.
echo ============================================
echo Build Complete!
echo ============================================
echo.
echo Your executable is located at:
echo %CD%\dist\PlaneSpottr.exe
echo.
echo To create an installer (.msi), run:
echo   build_installer.bat
echo.
pause
