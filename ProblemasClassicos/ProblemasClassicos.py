from Classes.Ponto import Ponto
from Classes.Reta import Reta
from Classes.Circulo import Circulo
from Classes.Segmento import Segmento
from Classes.Conjunto import Conjunto
from Classes.Poligono import Poligono
import math
import copy
import matplotlib.pyplot as plt

#distancia entre dois pontos
def distance(p0: Ponto, p1: Ponto):
    return math.sqrt((p0.x - p1.x)**2 + (p0.y - p1.y)**2)

# distancia entre um ponto e uma reta
def DistanciaEntreUmPontoEumaReta(reta : Reta, ponto : Ponto):
    numerador = reta.getA()*ponto.getX()  + reta.getB()*ponto.getY() + reta.getC()
    if numerador < 0:
        numerador = numerador*(-1)

    denominador = math.sqrt((reta.getA()**2)+ (reta.getB()**2))

    return numerador / denominador

#area do circulo
def AreaDoCirculo(circulo : Circulo):
    return math.pi*(circulo.getRaio()**2)

#predicado do lado do circulo
def sideCircle(circulo : Circulo, ponto: Ponto):
    d = distance(ponto, circulo.centro)
    if(d == circulo.raio):
        return "Boundary"
    if(d< circulo.raio):
        return "Inside"
    if(d> circulo.raio):
        return "Outside"



#Intersecçao de segmentos
def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)

# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

#=====================================================================================
#ponto mais proximo de um segmento de reta


def _distancia_mais_proxima(segmento: Segmento, ponto: Ponto):

    A = ponto.getX() - segmento.getPonto1().getX()
    B = ponto.getY() - segmento.getPonto1().getY()
    C = segmento.getPonto2().getX() - segmento.getPonto1().getX()
    D = segmento.getPonto2().getY() - segmento.getPonto1().getY()

    dot = A * C + B * D
    len_sq = C * C + D * D
    param = -1
    if (len_sq != 0):  # in case of 0 length line
        param = dot / len_sq

    if (param < 0):
        xx = segmento.getPonto1().getX()
        yy = segmento.getPonto1().getY()

    elif (param > 1):
        xx = segmento.getPonto2().getX()
        yy = segmento.getPonto2().getY()

    else:
        xx = segmento.getPonto1().getX() + param * C
        yy = segmento.getPonto1().getY() + param * D

    dx = ponto.getX() - xx
    dy = ponto.getY() - yy
    return math.sqrt(dx * dx + dy * dy)



def ponto_mais_proximo(segmento: Segmento, conjuntoP: Conjunto):
    lista = conjuntoP.RetornaConjuntoEmLista()
    distancia = _distancia_mais_proxima(segmento, lista[0])
    ponto = None
    for i in lista:
        valor = _distancia_mais_proxima(segmento, i)
        if (valor < distancia):
            distancia = valor
            ponto = Ponto(i.getX(), i.getY())

    #plotaPontoMaisProximoSegmento(segmento, ponto,conjuntoP)
    return ponto


#=================================================================================
#intersecão entre dois segmentos
def onSegment(p : Ponto, q : Ponto, r : Ponto):
    if (q.getX <= max(p.getX, r.getX) and q.getX >= min(p.getX, r.getX) and
                q.getY <= max(p.getY, r.getY) and q.getY >= min(p.getY, r.getY)):
        return True

    return False
#predicado orientação 2d
def orientation(p : Ponto, q : Ponto, r : Ponto):
    val = (q.getY() - p.getY()) * (r.getX() - q.getX()) - (q.getX() - p.getX()) * (r.getY() - q.getY())
    if (val==0):
        return 0
    if (val>0):
        return 1
    else:
        return 2



def doIntersect(seg1: Segmento, seg2: Segmento):
    o1 = orientation(seg1.getPonto1(), seg1.getPonto2(), seg2.getPonto1())
    o2 = orientation(seg1.getPonto1(), seg1.getPonto2(), seg2.getPonto2())
    o3 = orientation(seg2.getPonto1(), seg2.getPonto2(), seg1.getPonto1())
    o4 = orientation(seg2.getPonto1(), seg2.getPonto2(), seg1.getPonto2())

    if ((o1 != o2) and (o3 != o4)):
        return True

    if ((o1 == 0) and (onSegment(seg1.getPonto1(), seg2.getPonto1(), seg1.getPonto2()))):
        return True

    if ((o2 == 0) and (onSegment(seg1.getPonto1(), seg2.getPonto2(), seg1.getPonto2()))):
        return True

    if ((o3 == 0) and (onSegment(seg2.getPonto1(), seg1.getPonto1(), seg2.getPonto2()))):
        return True

    if ((o4 == 0) and (onSegment(seg2.getPonto1(), seg1.getPonto2(), seg2.getPonto2()))):
        return True

    return False

#============================================================================================
#area de um poligono
def area(p1: Ponto, p2 : Ponto, p3 : Ponto):
    a = []
    for i in range(5):
        a.append([0] * 5)
    a[0][0] = p1.getX()
    a[1][0]= p1.getY()
    a[2][0] = 1

    a[0][1] = p2.getX()
    a[1][1] = p2.getY()
    a[2][1] = 1

    a[0][2] = p3.getX()
    a[1][2] = p3.getY()
    a[2][2] = 1

    a[0][3] = p2.getX()
    a[1][3] = p2.getY()
    a[2][3] = 1

    a[0][4] = p3.getX()
    a[1][4] = p3.getY()
    a[2][4] = 1

    x = (a[0][0] * a[1][1] * a[2][2]) + (a[1][0] * a[2][1] * a[3][2]) + (a[2][0] * a[3][1] * a[4][2])
    y = (a[0][2] * a[1][1] * a[2][0]) + (a[1][2] * a[2][1] * a[3][0]) + (a[2][2] * a[3][1] * a[4][0])
    return (x - y)

def polignoArea(pol : Poligono):
    lista = pol.conjuntoSegmentos.RetornaConjuntoEmLista()
    if(len(lista)<3):
        return 0
    p = copy.deepcopy(lista[0].getPonto1())
    A = 0
    i = 1
    while (i<len(lista)):
        det = area(p,lista[i].getPonto1(),lista[i].getPonto2())
        if (det < 0):
            det = det * (-1)
        A = A + det*(1/2)
        i += 1
    return A



#def isleft(p0: Ponto, p1: Ponto ,p2: Ponto):
 #       return ((p1.getX()- p0.getX()) * (p2.getY()- p0.getY()) - (p2.getX() - p0.getX()) * (p1.getY()- p0.getY()))


#predicao convexidade de um poligono
def predicado_convexidade_poligono(poligono:Poligono):
    if (len(poligono.listaPonto) < 3):
        return False
    res = 0
    for i in range (len(poligono.listaPonto)):
        p = poligono.listaPonto[i]
        tmp = poligono.listaPonto[((i + 1) % len(poligono.listaPonto))]
        vx = tmp[0] - p[0]
        vy = tmp[1] - p[1]
        v = Ponto(vx,vy)
        u = poligono.listaPonto[((i + 2) % len(poligono.listaPonto))]

        if (i == 0): #in first loop direction is unknown, so save it in res
            res = u[0] * v.getY() - u[1] * v.getX() + v.getX() * p[1] - v.getY() * p[0]
        else:
            newres = u[0] * v.getY()- u[1] * v.getX() + v.getX() * p[1] - v.getY() * p[0]
            if ( (newres > 0 and res < 0) or (newres < 0 and res > 0) ):
               return False
    return True

#=====================================================================================================


def plotaPontoMaisProximoSegmento(segmento: Segmento, ponto : Ponto, pontoconjunto: Conjunto):
    plt.scatter(segmento.getPonto1().getX(), segmento.getPonto1().getY(), color='black')
    plt.scatter(segmento.getPonto2().getX(), segmento.getPonto2().getY(), color='black')
    lista = pontoconjunto.RetornaConjuntoEmLista()
    for i in range(len(lista)):
        if( not((lista[i].getX()== ponto.getX()) and (lista[i].getY()== ponto.getY())) ):
            plt.scatter(lista[i].getX(), lista[i].getY(), color='black')

    plt.scatter(ponto.getX(), ponto.getY(), color='blue')
    plt.plot([segmento.getPonto1().getX(), segmento.getPonto2().getX()], [segmento.getPonto1().getY(), segmento.getPonto2().getY()], zorder=2, color='red')
    plt.ylabel('Ponto mais próximo do segmento')
    plt.show()


#dobra de polígonos
def getEar(poly):
    size = len(poly)
    if size < 3:
        return []
    if size == 3:
        tri = (poly[0], poly[1], poly[2])
        del poly[:]
        return tri
    for i in range(size):
        tritest = False
        p1 = poly[(i - 1) % size]
        p2 = poly[i % size]
        p3 = poly[(i + 1) % size]
        if IsConvex(p1, p2, p3):
            for x in poly:
                if not (x in (p1, p2, p3)) and InTriangle(p1, p2, p3, x):
                    tritest = True
            if tritest == False:
                del poly[i % size]
                return (p1, p2, p3)
    print('GetEar(): no ear found')
    return []


#metodos auxiliares do triangulação


def IsConvex(a, b, c):
    # only convex if traversing anti-clockwise!
    crossp = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if crossp >= 0:
        return True
    return False

def InTriangle(a, b, c, p):
    L = [0, 0, 0]
    eps = 0.0000001
    # calculate barycentric coefficients for point p
    # eps is needed as error correction since for very small distances denom->0
    L[0] = ((b[1] - c[1]) * (p[0] - c[0]) + (c[0] - b[0]) * (p[1] - c[1])) \
           / (((b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])) + eps)
    L[1] = ((c[1] - a[1]) * (p[0] - c[0]) + (a[0] - c[0]) * (p[1] - c[1])) \
           / (((b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])) + eps)
    L[2] = 1 - L[0] - L[1]
    # check if p lies in triangle (a, b, c)
    for x in L:
        if x >= 1 or x <= 0:
            return False
    return True


def IsClockwise(poly):
    # initialize sum with last element
    sum = (poly[0][0] - poly[len(poly)-1][0]) * (poly[0][1] + poly[len(poly)-1][1])
    # iterate over all other elements (0 to n-1)
    for i in range(len(poly)-1):
        sum += (poly[i+1][0] - poly[i][0]) * (poly[i+1][1] + poly[i][1])
    if sum > 0:
        return True
    return False





# Ponto dentro do poligono
def point_inside_polygon(ponto:Ponto, poly, include_edges=True):
    x = ponto.getX()
    y = ponto.getY()
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(1, n + 1):
        p2x, p2y = poly[i % n]
        if p1y == p2y:
            if y == p1y:
                if min(p1x, p2x) <= x <= max(p1x, p2x):
                    # point is on horisontal edge
                    inside = include_edges
                    break
                elif x < min(p1x, p2x):  # point is to the left from current edge
                    inside = not inside
        else:  # p1y!= p2y
            if min(p1y, p2y) <= y <= max(p1y, p2y):
                xinters = (y - p1y) * (p2x - p1x) / float(p2y - p1y) + p1x

                if x == xinters:  # point is right on the edge
                    inside = include_edges
                    break

                if x < xinters:  # point is to the left from current edge
                    inside = not inside

        p1x, p1y = p2x, p2y

    return inside

