# Detección Facial en Tiempo Real con OpenCV

## Descripción
Este programa utiliza la librería **OpenCV** para realizar detección facial en tiempo real mediante la cámara del dispositivo.  
Emplea el clasificador preentrenado **Haar Cascade** incluido en OpenCV, el cual permite identificar rostros en imágenes o videos.

## Código
```python
import cv2 

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cam.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Deteccion Facial", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()
```
## Ejemplo de uso 

- **Al ejecutar el programa, se abrirá la cámara del dispositivo y se mostrará una ventana llamada "Detección Facial".**
- **Para finalizar la ejecución, el usuario puede presionar la tecla 'q'.**  
- **Cada vez que el sistema detecta un rostro, dibuja un rectángulo verde alrededor de él.**  

## Observaciones

- **Requiere tener instalada la librería OpenCV (pip install opencv-python).**
- **Es sensible a las condiciones de iluminación, posición del rostro y resolución de la cámara.**
- **Utiliza un modelo Haar Cascade, que es rápido pero menos preciso que los métodos modernos basados en redes neuronales.**

## Conclucion
El programa demuestra una implementación funcional y sencilla de visión por computadora para la detección de rostro, comprendiendo el flujo básico de captura, procesamiento y visualización de video con OpenCV, aunque su precisión es limitada en entornos complejos.