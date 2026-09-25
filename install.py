"""
Automatic installer for Blender Layer V2 in Krita
Compatible with Windows, macOS, and Linux
"""

import os
import shutil
import sys
from pathlib import Path


def get_krita_pykrita_path():
    """Find the standard pykrita path for the current operating system."""
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
    print("      Blender Layer V2 installer for Krita")
    print("  Compatible with Blender 5.2.0 LTS and Krita 5.3+")
    print("========================================================")
    print(f"[*] Source:      {source_dir}")
    print(f"[*] Destination: {dest_dir}\n")

    dest_dir.mkdir(parents=True, exist_ok=True)

    desktop_src = source_dir / "blender_layer.desktop"
    module_src = source_dir / "blender_layer"

    if desktop_src.exists():
        shutil.copy2(desktop_src, dest_dir / "blender_layer.desktop")
        print(" [OK] Copied: blender_layer.desktop")
    else:
        print(" [ERROR] blender_layer.desktop was not found")
        return False

    dest_module = dest_dir / "blender_layer"
    if module_src.exists():
        if dest_module.exists():
            shutil.rmtree(dest_module)
        shutil.copytree(module_src, dest_module)
        print(" [OK] Copied: blender_layer/ folder")
    else:
        print(" [ERROR] blender_layer/ folder was not found")
        return False

    print("\n========================================================")
    print("  Installation completed successfully!")
    print("========================================================")
    print("\nTo enable the plugin in Krita:")
    print("  1. Open or restart Krita.")
    print("  2. Go to: Settings > Configure Krita... > Python Plugin Manager.")
    print("  3. Check: [X] Blender Layer.")
    print("  4. Click OK and restart Krita.")
    print("  5. Open the docker from: Settings > Dockers > Blender Layer.")
    print("========================================================\n")
    return True


if __name__ == "__main__":
    install()
