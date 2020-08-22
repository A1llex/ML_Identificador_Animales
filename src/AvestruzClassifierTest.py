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
AvestruzClassifierTest encargada del las pruebas
de la clase AvestruzClassifier.
=============================================
"""

import unittest
from AvestruzClassifier import AvestruzClassifier

# Imagen de aveztruz
AVESTRUZ_FILE = './unit_test_data/avestruz.jpg'
# Imagen de no aveztruz
NOT_AVESTRUZ_FILE = './unit_test_data/not_avestruz.jpg'

class AvestruzClassifierTest(unittest.TestCase):
    
    # Prueba el caso de que se pase la imagen de un aveztruz
    def test_predict_true(self):
        classifier = AvestruzClassifier()
        self.assertTrue(classifier.predict(AVESTRUZ_FILE))

    # Prueba el caso de que se pase la imagen de algo que no sea
    # un aveztruz
    def test_predict_false(self):
        classifier = AvestruzClassifier()
        self.assertFalse(classifier.predict(NOT_AVESTRUZ_FILE))

if __name__ == "__main__":
    unittest.main()
