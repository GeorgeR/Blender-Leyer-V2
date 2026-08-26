# Blender Layer V2

[![Krita](https://img.shields.io/badge/Krita-5.2%20%7C%205.3%2B-blue.svg)](https://krita.org)
[![Blender](https://img.shields.io/badge/Blender-5.2%20LTS%20%7C%204.x%20%7C%203.6%2B-orange.svg)](https://blender.org)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

**Blender Layer V2** es un plugin para **Krita** y **Blender** que permite conectar el viewport 3D de Blender directamente sobre una capa de dibujo en Krita en tiempo real. 

Diseñado especialmente para artistas 2D, ilustradores y concept artists que desean utilizar modelos y poses 3D como base y referencia para pintar en Krita.

---

## ✨ Novedades en V2 (Compatibilidad con Blender 5.2.0 LTS y Krita 5.3+)

- ✅ **Soporte total para Blender 5.2.0 LTS y Blender 4.x**: Actualizado para la nueva arquitectura gráfica y APIs de viewport de Blender.
- 🛠️ **Corrección del error de transparencia / lienzo en blanco**: Se solucionó el fallo de aplanamiento de matriz en el canal Alfa (`ravel(order='F')`) que volvía invisibles los modelos 3D en Krita.
- 📐 **Soporte para Pose Library y Action Previews**: Solucionado el error de desbordamiento en la lectura de previsualizaciones de poses de la biblioteca de assets.
- ⚡ **Optimización de memoria compartida (Shared Memory)**: Transferencia de píxeles fluida con recorte exacto de búfer.
- 🔍 **Detección automática en Windows**: Detección inteligente de ejecutables de Blender (versiones LTS, estándar y Steam).
- 📦 **Instalador de 1 Clic**: Scripts `install.bat` (Windows) e `install.py` (Multiplataforma) incluidos.

---

## 🚀 Instalación Rápida

### Opción A (Recomendada): Usar el instalador automático
1. Descarga o clona este repositorio.
2. **En Windows**: Haz doble clic en `install.bat`.
   **En macOS / Linux**: Ejecuta en la terminal `python install.py`.
3. Abre **Krita** y ve a:
   `Ajustes` ➔ `Configurar Krita...` ➔ `Gestor de complementos de Python`.
4. Activa la casilla **[X] Blender Layer**.
5. Reinicia Krita y abre el panel desde:
   `Ajustes` ➔ `Paneles` ➔ `Blender Layer`.

### Opción B: Instalación manual
1. Copia el archivo `blender_layer.desktop` y la carpeta `blender_layer` en la carpeta `pykrita` de tu usuario:
   - **Windows**: `%APPDATA%\krita\pykrita\`
   - **Linux**: `~/.local/share/krita/pykrita/`
   - **macOS**: `~/Library/Application Support/krita/pykrita/`
2. Activa el plugin en la configuración de Krita y reinicia.

---

## 🎮 Cómo Usar

1. Abre un lienzo en **Krita**.
2. En el panel lateral de **Blender Layer**, haz clic en **"Start Blender"**.
3. Blender se abrirá y se conectará automáticamente. Se creará una capa llamada `Blender Layer` en tu lienzo donde verás la previsualización 3D en vivo.
4. También puedes **arrastrar y soltar cualquier archivo `.blend`** directamente dentro de Krita para abrirlo y conectarlo automáticamente.

### Controles de Navegación
- **Girar vista 3D**: Arrastra el widget de esfera en el panel o mantén **Alt + Clic Central del Ratón** en el lienzo.
- **Desplazar (Pan)**: Mantén **Shift** y arrastra en el widget de esfera o **Alt + Ctrl + Clic Central**.
- **Zoom / Distancia focal**: Usa el control deslizante de distancia focal o **Alt + Shift + Clic Central**.

### Funciones Adicionales
- **Modos de Sombreado**: Cambia entre *Wireframe*, *Solid*, *Material Preview* y *Rendered*.
- **Guías de Perspectiva (Drawing Assistants)**: Haz clic en **"Create Assistant Set"** para generar líneas guía de perspectiva automáticas que coinciden con el ángulo de la cámara 3D.
- **Biblioteca de Poses**: Selecciona maniquíes (como *Body-chan* / *Body-kun*) y aplica poses de la biblioteca con doble clic.
- **Renderizado Final y Animación**: Renderiza directamente a la capa de Krita o importa secuencias de fotogramas como animación 2D.

---

## 📄 Licencia y Créditos

- **Código base original**: Creado por [Yuntoko](https://github.com/Yuntokon/BlenderLayer) bajo licencia GNU General Public License v3.0 (GPL-3.0).
- **Mantenimiento y compatibilidad V2**: Actualizado y mantenido por [JovasMotionDesigner](https://github.com/JovasMotionDesigner/Blender-Leyer-V2) para la comunidad de código abierto.
- **Modelos 3D Body-chan / Body-kun**: [vinchau](https://blendswap.com/blend/23521) (CC-0).
