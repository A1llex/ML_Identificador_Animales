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
CuyoClassifierTest encargada del las pruebas
de la clase CuyoClassifier.
=============================================
"""

import unittest
from CuyoClassifier import CuyoClassifier

# Imagen de cuyo
CUYO_FILE = './unit_test_data/cuyo.jpg'
# Imagen de no cuyo
NOT_CUYO_FILE = './unit_test_data/not_cuyo.jpg'

class CuyoClassifierTest(unittest.TestCase):
    
    # Prueba el caso de que se pase la imagen de un cuyo
    def test_predict_true(self):
        classifier = CuyoClassifier()
        self.assertTrue(classifier.predict(CUYO_FILE))

    # Prueba el caso de que se pase la imagen de algo que no sea
    # un cuyo
    def test_predict_false(self):
        classifier = CuyoClassifier()
        self.assertFalse(classifier.predict(NOT_CUYO_FILE))

if __name__ == "__main__":
    unittest.main()