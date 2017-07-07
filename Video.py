import numpy as np
import cv2

# cargamos la plantilla e inicializamos la webcam:
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)

while(True):
    # leemos un frame y lo guardamos
    ret, img = cap.read()

    # convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # buscamos las coordenadas de los rostros (si los hay) y
    # guardamos su posicion
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    # Dibujamos un rectangulo en las coordenadas de cada rostro
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)

    # Mostramos la imagen
    cv2.imshow('img', img)

    # con la tecla 'q' salimos del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
