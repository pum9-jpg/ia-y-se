# 📷 Detección Facial Simple con OpenCV

Este es un script de Python que utiliza la biblioteca **OpenCV (cv2)** para realizar detección de rostros en tiempo real utilizando la cámara web de tu ordenador.

## 🚀 Requisitos

Necesitas tener **Python** instalado en tu sistema, junto con la biblioteca **OpenCV**.

## Activar el entorno virtual 
Mediante cmd
```bash
C:\....\env\Scripts\activate
#En caso de que no funcione solo ir hasta el \Scripts y ahi ejecutar
activate
```

Mediante bash
```bash
#ir hasta 
/.../../env/Script
#una vez en ese directorio ejecutar
. activate
```

Verificar que estas dentro del entorno virtual
```bash
#al principio de toda la ruta debe mostrar
(env)
```

### Instalación de OpenCV

Abre tu terminal o símbolo del sistema y ejecuta el siguiente comando:
```bash
pip install opencv-python
```

# 🛠️ Cómo Funciona
El script utiliza el clasificador en cascada Haar pre-entrenado para la detección frontal de rostros, que es un método clásico de visión por computadora.

## Pasos Clave del Código:

### 1. Inicialización de la Cámara
```bash
cam = cv2.VideoCapture(0)
```
Se abre la cámara web predeterminada

### 2. Carga del Detector
```bash
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
```
Se carga el archivo XML que contiene los patrones para detectar rostro

### 3. Bucle Principal
```bash ret, frame = cam.read()```: Lee un frame de la cámara.

```bash gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)```: Convierte el frame a escala de grises, lo que acelera el proceso de detección.

```bash faces = detector.detectMultiScale(...)```: Ejecuta la detección en la imagen en escala de grises.

Dibuja Rectángulos: Itera sobre las coordenadas de los rostros detectados y dibuja un rectángulo verde ((0, 255, 0)) alrededor de cada uno.

### 4. Mostrar y salir
```bash
cv2.imshow('Detección facial', frame)
if cv2.waitKey(1) == 27:
    break
```

### 5. Liberación de recursos
```bash
cam.release()
cv2.destroyAllWindows()
```
Libera la cámara y cierra todas las ventanas abiertas por OpenCV al salir del bucle.

# 💻 Uso
1. Asegúrate de que tu cámara web esté disponible y no esté siendo utilizada por otra aplicación.

2. Ejecuta el script desde tu terminal: ```bash python detector.py```
3. Aparecerá una ventana con el feed de tu cámara. Los rostros detectados serán marcados con un recuadro verde.

4. Para detener el programa, simplemente presiona la tecla ESC.