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
PinguinoClassifier encargada identificar
imagenes de pinguinos.
=============================================
"""

from AnimalClassifier import AnimalClassifier

MODEL = './modelos/Pinguino_v2.model'

class PinguinoClassifier:
    
    # Crea un clasificador con el modelo del pinguino
    classifier = AnimalClassifier(MODEL)

    # Devuelve verdadero si la imagen dada es un pinguino
    # falso en caso contrario
    def predict(self, filepath):
        return self.classifier.predict(filepath)
    