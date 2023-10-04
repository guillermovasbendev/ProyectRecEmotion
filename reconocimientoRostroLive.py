import cv2 as cv

# Cargar el clasificador en cascada Haar para la detección facial
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# Inicializar la cámara
cap = cv.VideoCapture(0)

while True:
    # Leer un fotograma de la cámara
    ret, frame = cap.read()

    # Convertir el fotograma a escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detectar rostros en el fotograma
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Dibujar rectángulos alrededor de los rostros detectados
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    # Mostrar el fotograma con los rectángulos alrededor de los rostros detectados
    cv.imshow("Detección de Rostros live", frame)

    # Esperar hasta que se presione cualquier tecla
    cv.waitKey(0)

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv.destroyAllWindows()
