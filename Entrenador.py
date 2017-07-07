import cv2
import os
import numpy as np
from PIL import Image
from time import sleep

reconocedor = cv2.face.createLBPHFaceRecognizer()
detector = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")


def getImagenesyEtiquetas(ruta):
        # Obtenemos la ruta de todos los archivos en la carpeta
        rutasImagen = [os.path.join(ruta, f) for f in os.listdir(ruta)]
        # Creamos una lista muestrasCaras vacia
        muestrasCaras = []
        # Creamos una lista Ids vacia
        Ids = []
        # Bucle que recorre todas las rutas de las imagenes obteniendo sus Ids y su iamgen
        for rutaImage in rutasImagen:
                # Cargamos la imagen y la convertimos en escala de grises
                imagenGris = Image.open(rutaImage).convert('L')
                # Ahora convertimos las imagenes PIL en arrays de numpy
                imagenNp = np.array(imagenGris, 'uint8')
                # Obtenemos el Id de la imagen
                Id = int(os.path.split(rutaImage)[-1].split(".")[1])
                # Estraer la cara de la muestra de entrenamietno
                caras = detector.detectMultiScale(imagenNp)
                # Si hay un rostro, lo agrega a la lista, con su Id
                for (x, y, w, h) in caras:
                        muestrasCaras.append(imagenNp[y:y + h, x:x + w])
                        print Id
                        Ids.append(Id)
                        # Mostramos las imagenes procesadas
                        cv2.imshow("Entrenando", imagenNp)
                        cv2.waitKey(10)
        return muestrasCaras, Ids


caras, Ids = getImagenesyEtiquetas('dataBase')
reconocedor.train(caras, np.array(Ids))
reconocedor.save('recognizer/trainner.yml')

cv2.destroyAllWindows()

print "Base de datos creada correctamente...\n"
sleep(3)
