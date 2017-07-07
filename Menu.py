import Tkinter as tk
import os

# os.system("start C:\Users\HP-pc\Desktop\ProyetoFaceRecSQLTK\Detector.py")
# os.system("exit")


def ejecutarVideo():
    os.system("start C:\Users\HP-pc\Desktop\ProyetoFaceRecSQLTK\Video.py")
    imprimir("Mostrando video - Pulse la tecla Q para salir")


def ejecutarCapturaR():
    os.system("start C:\Users\HP-pc\Desktop\ProyetoFaceRecSQLTK\CapturaRostros.py")
    imprimir("Capturando caras")


def ejecutarEntrenador():
    os.system("start C:\Users\HP-pc\Desktop\ProyetoFaceRecSQLTK\Entrenador.py")
    imprimir("Entrenando")


def ejecutarDetector():
    os.system("start C:\Users\HP-pc\Desktop\ProyetoFaceRecSQLTK\Detector.py")
    imprimir("Detectando caras - Pulse la tecla Q para salir")


def ejecutarBaseDatos():
    os.system("start C:\Users\HP-pc\Desktop\SQLiteStudio\SQLiteStudio.exe")
    imprimir("Abriendo la Base de Datos")


def ejecutarCarpeta():
    os.system("explorer C:\Users\HP-pc\Desktop\ProyetoFaceRecSQLTK\dataBase")
    imprimir("Abriendo carpeta de imagenes")


def imprimir(textoL):
    accion.set(textoL)


fuente = 'Roboto'
textBasico = "Seleccione una opcion"

root = tk.Tk()
root.title("Menu - Deteccion de rostros")
root.geometry("350x450+0+0")

accion = tk.StringVar(root)
accion.set("Seleccione una opcion")

botonCV = tk.Button(root, text="Comprobar Video",
                    width=50, height=2, command=ejecutarVideo, font=fuente)
botonCV.pack()
botonCP = tk.Button(root, text="Capturar Rostros",
                    width=50, height=2, command=ejecutarCapturaR, font=fuente)
botonCP.pack()
botonE = tk.Button(root, text="Entrenador", width=50,
                   height=2, command=ejecutarEntrenador, font=fuente)
botonE.pack()
botonD = tk.Button(root, text="Detector", width=50,
                   height=2, command=ejecutarDetector, font=fuente)
botonD.pack()
botonBD = tk.Button(root, text="Comprobar BD", width=50,
                    height=2, command=ejecutarBaseDatos, font=fuente)
botonBD.pack()
botonC = tk.Button(root, text="Abrir carpeta de Imagenes", width=50,
                   height=2, command=ejecutarCarpeta, font=fuente)
botonC.pack()

texto = tk.Label(textvariable=accion, width=80, height=3,
                 bg="white", font=('Roboto', 12))
texto.pack()

tk.mainloop()


# botonEjemplo = tk.Button(root, text="Detector", command=funcion, width=80, height=20, anchor="w")
# botonEjemplo.pack()

# def cambioNombre(self):
# root.title("Titulo Cambiado")
