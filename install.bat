@echo off
setlocal

echo ========================================================
echo   Instalador de Blender Layer V2 para Krita
echo   Compatible con Blender 5.2.0 LTS y Krita 5.3+
echo ========================================================
echo.

set "TARGET=%APPDATA%\krita\pykrita"
set "SOURCE=%~dp0"

echo [*] Carpeta destino Krita: %TARGET%
echo.

if not exist "%TARGET%" (
    echo [*] Creando carpeta pykrita...
    mkdir "%TARGET%"
)

if exist "%SOURCE%blender_layer.desktop" (
    echo [*] Copiando blender_layer.desktop...
    copy /Y "%SOURCE%blender_layer.desktop" "%TARGET%\" >nul
    
    echo [*] Copiando modulo blender_layer...
    if not exist "%TARGET%\blender_layer" (
        mkdir "%TARGET%\blender_layer"
    )
    xcopy "%SOURCE%blender_layer\*" "%TARGET%\blender_layer\" /Y /E /I >nul
    echo  [OK] Blender Layer instalado con exito.
) else (
    echo  [ERROR] No se encontro blender_layer.desktop en la carpeta actual.
    pause
    exit /b 1
)

echo.
echo ========================================================
echo   Instalacion completada con exito!
echo ========================================================
echo.
echo Pasos para activarlo en Krita:
echo 1. Abre Krita (o reinicialo si ya estaba abierto).
echo 2. Ve a: Ajustes ^> Configurar Krita... ^> Gestor de complementos de Python
echo 3. Activa la casilla:
echo    [X] Blender Layer
echo 4. Pulsa Aceptar y reinicia Krita.
echo 5. Abre el panel desde: Ajustes ^> Paneles ^> Blender Layer
echo.
pause
