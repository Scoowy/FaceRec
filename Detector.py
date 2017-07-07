import numpy as np
import cv2
import sqlite3

# cargamos la plantilla e inicializamos la webcam:
rec = cv2.face.createLBPHFaceRecognizer()
rec.load("recognizer/trainner.yml")
faceDetect = cv2.CascadeClassifier(
    './haarcascades/haarcascade_frontalface_default.xml')


def getPerfil(id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM Personas WHERE ID=" + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


cam = cv2.VideoCapture(1)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

while(True):
    # leemos un frame y lo guardamos
    ret, img = cam.read()

    # convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # buscamos las coordenadas de los rostros (si los hay) y
    # guardamos su posicion
    faces = faceDetect.detectMultiScale(gray, 1.2, 5)

    # Dibujamos un rectangulo en las coordenadas de cada rostro
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])

        if conf <= 40:
            profile = getPerfil(id)
        else:
            profile = getPerfil(0)

        if (profile != None):
            #cv2.putText(img, "ID - " + str(profile[0]), (x, y + h + 30), font, 1, (255, 255, 255))
            cv2.putText(img, "NOMBRE - " + str(profile[1]), (x, y + h + 30), font, 1, (255, 255, 255))
            #cv2.putText(img, "EDAD - " + str(profile[2]), (x, y + h + 60), font, 1, (255, 255, 255))
            #cv2.putText(img, "SEXO - " + str(profile[3]), (x, y + h + 90), font, 1, (255, 255, 255))
        print conf

    # Mostramos la imagen
    cv2.imshow('img', img)

    # con la tecla 'q' salimos del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
