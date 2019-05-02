from Arvore.Arvore import arvbin

class Conjunto():
    Arv  = None

    def __init__(self, funcao):
        self.funcao = funcao
        self.Arv = arvbin(self.funcao)


    def Insert(self, elemento):
        self.Arv.put(elemento)

    def Member(self,elemento):
        teste = self.Arv.get(elemento)
        if teste == None:
            return False
        else:
            return True


    def RetornaConjunto(self):
        return self.Arv

    def RetornaConjuntoEmLista(self):
        return self.Arv.retorna_em_lista()


    def Intercection(conjunto1,conjunto2):
        arvore = arvbin.arv_Intercection(conjunto1.RetornaConjunto(), conjunto2.RetornaConjunto(), None)
        if(not(arvore is None)):
            arvore.printaArvore()


    def Union(conjunto1,conjunto2):
        arvore = arvbin.arv_Union(conjunto1.RetornaConjunto(), conjunto2.RetornaConjunto(), None)
        arvore.printaArvore()


    def Difference(conjunto1,conjunto2):
        arvore = arvbin.arv_Difference(conjunto1.RetornaConjunto(), conjunto2.RetornaConjunto(), None)
        arvore.printaArvore()


    def PrintaConjunto(self):
        self.Arv.printaArvore()

    def Min(self):
        self.Arv.minArvore()


    def tamanho(self):
        return self.Arv.size

    def delete(self, elemento):
        self.Arv.delete(elemento)

    def find(self,elemento):
        return self.Arv.get(elemento)