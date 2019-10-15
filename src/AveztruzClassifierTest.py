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
AveztruzClassifierTest encargada del las pruebas
de la clase AveztruzClassifier.
=============================================
"""

import unittest
from AveztruzClassifier import AveztruzClassifier

# Imagen de aveztruz
AVEZTRUZ_FILE = './unit_test_data/aveztruz.jpg'
# Imagen de no aveztruz
NOT_AVEZTRUZ_FILE = './unit_test_data/not_aveztruz.jpg'

class AveztruzClassifierTest(unittest.TestCase):
    
    # Prueba el caso de que se pase la imagen de un aveztruz
    def test_predict_true(self):
        classifier = AveztruzClassifier()
        self.assertTrue(classifier.predict(AVEZTRUZ_FILE))

    # Prueba el caso de que se pase la imagen de algo que no sea
    # un aveztruz
    def test_predict_false(self):
        classifier = AveztruzClassifier()
        self.assertFalse(classifier.predict(NOT_AVEZTRUZ_FILE))

if __name__ == "__main__":
    unittest.main()