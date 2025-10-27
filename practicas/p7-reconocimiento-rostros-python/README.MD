
---

# 🐍 Guía de Instalación de Python

Esta guía describe diferentes métodos para instalar **Python** en **Windows**, **Linux** y **macOS**, utilizando la **línea de comandos**, la **Microsoft Store**, o **Visual Studio Code**.

---

## 📋 Requisitos Previos

* Conexión a Internet
* Permisos de administrador (en algunos sistemas)
* Conocer la versión del sistema operativo

---

## 🪟 Instalación en Windows

### 1️⃣ Opción 1: Línea de comandos (PowerShell o CMD)

```bash
# Descarga e instalación automática con winget
winget install Python.Python.3.12
```

> 🔎 *Puedes reemplazar `3.12` por la versión que desees instalar.*

**Verificar instalación:**

```bash
python --version
```

---

### 2️⃣ Opción 2: Microsoft Store

1. Abre la **Microsoft Store**.
2. Busca **"Python"**.
3. Selecciona una versión oficial de **Python Software Foundation**.
4. Haz clic en **Instalar**.

**Verifica desde CMD o PowerShell:**

```bash
python --version
```

---

### 3️⃣ Opción 3: Desde Visual Studio Code

1. Abre **Visual Studio Code**.
2. Presiona `Ctrl + Shift + X` para abrir **Extensiones**.
3. Busca **“Python”** (autor: *Microsoft*).
4. Instálala.
5. Si VS Code no detecta Python, te sugerirá instalarlo automáticamente.

   * Haz clic en **“Install Python”** y sigue las instrucciones.

---

## 🐧 Instalación en Linux

### 1️⃣ Opción 1: Línea de comandos

#### Debian / Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

#### Fedora:

```bash
sudo dnf install python3 python3-pip -y
```

#### Arch / Manjaro:

```bash
sudo pacman -S python python-pip
```

**Verificar instalación:**

```bash
python3 --version
```

---

### 2️⃣ Opción 2: VS Code Extension

1. Instala **VS Code** (si no lo tienes).
2. Abre VS Code → Extensiones (`Ctrl + Shift + X`).
3. Instala la extensión **Python** de Microsoft.
4. Configura el intérprete con `Ctrl + Shift + P` → “Python: Select Interpreter”.

---

## 🍎 Instalación en macOS

### 1️⃣ Opción 1: Línea de comandos (Homebrew)

```bash
# Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python
brew install python
```

**Verificar instalación:**

```bash
python3 --version
```

---

### 2️⃣ Opción 2: Instalador oficial

1. Ve a [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/)
2. Descarga el instalador `.pkg` de la última versión.
3. Sigue las instrucciones del asistente.

**Verificar instalación:**

```bash
python3 --version
```

---

### 3️⃣ Opción 3: VS Code Extension

1. Instala **VS Code** desde [https://code.visualstudio.com](https://code.visualstudio.com).
2. Abre VS Code → Extensiones (`Cmd + Shift + X`).
3. Instala la extensión **Python** de Microsoft.
4. Selecciona el intérprete con `Cmd + Shift + P` → “Python: Select Interpreter”.

---

## ✅ Verificación Final

Para comprobar que todo está funcionando correctamente:

```bash
python --version
pip --version
```

Y ejecuta un pequeño script de prueba:

```bash
python -c "print('¡Python instalado correctamente!')"
```

---

## 💡 Consejos adicionales

* Usa **pip** para instalar librerías:

  ```bash
  pip install nombre_de_paquete
  ```
* Mantén Python actualizado:

  ```bash
  python -m pip install --upgrade pip
  ```
* En VS Code, crea un entorno virtual con:

  ```bash
  python -m venv .venv
  ```

---

## Librerias del projecto

El projecto para su ejecucion depende de la libreria `cv2` que permitiria el fucionamiento del mismo.

Para installar, en la terminal ejecuta:
```bash
pip install opencv-python
```

---

## Ejecucion del projecto

Ejecuta el projecto con: 
```bash
python {projecto}.py
```

Si no se presentan errores con las librerias o dependencias, este solicitará acceso a la camara. Una vez aceptada, se abrira y detectara rostros, remarcandolos dentro de un cuadro.

---

# 🧠 Top 3 Alternativas a OpenCV (cv2)

Cuando **OpenCV** no es la mejor opción (por ser muy pesado, complejo o incompatible), existen otras bibliotecas de Python ideales para **procesamiento y análisis de imágenes**.
Aquí están las **3 mejores alternativas**:

---

## 🥇 1. **scikit-image**

### 📘 Descripción

Biblioteca de Python puro basada en **NumPy**, **SciPy** y **matplotlib**, centrada en el **procesamiento científico de imágenes**.
Ideal para investigadores o desarrolladores que prefieren operaciones tipo **NumPy** y un código más legible.

### ⚖️ Comparación

| Característica       | OpenCV                              | scikit-image                        |
| -------------------- | ----------------------------------- | ----------------------------------- |
| Base del lenguaje    | C++                                 | Python puro                         |
| Velocidad            | Más rápida (C/C++)                  | Más lenta (Python)                  |
| Curva de aprendizaje | Media                               | Fácil                               |
| Enfoque              | Visión por computadora              | Análisis científico                 |
| Ideal para           | Procesamiento en tiempo real, video | Segmentación y análisis de imágenes |

### 💻 Instalación

```bash
pip install scikit-image
```

### 🧩 Ejemplo

```python
from skimage import io, filters

imagen = io.imread('ejemplo.jpg', as_gray=True)
bordes = filters.sobel(imagen)

io.imshow(bordes)
io.show()
```

---

## 🥈 2. **Pillow (PIL Fork)**

### 📘 Descripción

Sucesora de la **Python Imaging Library (PIL)**. Excelente para **manipulación básica de imágenes**, como redimensionar, recortar, cambiar formato o aplicar filtros.

### ⚖️ Comparación

| Característica       | OpenCV                        | Pillow                             |
| -------------------- | ----------------------------- | ---------------------------------- |
| Enfoque              | Visión por computadora        | Edición de imágenes                |
| Rendimiento          | Alto (C++)                    | Medio                              |
| Formatos compatibles | Muy amplios                   | Muy amplios                        |
| Facilidad de uso     | Media                         | Muy fácil                          |
| Ideal para           | Procesamiento visual complejo | Edición simple y carga de imágenes |

### 💻 Instalación

```bash
pip install Pillow
```

### 🧩 Ejemplo

```python
from PIL import Image, ImageFilter

img = Image.open("ejemplo.jpg")
desenfocada = img.filter(ImageFilter.BLUR)
desenfocada.show()
```

---

## 🥉 3. **imageio**

### 📘 Descripción

Biblioteca ligera para **leer, escribir y mostrar imágenes y videos**, ideal para tareas simples y rápida integración con **NumPy** o **scikit-image**.

### ⚖️ Comparación

| Característica      | OpenCV                   | imageio                         |
| ------------------- | ------------------------ | ------------------------------- |
| Enfoque             | Suite completa de visión | Lectura/escritura de imágenes   |
| Soporte de video    | Sí                       | Limitado pero simple            |
| Rendimiento         | Optimizado               | Ligero                          |
| Complejidad del API | Media                    | Muy simple                      |
| Ideal para          | Proyectos de visión      | Conversión y manejo de archivos |

### 💻 Instalación

```bash
pip install imageio
```

### 🧩 Ejemplo

```python
import imageio.v3 as iio

imagen = iio.imread("ejemplo.jpg")
iio.imwrite("copia.jpg", imagen)
```

---

# 🧾 Tabla Resumen

| Posición | Biblioteca       | Caso Ideal                                 | Fortalezas                       | Facilidad de uso |
| -------- | ---------------- | ------------------------------------------ | -------------------------------- | ---------------- |
| 🥇 1     | **scikit-image** | Análisis, segmentación, investigación      | Herramientas científicas sólidas | ⭐⭐⭐⭐             |
| 🥈 2     | **Pillow**       | Edición y manipulación de imágenes         | API sencilla y clara             | ⭐⭐⭐⭐⭐            |
| 🥉 3     | **imageio**      | Lectura/escritura y conversión de archivos | Ligera y rápida                  | ⭐⭐⭐⭐             |

---

## 🔧 Recomendación

* Si necesitas **algoritmos de visión por computadora** → usa **OpenCV** o **scikit-image**.
* Si solo buscas **editar o manipular imágenes** → elige **Pillow**.
* Si tu objetivo es **leer, guardar o convertir archivos** → usa **imageio**.

---
