from Classes.Ponto import Ponto

class Segmento:
    def __init__(self,ponto1,ponto2:Ponto):
        self.ponto1 = ponto1
        self.ponto2 = ponto2


    def getPonto1(self):
        return self.ponto1
    def getPonto2(self):
        return self.ponto2

    def setPonto1(self,ponto1):
        self.ponto1 = ponto1

    def setPonto2(self,ponto2):
        self.ponto2 = ponto2

    def printa(self):
        print("Segmento ponto1", self.getPonto1().getX(), ",",self.getPonto1().getY(),
              "Ponto2", self.getPonto2().getX(),",",self.getPonto2().getY())





