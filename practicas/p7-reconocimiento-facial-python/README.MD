# 📸 Detección Facial con OpenCV

## 🧠 Descripción General

Este programa utiliza la librería **OpenCV** en Python para realizar
**detección facial en tiempo real** a través de la cámara del
dispositivo.\
Emplea un **clasificador Haar Cascade**, una técnica de visión por
computadora basada en aprendizaje automático.

------------------------------------------------------------------------

## ⚙️ Requisitos Previos

Antes de ejecutar el programa, asegúrate de tener instaladas las
siguientes dependencias:

``` bash
pip install opencv-python
```

------------------------------------------------------------------------

## 🧩 Explicación del Código

### 1. Importación de librerías

``` python
import cv2
```

La librería `cv2` pertenece a OpenCV y proporciona las funciones
necesarias para capturar video, procesar imágenes y detectar objetos.

------------------------------------------------------------------------

### 2. Inicialización de la cámara

``` python
cam = cv2.VideoCapture(0)
```

El parámetro `0` indica que se usará la cámara predeterminada del
sistema.\
Si se conecta una cámara externa, puede probarse con `1`, `2`, etc.

------------------------------------------------------------------------

### 3. Carga del clasificador Haar

``` python
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
```

Este clasificador preentrenado permite detectar rostros en imágenes
mediante patrones geométricos.

------------------------------------------------------------------------

### 4. Bucle principal

``` python
while True:
    ret, frame = cam.read()
```

Captura cada fotograma de la cámara en tiempo real.\
`ret` indica si la captura fue exitosa.

------------------------------------------------------------------------

### 5. Conversión a escala de grises

``` python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

Los clasificadores Haar funcionan mejor con imágenes en escala de
grises.

------------------------------------------------------------------------

### 6. Detección de rostros

``` python
faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
```

-   **`scaleFactor`**: reduce el tamaño de la imagen en cada escala
    (controla la precisión).
-   **`minNeighbors`**: número mínimo de detecciones vecinas para
    confirmar un rostro.

------------------------------------------------------------------------

### 7. Dibujo de rectángulos

``` python
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
```

Dibuja un **rectángulo verde** alrededor de cada rostro detectado.

------------------------------------------------------------------------

### 8. Mostrar la ventana de video

``` python
cv2.imshow("Detección facial", frame)
```

Muestra en pantalla el video con los rostros resaltados.

------------------------------------------------------------------------

### 9. Salida del programa

``` python
if cv2.waitKey(1) == 27:
    break
```

Si se presiona la tecla **ESC (27)**, el programa se detiene.

------------------------------------------------------------------------

### 10. Liberar recursos

``` python
cam.release()
cv2.destroyAllWindows()
```

Libera la cámara y cierra todas las ventanas abiertas de OpenCV.

------------------------------------------------------------------------

## 🧾 Resultado Esperado

Al ejecutar el programa, se abrirá una ventana mostrando el video en
tiempo real.\
Cada rostro detectado aparecerá rodeado por un **rectángulo verde**.

------------------------------------------------------------------------

## 🧠 Conclusión

El programa nos muestra cómo la visión por computadora puede llegar a aplicarse fácilmente con Python para detectar rostros en tiempo real. Gracias al uso de Haar Cascade, se logra identificar los rostros de forma correcta, llegando a servir como una base sólida para futuras aplicaciones de inteligencia artificial en reconocimiento facial o seguridad.

------------------------------------------------------------------------

