# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
=============================================
Autor: Equipo Pumacate
       - Johann Ramón Gordillo Guzman
       - José Jhovan Gallardo Valdez
       - Luis Erick Montes García
       - Diana Laura Nicolas Pavia
       - Alex González Fernández

Fecha:  23/09/2019
=============================================
Contiene la definición de la clase
Preprocess encargada del preprocesamiento
de datos.
=============================================
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random
import pickle
import cv2
import os


class Preprocess(object):
    """Clase para preprocesamiento de datos."""
    def __init__(self):
        """Constructor para la clase."""
        self.DATADIR = "data"
        self.CATEGORIES = ['trees', 'cats'] # Nuestras carpetas de imagenes.
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

                    # Todas las imagenes a tamaño 50x50. Pues los vectores siempre están en la misma dimensión.
                    new_array = cv2.resize(img_array, (self.IMG_SIZE, self.IMG_SIZE))

                    # Arreglo con la imagen y su etiqueta.
                    self.training_data.append([new_array, class_num])
                except Exception as e:
                    print(e)

    def split_and_prepare(self):
        """Docstring."""
        random.shuffle(self.training_data)
        for features, label in self.training_data:
            self.features.append(features)
            self.labels.append(label)

        # Un tensor recibe un vector y las matrices no son vectores.
        self.features = np.array(self.features).reshape(-1, self.IMG_SIZE, self.IMG_SIZE, 1)
        self.features =  (self.features.astype(float)/ 255.0)

    def write_out(self):
        """Docstring."""
        pickle_out = open("features.pickle", "wb")
        pickle.dump(self.features, pickle_out)
        pickle_out.close()

        pickle_out = open("labels.pickle", "wb")
        pickle.dump(self.labels, pickle_out)
        pickle_out.close()


# USO.
pr = Preprocess()
pr.load_training_data()
pr.split_and_prepare()
pr.write_out()
