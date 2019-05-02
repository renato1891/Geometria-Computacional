
from Classes.Interface import *
from MetodosOrdenacao.MetodosOrdenacao import *
root = tk.Tk()
app = MainWindow(root)
root.mainloop()










p = Ponto(3,-6)
p1 = Ponto(5,4)
p2 = Ponto(33,-16)
p3 = Ponto(3,1)
p4 = Ponto(-3,-6)
p5 = Ponto(5,2)
p6 = Ponto(47,20)
p7 = Ponto(11,14)

seg1= Segmento(p1,p2)

seg3= Segmento(p4,p5)


seg6 = Segmento(p4,p6)
seg4= Segmento(p3,p4)
seg2= Segmento(p2,p3)
seg5= Segmento(p6,p7)

conjuntoponto = Conjunto(MetodoPontoOrdena) # None ou nome da funcao
conjuntoponto.Insert(p2)
conjuntoponto.Insert(p1)
conjuntoponto.Insert(p4)
conjuntoponto.Insert(p5)

conjuntoponto2 = Conjunto(MetodoPontoOrdena) # None ou nome da funcao
conjuntoponto2.Insert(p)
conjuntoponto2.Insert(p2)
conjuntoponto2.Insert(p1)
conjuntoponto2.Insert(p4)
conjuntoponto2.Insert(p5)


conjuntoseg1 = Conjunto(MetodoSegmentoOrdena)
conjuntoseg1.Insert(seg5)
conjuntoseg1.Insert(seg6)

conjuntoseg2 = Conjunto(MetodoSegmentoOrdena)
conjuntoseg2.Insert(seg6)
conjuntoseg2.Insert(seg5)
conjuntoseg2.Insert(seg2)


conjuntoponto3 = Conjunto(MetodoPontoOrdena)
po1 = Ponto(0,0)
po2 = Ponto(7,6)
po3 = Ponto(2,20)
po4 = Ponto(12,5)
po5 = Ponto(16,16)
po6 = Ponto(5,8)
po7 = Ponto(19,7)
po8 = Ponto(14,22)
po9 = Ponto(8,19)
po10 = Ponto(7,29)
po11 = Ponto(10,11)
po12 = Ponto(1,13)
conjuntoponto3.Insert(po1)
conjuntoponto3.Insert(po2)
conjuntoponto3.Insert(po3)
conjuntoponto3.Insert(po4)
conjuntoponto3.Insert(po5)
conjuntoponto3.Insert(po6)
conjuntoponto3.Insert(po7)
conjuntoponto3.Insert(po8)
conjuntoponto3.Insert(po9)
conjuntoponto3.Insert(po10)
conjuntoponto3.Insert(po11)
conjuntoponto3.Insert(po12)



paux = Ponto(0,0)
conjuntoponto3.PrintaConjunto()
conjuntoponto3.delete(paux)
conjuntoponto3.PrintaConjunto()





