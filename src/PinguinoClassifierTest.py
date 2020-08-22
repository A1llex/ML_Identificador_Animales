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
PinguinoClassifierTest encargada del las pruebas
de la clase PinguinoClassifier.
=============================================
"""

import unittest
from PinguinoClassifier import PinguinoClassifier

# Imagen de pinguino
PINGUINO_FILE = './unit_test_data/pinguino.jpg'
# Imagen de no pinguino
NOT_PINGUINO_FILE = './unit_test_data/not_pinguino.jpg'

class PinguinoClassifierTest(unittest.TestCase):
    
    # Prueba el caso de que se pase la imagen de un pinguino
    def test_predict_true(self):
        classifier = PinguinoClassifier()
        self.assertTrue(classifier.predict(PINGUINO_FILE))

    # Prueba el caso de que se pase la imagen de algo que no sea
    # un pinguino
    def test_predict_false(self):
        classifier = PinguinoClassifier()
        self.assertFalse(classifier.predict(NOT_PINGUINO_FILE))

if __name__ == "__main__":
    unittest.main()