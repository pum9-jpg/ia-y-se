# Proyecto de Reconocimiento de Rostros en Tiempo Real

## Descripción
Este proyecto implementa un **sistema robusto de reconocimiento facial** utilizando las librerías `face_recognition` y `OpenCV`.  
Permite detectar y reconocer rostros en tiempo real mediante la cámara web, comparando los rostros detectados con una base de datos local.

---

## 🧠 Tecnologías Utilizadas
- **Python 3.8+**
- **OpenCV** → Captura y visualización de video.
- **face_recognition** → Detección y codificación facial.
- **NumPy** → Procesamiento matemático de vectores faciales.

---

## 📂 Estructura del Proyecto

> La carpeta `rostros_conocidos` contiene las imágenes de las personas a reconocer.  
> El nombre del archivo (sin extensión) será el nombre mostrado en pantalla.

---

## ⚙️ Funcionamiento del Código

### 1. Carga de Rostros
El sistema busca imágenes dentro del directorio `rostros_conocidos/` y genera una **codificación numérica** por cada rostro detectado.

### 2. Detección en Tiempo Real
Usa la cámara web para capturar imágenes y convertirlas a formato RGB (requerido por la librería `face_recognition`).

### 3. Reconocimiento Facial
Compara cada rostro detectado con las codificaciones almacenadas mediante **distancia euclidiana**.  
Si una coincidencia es suficientemente cercana, el sistema muestra el nombre de la persona.

### 4. Visualización
Se dibujan rectángulos verdes alrededor de los rostros y se muestra el nombre correspondiente.  
Presionar **'q'** finaliza el reconocimiento.

---

## 🚀 Ejecución del Programa
1. Crea una carpeta llamada `rostros_conocidos` en el mismo directorio del script.
2. Añade imágenes claras de las personas que desees reconocer.
3. Ejecuta el programa desde consola:
   ```bash
   python reconocimiento_rostros.py
