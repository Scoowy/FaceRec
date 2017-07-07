import cv2
import sqlite3
from time import sleep

cam = cv2.VideoCapture(1)
detector = cv2.CascadeClassifier(
    './haarcascades/haarcascade_frontalface_default.xml')


def insertOrUpdate(Id, Name):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM Personas WHERE ID=" + str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if (isRecordExist == 1):
        cmd = "UPDATE Personas SET Nombre=' "+str(Name)+" ' WHERE ID="+str(Id)
    else:
        cmd = "INSERT INTO Personas(ID,Nombre) Values("+str(Id)+",' "+str(Name)+" ' )"
    conn.execute(cmd)
    conn.commit()
    conn.close()


Id = raw_input('Escribe el ID\n')
nombre = raw_input('Escribe el Nombre\n')
insertOrUpdate(Id, nombre)

numFotosIng = raw_input("Numero de Imagenes a realizar\n")
if len(numFotosIng) == 0:
    numFotosIng = 40
else:
    numFotosIng = int(numFotosIng)

numFotos = numFotosIng - 1
numImg = 0

while(True):
    ret, img = cam.read()
    colorGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    caras = detector.detectMultiScale(colorGris, 1.2, 5)

    for (x, y, w, h) in caras:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Incremento de la muestra
        numImg = numImg + 1

        # Guardar la imagen en la carpeta de dataBase
        cv2.imwrite("dataBase/User." + Id + '.' + str(numImg) +
                    ".jpg", colorGris[y:y + h, x:x + w])

        cv2.imshow('frame', img)

    # Esperar por 1 segundo
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

    # Termina el proceso al capturar 20 imagenes
    elif numImg > numFotos:
        print "Captura de rostro - COMPLETA"
        break

cam.release()
cv2.destroyAllWindows()

sleep(3)
