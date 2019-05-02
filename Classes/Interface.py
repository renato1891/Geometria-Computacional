import tkinter as tk
from ProblemasClassicos.ProblemasClassicos import *
from ParMaisProximo.parMaisProximo import *
from Voronoi.Voronoi import *
from Fecho.Fecho import *
from MetodosOrdenacao.MetodosOrdenacao import *


class MainWindow:
    # radius of drawn points on canvas
    RADIUS = 3

    # flag to lock the canvas when drawn
    LOCK_FLAG = False

    # flag poligono "se está montando o poligono"
    POLIGONO_FLAG = False


    def __init__(self, master):
        self.master = master
        self.master.title("Menu")

        self.frm1 = tk.Frame(self.master)
        self.frm1.pack()

        self.frmMain = tk.Frame(self.frm1, relief=tk.RAISED, borderwidth=1)
        self.frmMain.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)

        self.w = tk.Canvas(self.frmMain, width=1000, height=700)
        self.w.config(background='white')
        self.w.bind('<Double-1>', self.onDoubleClick)
        self.w.pack(side=tk.RIGHT)

        self.frmButton = tk.Frame(self.master)
        self.frmButton.pack(side=tk.BOTTOM)

        self.frmMenu = tk.Frame(self.frm1)
        self.frmMenu.pack(side=tk.RIGHT)

        self.btnProximoSegmento = tk.Button(self.frmMenu, text="Ponto proximo segmento", width=25, command=self.onPontoMaisProximodoSegmento)
        self.btnProximoSegmento.pack(side=tk.TOP)

        self.btnVoronoi = tk.Button(self.frmMenu, text="Voronoi", width=25, command=self.onVoronoi)
        self.btnVoronoi.pack(side=tk.TOP)

        self.btnParmaisProximo = tk.Button(self.frmMenu, text='Par mais proximo', width=25, command=self.onParmaixproximo)
        self.btnParmaisProximo.pack(side=tk.TOP)

        self.btnDobraOrelhas = tk.Button(self.frmMenu, text='Dobrar Poligono', width=25,command=self.onDobrarPoligono)
        self.btnDobraOrelhas.pack(side=tk.TOP)

        self.btnPontoDentro = tk.Button(self.frmMenu, text='Ponto dentro', width=25, command=self.onPontoDentro)
        self.btnPontoDentro.pack(side=tk.TOP)

        self.btnFecho = tk.Button(self.frmMenu, text='Fecho', width=25, command=self.onFecho)
        self.btnFecho.pack(side=tk.TOP)

        self.btnIntersection = tk.Button(self.frmMenu, text='Intersection', width=25, command=self.onIntersection)
        self.btnIntersection.pack(side=tk.TOP)

        self.btn2D = tk.Button(self.frmMenu, text='Orientação 2D', width=25, command=self.on2D)
        self.btn2D.pack(side=tk.TOP)

        self.btnConvexidade = tk.Button(self.frmMenu, text='Convexidade', width=25, command=self.onConvexidade)
        self.btnConvexidade.pack(side=tk.TOP)

        self.btnCirculo = tk.Button(self.frmMenu, text='Circulo', width=25, command=self.onCirculo)
        self.btnCirculo.pack(side=tk.TOP)

        self.btnSideCirculo = tk.Button(self.frmMenu, text='Lado circulo', width=25, command=self.onSideCirculo)
        self.btnSideCirculo.pack(side=tk.TOP)

        self.btnPonto = tk.Button(self.frmButton, text='Adicionar Pontos', width=15, command=self.onCriaPontos)
        self.btnPonto.pack(side=tk.LEFT)

        self.btnClear = tk.Button(self.frmButton, text='Limpar canvas', width=15, command=self.onClickClear)
        self.btnClear.pack(side=tk.LEFT)

        self.btnSegmento = tk.Button(self.frmButton, text='Adicionar segmentos', width=15, command=self.onCriaSegmento)
        self.btnSegmento.pack(side=tk.LEFT)

        self.btnPoligono = tk.Button(self.frmButton, text='Adicionar polignos', width=15, command=self.onCriaPoligono)
        self.btnPoligono.pack(side=tk.LEFT)

        self.btnTerminaPoligono = tk.Button(self.frmButton, text='Termina Poligono', width=15, command=self.onTerminaPoligono)
        self.btnTerminaPoligono.pack(side=tk.LEFT)



        self.pts = []

        self.conjuntoPontos = Conjunto(MetodoPontoOrdena)
        self.conjuntoSegmentos = Conjunto(MetodoSegmentoOrdena)
        self.primeiroPonto = None
        self.ultimoPonto = None
        self.ultimo = None
        self.poligono = None
        self.circulo = None

    def onCriaPontos(self):
        #if not self.LOCK_FLAG:
         #   self.LOCK_FLAG = True
            pObj = self.w.find_all()
            for i in range(len(self.pts)):
                ponto = Ponto(self.pts[i][0],self.pts[i][1] )
                self.conjuntoPontos.Insert(ponto)
            self.pts.clear()


    def onCriaSegmento(self):
            tamanho = len(self.pts)
            ponto1 = None
            ponto2 = None
            if(tamanho>2):
                for i in range(len(self.pts)):
                    self.w.create_line(self.pts[i][0], self.pts[i][1], self.pts[(i+1) % tamanho][0], self.pts[(i+1) % tamanho][1], fill='blue')
                    ponto1 = Ponto(self.pts[i][0],self.pts[i][1])
                    ponto2 = Ponto(self.pts[(i+1) % tamanho][0],self.pts[(i+1) % tamanho][1])
                    segmentoaux = Segmento(ponto1, ponto2)
                    self.ultimo = Segmento(ponto1,ponto2)
                    self.conjuntoSegmentos.Insert(segmentoaux)
            else:
                ponto1 = Ponto(self.pts[0][0], self.pts[0][1])
                ponto2 = Ponto(self.pts[1][0], self.pts[1][1])
                self.ultimo = Segmento(ponto1, ponto2)
                segmentoaux = Segmento(ponto1, ponto2)
                self.conjuntoSegmentos.Insert(segmentoaux)
                self.w.create_line(self.pts[0][0], self.pts[0][1], self.pts[1][0],self.pts[1][1], fill='blue')

            self.pts.clear()
            #self.conjuntoSegmentos.PrintaConjunto()

    def onParmaixproximo(self):
        self.LOCK_FLAG = True
        pObj = self.w.find_all()
        a =  closestpair(self.conjuntoPontos)
        ax1 = a[0][0]
        ax2 = a[1][0]
        ay1 = a[0][1]
        ay2 = a[1][1]
        self.w.create_line(ax1, ay1, ax2, ay2, fill='blue')

    def onPontoMaisProximodoSegmento(self):
        a= copy.deepcopy(ponto_mais_proximo(self.ultimo,self.conjuntoPontos))
        self.w.create_text(a.getX(),(a.getY()-10), text= "!", fill='red')

    def onCriaPoligono(self):
        self.POLIGONO_FLAG = True
        if ((self.primeiroPonto is None)):
            self.primeiroPonto = Ponto(self.pts[0][0],self.pts[0][1])
        if(not(self.ultimoPonto is None)):
            ponto1 = Ponto(self.ultimoPonto.getX(), self.ultimoPonto.getY())
            ponto2 = Ponto(self.pts[0][0], self.pts[0][1])
            self.w.create_line(self.ultimoPonto.getX(), self.ultimoPonto.getY(), self.pts[0][0],
                               self.pts[0][1], fill='blue')
            segmento = Segmento(ponto1,ponto2)
            if (self.poligono is None):
                self.poligono = Poligono(segmento,MetodoSegmentoOrdena)
            else:
                self.poligono.addSegmento(segmento)
            self.conjuntoSegmentos.Insert(segmento)
            self.ultimoPonto = Ponto(self.pts[0][0], self.pts[0][1])
        else:
            self.ultimoPonto = Ponto(self.pts[0][0], self.pts[0][1])

        self.pts.clear()

    def onTerminaPoligono(self):
        ponto1 = Ponto(self.ultimoPonto.getX(), self.ultimoPonto.getY())
        ponto2 = Ponto(self.primeiroPonto.getX(), self.primeiroPonto.getY())
        segmento = Segmento(ponto1, ponto2)
        self.poligono.addSegmento(segmento)
        self.conjuntoSegmentos.Insert(segmento)
        self.w.create_line(ponto1.getX(), ponto1.getY(), ponto2.getX(),
                           ponto2.getY(), fill='blue')

        self.POLIGONO_FLAG = False
        self.pts.clear()

    def onVoronoi(self):
        self.onCriaPontos()
        vp = Voronoi(self.conjuntoPontos)
        vp.process()
        lines = vp.get_output()
        self.drawLinesOnCanvas(lines)

    def onDobrarPoligono(self):
        pontos = copy.deepcopy(self.poligono.listaPonto)
        lista = pontos[::-1] if IsClockwise(pontos) else pontos[:]
        while len(lista) >= 3:
            a = getEar(lista)
            if a == []:
                break
            self.w.create_line(a[0][0], a[0][1], a[1][0], a[1][1], fill='blue')
            self.w.create_line(a[0][0], a[0][1], a[2][0], a[2][1], fill='blue')
            self.w.create_line(a[1][0], a[1][1], a[2][0], a[2][1], fill='blue')

    def onFecho(self):
        ch = ConvexHull(self.conjuntoPontos)
        a = ch.get_hull_points()
        tamanho = len(a)
        for i in range(len(a)):
            #print(x.x,x.y)
            self.w.create_line(a[i].x, a[i].y, a[(i+1) % tamanho].x,
                               a[(i+1) % tamanho].y, fill='blue')

    def onPontoDentro(self):
        listapontos = self.conjuntoPontos.RetornaConjuntoEmLista()
        b = self.poligono.listaPonto
        a = point_inside_polygon(listapontos[0],b,True)
        if (a==1):
            self.w.create_text(listapontos[0].getX(), (listapontos[0].getY() - 10), text="Está dentro", fill='red')
        else :
            self.w.create_text(listapontos[0].getX(), (listapontos[0].getY() - 10), text="Não está dentro", fill='red')

    def onIntersection(self):
        seg = self.conjuntoSegmentos.RetornaConjuntoEmLista()
        #a = intersect(seg[0].ponto1,seg[0].ponto2, seg[1].ponto1,seg[1].ponto2)
        a = doIntersect(seg[0],seg[1])
        if(a):
            self.w.create_text(400, 400, text="Intersecta", fill='red')
        else:
            self.w.create_text(400,400, text="Não intersecta", fill='red')

    def on2D(self):
        ponto1 = Ponto(self.pts[0][0],self.pts[0][1])
        ponto2 = Ponto(self.pts[1][0], self.pts[1][1])
        ponto3 = Ponto(self.pts[2][0], self.pts[2][1])
        a = orientation(ponto1,ponto2,ponto3)
        if(a==0):
            self.w.create_text(400, 400, text="Colinear", fill='red')
        if(a==1):
            self.w.create_text(400, 400, text="Esquerda", fill='red')
        if(a==2):
            self.w.create_text(400, 400, text="Direita", fill='red')

        self.pts.clear()

    def onConvexidade(self):
        a= predicado_convexidade_poligono(self.poligono)
        if(a):
            self.w.create_text(400, 400, text="Convexo", fill='red')
        else:
            self.w.create_text(400, 400, text="Não convexo", fill='red')


    def onCirculo(self):
        centro = Ponto(self.pts[0][0],self.pts[0][1])
        ponto = Ponto(self.pts[1][0],self.pts[1][1])
        raio =  distance(centro,ponto)
        self.circulo = Circulo(centro,raio)
        self.w.create_line(self.pts[0][0], self.pts[0][1], self.pts[1][0], self.pts[1][1], fill='blue')
        self.w.create_oval(self.circulo.centro.x - raio,self.circulo.centro.y - raio,
                           self.circulo.centro.x + raio,self.circulo.centro.y + raio)
        self.pts.clear()

    def onSideCirculo(self):
        ponto = Ponto(self.pts[0][0],self.pts[0][1])
        text = sideCircle(self.circulo,ponto)
        self.w.create_text(400, 400, text=text , fill='red')
        self.pts.clear()




    def onClickClear(self):
        self.LOCK_FLAG = False
        self.POLIGONO_FLAG = False
        self.w.delete(tk.ALL)
        del(self.conjuntoPontos)
        del(self.conjuntoSegmentos)
        self.pts.clear()
        self.conjuntoPontos = Conjunto(MetodoPontoOrdena)
        self.conjuntoSegmentos = Conjunto(MetodoSegmentoOrdena)
        self.primeiroPonto = None
        self.ultimoPonto = None
        self.ultimo = None
        self.poligono = None
        self.circulo = None




    def onDoubleClick(self, event):
        if not self.LOCK_FLAG:
            self.w.create_oval(event.x - self.RADIUS, event.y - self.RADIUS, event.x + self.RADIUS,
                               event.y + self.RADIUS, fill="black")
            self.pts.append((event.x, event.y))
            if self.POLIGONO_FLAG:
                self.onCriaPoligono()

    def drawLinesOnCanvas(self, lines):
        for l in lines:
            self.w.create_line(l[0], l[1], l[2], l[3], fill='blue')

