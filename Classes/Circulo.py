from Classes.Ponto import Ponto

class Circulo():

        def __init__(self, centro: Ponto, raio: float):
            self.centro = centro
            self.raio = raio

        def getCentro(self):
            return self.centro

        def getRaio(self):
            return self.raio

        def setCentro(self, centro :Ponto):
            self.centro = centro

        def setRaio(self, raio: float):
            self.raio = raio


