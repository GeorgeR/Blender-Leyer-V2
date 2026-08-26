"""
Instalador automático para Blender Layer V2 en Krita
Compatible con Windows, macOS y Linux
"""

import os
import shutil
import sys
from pathlib import Path


def get_krita_pykrita_path():
    """Detecta la ruta estándar de pykrita según el sistema operativo."""
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        if appdata:
            return Path(appdata) / "krita" / "pykrita"
        return Path.home() / "AppData" / "Roaming" / "krita" / "pykrita"
    elif sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "krita" / "pykrita"
    else:  # Linux
        return Path.home() / ".local" / "share" / "krita" / "pykrita"


def install():
    source_dir = Path(__file__).resolve().parent
    dest_dir = get_krita_pykrita_path()

    print("========================================================")
    print("      Instalador de Blender Layer V2 para Krita")
    print("  Compatible con Blender 5.2.0 LTS y Krita 5.3+")
    print("========================================================")
    print(f"[*] Origen:  {source_dir}")
    print(f"[*] Destino: {dest_dir}\n")

    dest_dir.mkdir(parents=True, exist_ok=True)

    desktop_src = source_dir / "blender_layer.desktop"
    module_src = source_dir / "blender_layer"

    if desktop_src.exists():
        shutil.copy2(desktop_src, dest_dir / "blender_layer.desktop")
        print(" [OK] Copiado: blender_layer.desktop")
    else:
        print(" [ERROR] No se encontro blender_layer.desktop")
        return False

    dest_module = dest_dir / "blender_layer"
    if module_src.exists():
        if dest_module.exists():
            shutil.rmtree(dest_module)
        shutil.copytree(module_src, dest_module)
        print(" [OK] Copiado: carpeta blender_layer/")
    else:
        print(" [ERROR] No se encontro la carpeta blender_layer/")
        return False

    print("\n========================================================")
    print("  Instalacion completada con exito!")
    print("========================================================")
    print("\nPasos para activarlo en Krita:")
    print("  1. Abre o reinicia Krita.")
    print("  2. Ve a: Ajustes > Configurar Krita... > Gestor de complementos de Python.")
    print("  3. Activa la casilla: [X] Blender Layer.")
    print("  4. Haz clic en Aceptar y reinicia Krita.")
    print("  5. Abre el panel desde: Ajustes > Paneles > Blender Layer.")
    print("========================================================\n")
    return True


if __name__ == "__main__":
    install()
