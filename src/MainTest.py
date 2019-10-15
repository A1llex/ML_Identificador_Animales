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
Main encargada del la ejecucion principal
del clasificador.
=============================================
"""
import unittest
from Main import Main

HIPOPOTAMO = 'hipopotamo'
PINGUINO = 'pinguino'
AVEZTRUZ = 'aveztruz'
CUYO = 'cuyo'
JIRAFA = 'jirafa'

# Imagen de hipopotamo
HIPPO_FILE = './unit_test_data/hippo.jpg'
# Imagen de pinguino
PINGUINO_FILE = './unit_test_data/pinguino.jpg'
# Imagen de aveztruz
AVEZTRUZ_FILE = './unit_test_data/aveztruz.jpg'
# Imagen de cuyo
CUYO_FILE = './unit_test_data/cuyo.jpg'
# Imagen de jirafa
JIRAFA_FILE = './unit_test_data/jirafa.jpg'

class MainTest(unittest.TestCase):
    
    # Prueba el caso de que se pase la imagen de un hipopotamo
    def test_hipopotamo(self):
        main = Main()
        self.assertEqual(main.clasificar(HIPPO_FILE),HIPOPOTAMO)

    # Prueba el caso de que se pase la imagen de un pinguino
    def test_pinguino(self):
        main = Main()
        self.assertEqual(main.clasificar(PINGUINO_FILE),PINGUINO)

    # Prueba el caso de que se pase la imagen de un aveztruz
    def test_aveztruz(self):
        main = Main()
        self.assertEqual(main.clasificar(AVEZTRUZ_FILE),AVEZTRUZ)

    # Prueba el caso de que se pase la imagen de un cuyo
    def test_cuyo(self):
        main = Main()
        self.assertEqual(main.clasificar(CUYO_FILE),CUYO)

    # Prueba el caso de que se pase la imagen de una jirafa
    def test_jirafa(self):
        main = Main()
        self.assertEqual(main.clasificar(JIRAFA_FILE),JIRAFA)


if __name__ == "__main__":
    unittest.main()