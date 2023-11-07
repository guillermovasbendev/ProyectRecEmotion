import os
import cv2 as cv
import numpy as np

# Lista de nombres de personas.
people = ['Dio', 'jenifer', 'jimi', 'Katerine', 'Lio']

# Lista vacía para almacenar los nombres de los archivos.
p = []

# Iteramos sobre los archivos en el directorio especificado.
for i in os.listdir(r"C:\Users\joseg\Desktop\MARCA PERSONAL\ProyectRecEmotion\images\caras"):
    p.append(i)  # Agregamos el nombre del archivo a la lista p.

# Imprimimos la lista de nombres de archivos después de procesar todos los archivos.
print(p)

# Inicializamos el clasificador Haar Cascade para detección de rostros.
haar_cascade = cv.CascadeClassifier("haar_face_xmls")

# Listas para almacenar características (imágenes de rostros) y etiquetas (nombres de personas).
features = []
labels = []

# Ruta del directorio que contiene las imágenes de las personas.
DIR = r"C:\Users\joseg\Desktop\MARCA PERSONAL\ProyectRecEmotion\images\caras"

# Función para crear el conjunto de entrenamiento.
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for image in os.listdir(path):
            img_path = os.path.join(path, image)

            # Leemos la imagen y la convertimos a escala de grises.
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Detectamos rostros en la imagen en escala de grises.
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            # Recorremos los rostros detectados y los agregamos a la lista de características y etiquetas.
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

# Llamamos a la función para crear el conjunto de entrenamiento.
create_train()

# Imprimimos la longitud de las características (imágenes de rostros) y etiquetas (nombres de personas).
print(f"Longitud de las características: {len(features)}")
print(f"Longitud de las etiquetas: {len(labels)}")


face_recognizer=cv.faceLBPHFaceRecognizer_create()
#2:58:15