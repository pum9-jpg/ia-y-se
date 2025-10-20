import cv2

# Iniciar la cámara
cam = cv2.VideoCapture(0)

# Cargar el clasificador preentrenado para detección de rostros
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
    faces = detector.detectMultiScale(gray, 1.1, 4)  # Detectar rostros

    for (x, y, w, h) in faces:
        # Dibujar un rectángulo alrededor del rostro detectado
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el video con la detección
    cv2.imshow('Detección facial', frame)

    # Salir si se presiona la tecla ESC (27)
    if cv2.waitKey(1) == 27:
        break

# Liberar la cámara y cerrar las ventanas
cam.release()
cv2.destroyAllWindows()
