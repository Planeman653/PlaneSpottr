; NSIS Installer Script for PlaneSpottr
; Compile with: pyinstaller --dist-name PlaneSpottr --dist-dir dist

; Modern UI plugin
  !include MUI2.nsh
  !include LogicLib.nsh

;--------------------------------
; General Settings
;--------------------------------

; App Name
Name "PlaneSpottr - Flight Tracker"

; Version
VIProductVersion "0.0.0"
VIAddVersionKey "ProductName" "PlaneSpottr"
VIAddVersionKey "FileDescription" "Flight Tracker Desktop Application"
VIAddVersionKey "FileVersion" "0.0.0"
VIAddVersionKey "CompanyName" "PlaneSpottr"
VIAddVersionKey "LegalCopyright" "MIT License"
VIAddVersionKey "ProductShortDescription" "Real-time flight tracking application"

; Manufacturer
VIAddVersionKey "Manufacturer" "PlaneSpottr"

; Icon
!define MUI_ICON "..\icon.ico"
!define MUI_UNICON "..\icon.ico"

; Output directory
!define MUI_WELCOMEFINISHPAGE_BITMAP "..\UI\WelcomeBitmap.bmp"
!define MUI_WELCOMEFINISHPAGE_BITMAP_INACTIVE "..\UI\WelcomeBitmap.bmp"

; License page
!define MUI_LICENSE_TEXT_EN "MIT License\n\nCopyright (c) 2026\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the \"Software\"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE."
!define MUI_LICENSE_TEXTLANG 1033

;--------------------------------
; Languages
;--------------------------------

!insertmacro MUI.Language "en_US"

;--------------------------------
; Pages
;--------------------------------

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

;--------------------------------
; Uninstaller Pages
;--------------------------------

!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

;--------------------------------
; Registers
;--------------------------------

!insertmacro MUI_FUNCTION_REGISTRY
; Add uninstall key
; Registry Key: HKEY_LOCAL_MACHINE\SOFTWARE\PlaneSpottr
; Name: UninstallString
; Value: "C:\Program Files\PlaneSpottr\uninstall.exe" /S
; Type: String
;

!insertmacro MUI_FUNCTION_REGISTRY_UNINSTALL

;--------------------------------
; Sections
;--------------------------------

Section "InstallFiles"

    ; Set output path for the installer
    SetOutPath $INSTDIR

    ; Install the executable
    File /r "dist\PlaneSpottr.exe"

    ; Create shortcuts
    CreateDirectory "$SMPROGRAMS\PlaneSpottr"
    CreateDirectory "$DESKTOP"

    ; Create desktop shortcut
    CreateShortCut "$DESKTOP\PlaneSpottr.lnk" "$INSTDIR\PlaneSpottr.exe" "$INSTDIR" "PlaneSpottr"
    CreateShortCut "$SMPROGRAMS\PlaneSpottr\PlaneSpottr.lnk" "$INSTDIR\PlaneSpottr.exe" "$INSTDIR" "PlaneSpottr"

    ; Create start menu link
    CreateShortCut "$SMPROGRAMS\PlaneSpottr\Uninstall PlaneSpottr.lnk" "$INSTDIR\uninstall.exe"

    ; Set icon for shortcuts
    WriteUninstaller "$INSTDIR\uninstall.exe"
    File /r "README.md"
    File /r "LICENSE"

    ; Set permissions
    ; This is optional but recommended for Windows applications

SectionEnd

Section "Uninstall"

    ; Remove shortcuts
    IfFileExists $SMPROGRAMS\PlaneSpottr\Uninstall PlaneSpottr.lnk, +2
    RmShortcut "$SMPROGRAMS\PlaneSpottr\Uninstall PlaneSpottr.lnk"
    Pop $0
    RmDir "$SMPROGRAMS\PlaneSpottr"
    Pop $0

    RmShortcut "$DESKTOP\PlaneSpottr.lnk"
    Pop $0

    ; Remove files
    RMDIR /r "$INSTDIR"

SectionEnd

;--------------------------------
; Functions
;--------------------------------

Function .onInit

    ; Set installation directory
    ; Use Program Files if running as admin, otherwise use user local app data
    StrCpy $INSTDIR "$PROGRAMFILES\PlaneSpottr"

    ; Check if admin
    ; $ADMIN = if running as admin
    ; If $ADMIN != "" then
    ;     StrCpy $INSTDIR "$PROGRAMFILES\PlaneSpottr"
    ; Else
    StrCpy $INSTDIR "$LOCALAPPDATA\PlaneSpottr"
    ; EndIf

FunctionEnd

Function .onInitUninst

    ; Set uninstaller directory
    StrCpy $INSTDIR "$LOCALAPPDATA\PlaneSpottr"

    ; Check if uninstaller exists
    IfFileExists $INSTDIR\uninstall.exe, uninstallExists

FunctionEnd

Function uninstallExists
    RmDir /r "$INSTDIR"
    RmShortcut "$SMPROGRAMS\PlaneSpottr\Uninstall PlaneSpottr.lnk"
    Pop $0
    RmShortcut "$DESKTOP\PlaneSpottr.lnk"
    Pop $0
    RmDir "$SMPROGRAMS\PlaneSpottr"
    RmDir "$DESKTOP"
    FunctionEnd

;--------------------------------
; Language Strings
;--------------------------------

LangString APP_TITLE 1033 "PlaneSpottr - Flight Tracker"
LangString WELCOME_TITLE 1033 "Welcome to PlaneSpottr"
LangString WELCOME_TEXT 1033 "This installer will set up PlaneSpottr on your computer.%n%nClick 'Next' to install the application.%nClick 'Cancel' to exit."
LangString LICENSE_TITLE 1033 "License Agreement"
LangString LICENSE_TEXT 1033 "Please read the End User License Agreement carefully before installing PlaneSpottr.%n%nBy clicking 'Next', you agree to the terms of the EULA."

;--------------------------------
; Compile
;--------------------------------

; Build the installer with the following command:
; nsis /DALLOW_REGISTRY=1 setup.nsi
