# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
=============================================
Autor: Equipo Pumacate
       - Johann Ramón Gordillo Guzman
       - José Jhovan Gallardo Valdez
       - Luis Erick Montes García
       - Diana Laura Nicolas Pavia
       - Alex Gerardo Fernández Aguilar

Fecha:  23/09/2019
=============================================
Contiene la definición de la clase
Preprocess encargada del preprocesamiento
de datos.
=============================================
"""

import numpy as np
import random
import pickle
import cv2
import os
from sklearn.preprocessing import LabelBinarizer


class Preprocess(object):
    """Clase para preprocesamiento de datos."""
    def __init__(self):
        """Constructor para la clase."""
        self.DATADIR = "data"
        self.CATEGORIES = ['NO','HIPOPOTAMO'] # Nuestras carpetas de imagenes.
        self.IMG_SIZE = 50 # 50x50.
        self.training_data = []
        self.labels = []
        self.features = []

    def load_training_data(self):
        """Cargamos las imagenes con las que entrenaremos nuestro modelo."""
        for category in self.CATEGORIES:
            path = os.path.join(self.DATADIR, category) # Une dos carpetas.
            class_num = self.CATEGORIES.index(category)
            for img in os.listdir(path):
                try:
                    # Leemos la imagen como arreglo. La leeremos en blanco/negro.
                    img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                    # Todas las imagenes a tamaño 50x50. Pues los vectores siempre 
                        #están en la misma dimensión.
                    new_array = cv2.resize(img_array, (self.IMG_SIZE, self.IMG_SIZE))
                    # Arreglo con la imagen y su etiqueta.
                    self.training_data.append([new_array, class_num])
                except Exception as e:
                    print("La imagen  ",path,img," no pudo ser leida.")

    def split_and_prepare(self):
        """Docstring."""
        labels = []
        random.shuffle(self.training_data)
        self.labels = []
        for features, label in self.training_data:
            self.features.append(features)
            self.labels.append(label)
        # Un tensor recibe un vector y las matrices no son vectores.
        self.features = np.array(self.features).reshape(-1, self.IMG_SIZE, self.IMG_SIZE, 1)
        
        self.features =  (self.features.astype(float)/ 255.0)
       
        self.labels = np.array(self.labels)

    def write_out(self):
        """Docstring."""
        pickle_out = open("features.pickle", "wb")
        pickle.dump(self.features, pickle_out)
        pickle_out.close()

        pickle_out = open("labels.pickle", "wb")
        pickle.dump(self.labels, pickle_out)
        pickle_out.close()

    @staticmethod
    def prepare_image(filepath):
        IMG_SIZE = 50  # 50 in txt-based
        img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  # read in the image, convert to grayscale
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize image to match model's expected sizing
        return new_array.reshape(1, IMG_SIZE, IMG_SIZE, 1).astype(float)/255.0  # return the image with shaping that TF wants.



# USO.
if __name__ == '__main__':
    pr = Preprocess()
    pr.load_training_data()
    pr.split_and_prepare()
    pr.write_out()

    print("Imagenes ",pr.features.shape)
    print("Etiquetas ",pr.labels.shape)

    print("Termino de procesar Exitosamente " , len(pr.labels) ,  "imagenes")
