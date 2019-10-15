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
from HippoClassifier import HippoClassifier
from PinguinoClassifier import PinguinoClassifier
from AveztruzClassifier import AveztruzClassifier
from CuyoClassifier import CuyoClassifier
from JirafaClassifier import JirafaClassifier
import sys

HIPOPOTAMO = 'hipopotamo'
PINGUINO = 'pinguino'
AVEZTRUZ = 'aveztruz'
CUYO = 'cuyo'
JIRAFA = 'jirafa'

class Main:

    hippo_classifier = HippoClassifier()
    pinguino_classifier = PinguinoClassifier()
    aveztruz_classifier = AveztruzClassifier()
    cuyo_classifier = CuyoClassifier()
    jirafa_classifier = JirafaClassifier()

    # Devuelve la categoria a la que pertenece la imagen
    def clasificar(self, filepath):
        if self.hippo_classifier.predict(filepath):
            return HIPOPOTAMO
        elif self.pinguino_classifier.predict(filepath):
            return PINGUINO
        elif self.jirafa_classifier.predict(filepath):
            return JIRAFA
        elif self.cuyo_classifier.predict(filepath):
            return CUYO
        else:
            return AVEZTRUZ

if __name__ == '__main__':
    main = Main()
    filepath = sys.argv[1]
    print(main.clasificar(filepath))
        

