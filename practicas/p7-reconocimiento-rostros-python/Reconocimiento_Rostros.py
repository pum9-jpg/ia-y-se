import cv2

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imshow("Detección Facial", frame)
    if cv2.waitKey(1) == 27: #ESC para salir
        break

cam.release()
cv2.destroyAllWindows()