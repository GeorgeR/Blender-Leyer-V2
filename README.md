# Blender Layer V2

[![Krita](https://img.shields.io/badge/Krita-5.2%20%7C%205.3%2B-blue.svg)](https://krita.org)
[![Blender](https://img.shields.io/badge/Blender-5.2%20LTS%20%7C%204.x%20%7C%203.6%2B-orange.svg)](https://blender.org)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

**Blender Layer V2** is a plugin for **Krita** and **Blender** that displays Blender's 3D viewport on a layer in Krita in real time.

It is designed for 2D artists, illustrators, and concept artists who want to use 3D models and poses as references while painting in Krita.

---

## ✨ What's New in V2 (Blender 5.2.0 LTS and Krita 5.3+ Compatibility)

- ✅ **Full support for Blender 5.2.0 LTS and Blender 4.x**: Updated for Blender's new graphics architecture and viewport APIs.
- 🛠️ **Transparency and blank canvas fix**: Fixed the alpha channel matrix flattening error (`ravel(order='F')`) that made 3D models invisible in Krita.
- 📐 **Pose Library and Action Preview support**: Fixed an overflow error when reading pose previews from the asset library.
- ⚡ **Shared memory optimization**: Smooth pixel transfer with precise buffer trimming.
- 🔍 **Automatic detection on Windows**: Finds Blender executables from LTS, standard, and Steam installations.
- 📦 **One-click installer**: Includes `install.bat` (Windows) and `install.py` (cross-platform).

---

## 🚀 Quick Installation

### Option A (Recommended): Use the automatic installer

1. Download or clone this repository.
2. **On Windows**: Double-click `install.bat`.
   **On macOS or Linux**: Run `python install.py` in a terminal.
3. Open **Krita** and go to:
   `Settings` ➔ `Configure Krita...` ➔ `Python Plugin Manager`.
4. Check **[X] Blender Layer**.
5. Restart Krita and open the panel from:
   `Settings` ➔ `Dockers` ➔ `Blender Layer`.

### Option B: Install manually

1. Copy `blender_layer.desktop` and the `blender_layer` folder to your user `pykrita` folder:
   - **Windows**: `%APPDATA%\krita\pykrita\`
   - **Linux**: `~/.local/share/krita/pykrita/`
   - **macOS**: `~/Library/Application Support/krita/pykrita/`
2. Enable the plugin in Krita's settings and restart Krita.

---

## 🎮 How to Use

1. Open a canvas in **Krita**.
2. In the **Blender Layer** docker, click **"Start Blender"**.
3. Blender will launch and connect automatically. A layer named `Blender Layer` will appear on your canvas with a live 3D preview.
4. You can also **drag and drop any `.blend` file** into Krita to open and connect it automatically.

### Navigation Controls

- **Rotate the 3D view**: Drag the sphere widget in the docker, or hold **Alt + Middle Mouse Button** on the canvas.
- **Pan**: Hold **Shift** and drag the sphere widget, or use **Alt + Ctrl + Middle Mouse Button**.
- **Zoom / focal length**: Use the focal length slider, or **Alt + Shift + Middle Mouse Button**.

### Additional Features

- **Shading modes**: Switch between *Wireframe*, *Solid*, *Material Preview*, and *Rendered*.
- **Perspective guides (Drawing Assistants)**: Click **"Create Assistant Set"** to generate perspective guides matching the 3D camera angle.
- **Pose Library**: Select mannequins such as *Body-chan* and *Body-kun*, then double-click a pose to apply it.
- **Final rendering and animation**: Render directly to a Krita layer or import frame sequences as 2D animation.

---

## 📄 License and Credits

- **Original codebase**: Created by [Yuntoko](https://github.com/Yuntokon/BlenderLayer) under the GNU General Public License v3.0 (GPL-3.0).
- **V2 maintenance and compatibility**: Updated and maintained by [JovasMotionDesigner](https://github.com/JovasMotionDesigner/Blender-Leyer-V2) for the open-source community.
- **Body-chan / Body-kun 3D models**: [vinchau](https://blendswap.com/blend/23521) (CC-0).
