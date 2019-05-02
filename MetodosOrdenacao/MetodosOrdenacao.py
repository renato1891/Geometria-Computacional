import copy
from Classes.Ponto import Ponto
from Classes.Segmento import Segmento
from Classes.Circulo import Circulo


def MetodoPontoOrdena(ponto1: Ponto, ponto2: Ponto):
    if (ponto1.getX() > ponto2.getX()):
        return 1
    if (ponto1.getX() < ponto2.getX()):
        return -1
    if (ponto1.getY() > ponto2.getY()):
        return 1
    if (ponto1.getY() < ponto2.getY()):
        return -1
    return 0


def MetodoSegmentoOrdena(segmento1: Segmento, segmento2: Segmento):
    ponto1 = copy.deepcopy(segmento1.getPonto1())
    ponto2 = copy.deepcopy(segmento1.getPonto2())
    ponto3 = copy.deepcopy(segmento2.getPonto1())
    ponto4 = copy.deepcopy(segmento2.getPonto2())
    if (ponto1.getX() > ponto3.getX()):
        return 1
    if (ponto1.getX() < ponto3.getX()):
        return -1
    if (ponto1.getY() > ponto3.getY()):
        return 1
    if (ponto1.getY() < ponto3.getY()):
        return -1

    if (ponto2.getX() > ponto4.getX()):
        return 1
    if (ponto2.getX() < ponto4.getX()):
        return -1
    if (ponto2.getY() > ponto4.getY()):
        return 1
    if (ponto2.getY() < ponto4.getY()):
        return -1

    return 0


def MetodoCirculoOrdena(circulo1: Circulo, circulo2: Circulo):
    if(circulo1.raio>circulo2.raio):
        return 1
    if(circulo1.raio<circulo2.raio):
        return -1

    return 0