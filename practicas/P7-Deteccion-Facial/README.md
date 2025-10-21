# 👁️ Detección Facial con OpenCV

Este programa utiliza la biblioteca **OpenCV** para realizar **detección facial en tiempo real** a través de la cámara del computador.

---

## 🧠 Descripción General

El código abre la cámara del dispositivo, captura los cuadros de video y utiliza un **clasificador Haar Cascade** preentrenado para detectar rostros.  
Una vez detectados, dibuja rectángulos verdes alrededor de las caras y muestra el resultado en una ventana.

El programa continúa ejecutándose hasta que el usuario presiona la tecla **ESC** para salir.

---

## ⚙️ Requisitos Previos

Antes de ejecutar el programa, asegúrate de tener instalado **Python** y la biblioteca **OpenCV**.  
Ejecuta en la terminal el siguiente comando:

```bash
pip install opencv-python
```

---

## 💻 Código Fuente

```python
import cv2

# Abre la cámara (0 = cámara por defecto)
cam = cv2.VideoCapture(0)

# Carga el clasificador Haar para rostros
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cam.read()
    if not ret:
        print("No se pudo acceder a la cámara.")
        break

    # Convierte a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostros
    faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    # Dibuja los rectángulos en los rostros detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Muestra el video
    cv2.imshow("Detección facial", frame)

    # Presiona ESC para salir
    if cv2.waitKey(1) == 27:
        break

# Libera la cámara y cierra ventanas
cam.release()
cv2.destroyAllWindows()
```

---

## 🎯 Funcionamiento del Código

1. **Importación de la biblioteca OpenCV:** Se utiliza `cv2` para acceder a la cámara y procesar las imágenes.
2. **Captura de video:** Se abre la cámara con `VideoCapture(0)`.
3. **Conversión a escala de grises:** Mejora el rendimiento del detector.
4. **Detección facial:** Usa un modelo Haar Cascade incluido en OpenCV.
5. **Visualización:** Dibuja rectángulos verdes alrededor de los rostros detectados.
6. **Finalización:** El programa termina al presionar **ESC** y libera los recursos de la cámara.

---

## 🧩 Aplicaciones

- Seguridad y reconocimiento facial básico.  
- Monitoreo en tiempo real.  
- Base para proyectos de inteligencia artificial o visión por computadora.  

---

## Conclusiones 
Este proyecto demuestra de manera práctica cómo una computadora puede reconocer rostros en tiempo real usando técnicas simples de visión artificial, aunque el código es corto, permite comprender los fundamentos del procesamiento de imágenes y la detección automática, abriendo la puerta a desarrollos más avanzados en inteligencia artificial y seguridad.

## 🧑‍💻 Autor

**Kevin Ponce de León**  

