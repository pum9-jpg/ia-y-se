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
