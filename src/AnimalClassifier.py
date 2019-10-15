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

Fecha:  13/10/2019
=============================================
Contiene la definición de la clase
AnimalClassifier encargada de clasificar
imagenes dado un modelo de red neuronal.
=============================================
"""

import tensorflow as tf
import numpy as np
from Preprocess import Preprocess

# La categoria en la posicion 1 siempre es la verdadera
CATEGORIES =['NO es','Si es']

class AnimalClassifier:

    def __init__(self, model):
        self.model = tf.keras.models.load_model(model)

    # Regresa verdadero si la imagen es clasificada como 'Si es' por el modelo
    def predict(self, filepath):
        prediction = self.model.predict([Preprocess.prepare_image(filepath)])
        max = np.argmax(prediction)
        # Si esta en la posicion 1 es verdadero
        return True if max >= .7 else False