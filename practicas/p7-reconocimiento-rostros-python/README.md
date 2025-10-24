# 👁️ Detección Facial con OpenCV (cv2)

Este programa utiliza la cámara web y un clasificador Haar Cascade para detectar rostros en tiempo real.


## ⚙️ Requisitos

Antes de ejecutar, instalá la librería necesaria:
```bash
pip install opencv-python
````

## 🚀 Ejecución

1. Guardá el script como `deteccion_facial.py`.
2. Ejecutalo con:

   ```bash
   python deteccion_facial.py
3. Se abrirá una ventana de video mostrando el marco de la cámara.
4. Presioná `ESC` para salir.

---

## 🧠 Cómo funciona

1. **Captura de video:** se obtiene la imagen desde la cámara (`cv2.VideoCapture(0)`).
2. **Conversión a escala de grises:** mejora la detección (`cv2.cvtColor`).
3. **Clasificación Haar Cascade:** detecta rostros en la imagen (`detectMultiScale`).
4. **Dibujo de rectángulos:** cada rostro detectado se marca con un recuadro azul.
5. **Salida controlada:** `ESC` cierra la ventana.

---

## 🧩 Alternativas a OpenCV (cv2)

| Librería             | Descripción breve                                                       | Facilidad de uso                   | Instalación                                 | Ideal para                                   |
| -------------------- | ----------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------- | -------------------------------------------- |
| **MediaPipe**        | Librería de Google con modelos preentrenados para rostro, manos y pose. | Alta (más automática)              | `pip install mediapipe`                     | IA aplicada y visión moderna                 |
| **dlib**             | Librería potente con detección facial basada en HOG o CNN.              | Media (requiere setup más técnico) | `pip install dlib` *(puede requerir CMake)* | Reconocimiento facial avanzado               |
| **face_recognition** | Usa `dlib` internamente, pero con API más simple.                       | Muy alta                           | `pip install face_recognition`              | Detección + reconocimiento facial rápido     |
| **DeepFace**         | Framework de alto nivel para análisis facial (edad, emoción, etc.).     | Alta                               | `pip install deepface`                      | Análisis y clasificación facial              |
| **ImageAI**          | Framework simplificado para detección general de objetos.               | Alta                               | `pip install imageai`                       | Detección múltiple con modelos preentrenados |

---

## 💡 Nota

`cv2` (OpenCV) es la opción más común y flexible para tareas básicas de visión por computadora.
Si buscás algo **más moderno o de alto nivel**, **MediaPipe** o **face_recognition** te ahorran mucho trabajo.

```

---
```
