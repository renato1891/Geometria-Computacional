from Classes.Ponto import Ponto
from Classes.Segmento import Segmento
from Classes.Conjunto import Conjunto
from operator import itemgetter
class Poligono:

    def __init__(self, segmento: Segmento, metodosegmento):
        self.listaPonto = [ ]
        self.conjuntoSegmentos = Conjunto(metodosegmento)
        self.conjuntoSegmentos.Insert(segmento)
        self.listaPonto.append((segmento.ponto1.getX(),segmento.ponto1.getY()))
        self.listaPonto.append((segmento.ponto2.getX(),segmento.ponto2.getY()))
        #self.listaPonto.sort(key=itemgetter(0))

    def addSegmento(self, segmento: Segmento):
        self.conjuntoSegmentos.Insert(segmento)
        a1 = ((segmento.getPonto1().x,segmento.getPonto1().y))
        if a1 not in self.listaPonto:
            self.listaPonto.append(a1)
        a2 = ((segmento.getPonto2().x,segmento.getPonto2().y))
        if a2 not in self.listaPonto:
            self.listaPonto.append(a2)
        #self.listaPonto.sort(key=itemgetter(0))
        #self.listaPonto = set(self.listaPonto)



