# Detección Facial con OpenCV

Este proyecto utiliza la librería **OpenCV** de Python para realizar detección facial en tiempo real a través de la cámara del dispositivo. El sistema emplea un modelo preentrenado basado en **Haar Cascades**, capaz de reconocer rostros humanos y marcarlos con un rectángulo verde.

---

## 🧩 Requisitos previos

Antes de ejecutar el programa, asegúrate de tener instalado lo siguiente:

### Python 3.8 o superior

Puedes verificar si lo tienes instalado ejecutando en la terminal:
```bash
python --version
```

### Librería OpenCV

Instálala con el siguiente comando:
```bash
pip install opencv-python
```

---

## ▶️ Ejecución del programa

1. Guarda el archivo con el nombre `ejemplo.py` (o el que prefieras).

2. Abre una terminal en el directorio donde está guardado el archivo.

3. Ejecuta el siguiente comando:
```bash
   python ejemplo.py
```

4. Se abrirá una ventana mostrando la imagen de tu cámara con la detección facial activa.

5. Para salir del programa, presiona la tecla **ESC**.

---

## 📝 Notas adicionales

- Asegúrate de que tu cámara esté correctamente conectada y tenga los permisos necesarios.
- El rendimiento puede variar dependiendo de las condiciones de iluminación y la calidad de la cámara.
- Si experimentas problemas, verifica que OpenCV esté instalado correctamente ejecutando:
```bash
  pip show opencv-python
```

---

## 🔍 ¿Cómo funciona?

### 1. Inicialización de la cámara
```python
cam = cv2.VideoCapture(0)
```
Se captura el video desde la cámara predeterminada del dispositivo (índice 0).

### 2. Carga del clasificador Haar Cascade
```python
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
```
Se carga el modelo preentrenado `haarcascade_frontalface_default.xml`, especializado en detectar rostros frontales.

### 3. Captura y procesamiento de frames
```python
ret, frame = cam.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```
- Se lee cada frame de la cámara.
- Se convierte a escala de grises para optimizar la detección (los clasificadores Haar trabajan mejor con imágenes en escala de grises).

### 4. Detección de rostros
```python
faces = detector.detectMultiScale(gray, 1.1, 4)
```
El método `detectMultiScale` busca rostros en la imagen. Los parámetros son:
- `1.1`: Factor de escala (qué tanto se reduce la imagen en cada escala).
- `4`: Mínimo de vecinos (cantidad mínima de detecciones vecinas para considerar válido un rostro).

### 5. Marcado de rostros detectados
```python
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
```
Se dibuja un rectángulo verde alrededor de cada rostro detectado usando sus coordenadas (x, y) y dimensiones (ancho, alto).

### 6. Control de salida
```python
if cv2.waitKey(1) == 27:
    break
```
El programa se cierra al presionar la tecla **ESC** (código ASCII 27).

---

## ▶️ Ejecución del programa

1. Guarda el código en un archivo llamado `deteccion_facial.py`.

2. Abre una terminal en el directorio donde está guardado el archivo.

3. Ejecuta el siguiente comando:
```bash
   python deteccion_facial.py
```

4. Se abrirá una ventana mostrando la imagen de tu cámara con la detección facial activa.

5. Para salir del programa, presiona la tecla **ESC**.

---

## 🎓 Conclusión

- Este programa es como un "detector de caras automático" que funciona en tiempo real. Es similar a cómo funciona la cámara de tu teléfono cuando enfoca automáticamente los rostros antes de tomar una foto.
- Mediante el uso del clasificador **Haar Cascade**, es posible reconocer rostros y resaltarlos visualmente con rectángulos en una transmisión de video.