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
HippoClassifierTest encargada del las pruebas
de la clase HippoClassifier.
=============================================
"""

import unittest
from HippoClassifier import HippoClassifier

# Imagen de hipopotamo
HIPPO_FILE = './control/a_Hipo.jpg'
# Imagen de no hipopotamo
NOT_HIPPO_FILE = './control/not_a_Hipo.jpg'

class HippoClassifierTest(unittest.TestCase):
    
    # Prueba el caso de que se pase la imagen de un hipopotamo
    def test_predict_true(self):
        hippo_classifier = HippoClassifier()
        self.assertTrue(hippo_classifier.predict(HIPPO_FILE))

    # Prueba el caso de que se pase la imagen de algo que no sea
    # un hipopotamo
    def test_predict_false(self):
        hippo_classifier = HippoClassifier()
        self.assertFalse(hippo_classifier.predict(NOT_HIPPO_FILE))

if __name__ == "__main__":
    unittest.main()
