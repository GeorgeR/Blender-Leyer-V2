@echo off
setlocal

echo ========================================================
echo   Blender Layer V2 installer for Krita
echo   Compatible with Blender 5.2.0 LTS and Krita 5.3+
echo ========================================================
echo.

set "TARGET=%APPDATA%\krita\pykrita"
set "SOURCE=%~dp0"

echo [*] Krita destination folder: %TARGET%
echo.

if not exist "%TARGET%" (
    echo [*] Creating pykrita folder...
    mkdir "%TARGET%"
)

if exist "%SOURCE%blender_layer.desktop" (
    echo [*] Copying blender_layer.desktop...
    copy /Y "%SOURCE%blender_layer.desktop" "%TARGET%\" >nul
    
    echo [*] Copying blender_layer module...
    if not exist "%TARGET%\blender_layer" (
        mkdir "%TARGET%\blender_layer"
    )
    xcopy "%SOURCE%blender_layer\*" "%TARGET%\blender_layer\" /Y /E /I >nul
    echo  [OK] Blender Layer installed successfully.
) else (
    echo  [ERROR] blender_layer.desktop was not found in the current folder.
    pause
    exit /b 1
)

echo.
echo ========================================================
echo   Installation completed successfully!
echo ========================================================
echo.
echo To enable the plugin in Krita:
echo 1. Open Krita (or restart it if it is already open).
echo 2. Go to: Settings ^> Configure Krita... ^> Python Plugin Manager
echo 3. Check:
echo    [X] Blender Layer
echo 4. Click OK and restart Krita.
echo 5. Open the docker from: Settings ^> Dockers ^> Blender Layer
echo.
pause
