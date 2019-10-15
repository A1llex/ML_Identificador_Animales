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
HippoClassifier encargada identificar
imagenes de hipopotamos.
=============================================
"""

from AnimalClassifier import AnimalClassifier

MODEL = './modelos/Hipopotamo_v2.model'

class HippoClassifier:
    
    # Crea un clasificador con el modelo del hipopotamo
    classifier = AnimalClassifier(MODEL)

    # Devuelve verdadero si la imagen dada es un hipopotamo
    # falso en caso contrario
    def predict(self, filepath):
        return self.classifier.predict(filepath)
    
