# Detección Facial con OpenCV

Este proyecto utiliza **Python** y la librería **OpenCV** para detectar rostros en tiempo real a través de la cámara web.

---

## 📦 Requisitos

Antes de ejecutar el programa, asegúrate de tener instalado:

- **Python 3.x**
- **pip** (gestor de paquetes de Python)
- Librería **OpenCV**

Puedes instalar OpenCV ejecutando el siguiente comando en la terminal o PowerShell:

```bash
pip install opencv-python

🧠 Funcionamiento del Código
El programa realiza los siguientes pasos:

Importación de librerías
Se importa cv2, el módulo principal de OpenCV.

Inicialización de la cámara

python
Copiar código
cam = cv2.VideoCapture(0)
Abre la cámara principal (índice 0).

Carga del clasificador Haar Cascade

python
Copiar código
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
Se utiliza un modelo preentrenado para detectar rostros en imágenes.

Bucle principal de detección

Captura fotogramas en tiempo real.

Convierte la imagen a escala de grises.

Detecta rostros con detectMultiScale().

Dibuja un rectángulo verde sobre cada rostro detectado.

Visualización
Muestra el video en una ventana titulada "Detección Facial".

Salida del programa
El bucle termina al presionar la tecla ESC (27), liberando la cámara y cerrando las ventanas.

▶️ Ejecución
Ejecuta el script desde la terminal o PowerShell:

bash
Copiar código
python practica7.py
Si todo está correctamente instalado, se abrirá una ventana mostrando el video de la cámara con detección facial en tiempo real.

🧰 Archivos del Proyecto
Copiar código
p7-practica7/
├── practica7.py
└── README.md
Al ejecutar el programa, deberías ver tu rostro con un rectángulo verde en tiempo real, como en este ejemplo:

java
Copiar código
[ Ventana: Detección Facial ]
| 😃  <-- Rostro detectado (marcado en verde)
⚙️ Dependencias opcionales
Si deseas usar más clasificadores o funciones adicionales de OpenCV, puedes instalar el paquete completo:

bash
Copiar código
pip install opencv-contrib-python
