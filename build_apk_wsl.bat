@echo off
REM 🔥 Script Build APK per Windows WSL 🔥
REM Created by Infinity X White devels team

echo ╔════════════════════════════════════════════════════════════╗
echo ║  🔥 BUILD APK - WINDOWS WSL 🔥                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Check if WSL is installed
wsl --list >nul 2>&1
if errorlevel 1 (
    echo ❌ ERRORE: WSL non installato!
    echo.
    echo 💡 Installa WSL con:
    echo    wsl --install
    echo    Poi riavvia il computer
    pause
    exit /b 1
)

echo ✅ WSL trovato!
echo.

REM Get current directory
set CURRENT_DIR=%CD%

REM Convert Windows path to WSL path
set WSL_PATH=%CURRENT_DIR:\=/%
set WSL_PATH=%WSL_PATH:C:=/mnt/c%
set WSL_PATH=%WSL_PATH:D:=/mnt/d%
set WSL_PATH=%WSL_PATH:E:=/mnt/e%
set WSL_PATH=%WSL_PATH:F:=/mnt/f%

echo 📍 Directory: %WSL_PATH%
echo.

echo 🚀 Avvio build in WSL...
echo ⏱️  Questo richiede 30-60 minuti...
echo.

REM Run build script in WSL
wsl bash -c "cd '%WSL_PATH%' && chmod +x build_apk.sh && ./build_apk.sh"

if errorlevel 1 (
    echo.
    echo ❌ ERRORE durante il build!
    pause
    exit /b 1
)

echo.
echo ✅ Build completato!
echo.
echo 📦 APK si trova in:
echo    %CURRENT_DIR%\bin\
echo.
pause
