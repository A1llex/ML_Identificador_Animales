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
JirafaClassifierTest encargada del las pruebas
de la clase JirafaClassifier.
=============================================
"""

import unittest
from JirafaClassifier import JirafaClassifier

# Imagen de jirafa
JIRAFA_FILE = './unit_test_data/jirafa.jpg'
# Imagen de no jirafa
NOT_JIRAFA_FILE = './unit_test_data/not_jirafa.jpg'

class JirafaClassifierTest(unittest.TestCase):
    
    # Prueba el caso de que se pase la imagen de un jirafa
    def test_predict_true(self):
        classifier = JirafaClassifier()
        self.assertTrue(classifier.predict(JIRAFA_FILE))

    # Prueba el caso de que se pase la imagen de algo que no sea
    # un jirafa
    def test_predict_false(self):
        classifier = JirafaClassifier()
        self.assertFalse(classifier.predict(NOT_JIRAFA_FILE))

if __name__ == "__main__":
    unittest.main()