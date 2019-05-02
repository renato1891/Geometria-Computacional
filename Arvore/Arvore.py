import copy



class nodo:
    def __init__(self,val,left=None,right=None, parent=None):
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,value, lc, rc):
        self.val = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current


    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


class arvbin:

    def __init__(self,metodo):
        self.root = None
        self.size = 0
        self.metodo = metodo

    def put(self, val):
        if self.root:
            self._put(val, self.root)
        else:
            self.root = nodo(val)
        self.size = self.size + 1

    def _put(self, valor, nodoatual):
        if self.metodo(valor,nodoatual.val)==-1:
            if nodoatual.hasLeftChild():
                self._put(valor, nodoatual.leftChild)
            else:
                nodoatual.leftChild = nodo(valor, parent=nodoatual)
        else:
            if nodoatual.hasRightChild():
                self._put(valor, nodoatual.rightChild)
            else:
                nodoatual.rightChild = nodo(valor,parent=nodoatual)

    def get(self, valor):
        if self.root:
            res = self._get(valor, self.root)
            if res:
                return res.val
            else:
                return None
        else:
            return None

    def _get(self, valor, nodoatual):
        if not nodoatual:
            return None
        elif (self.metodo(nodoatual.val, valor) == 0):
            return nodoatual
        elif self.metodo(valor,nodoatual.val)==-1:
            return self._get(valor, nodoatual.leftChild)
        else:
            return self._get(valor, nodoatual.rightChild)

    def arv_Intercection(self, conjuntoarv2, arv):
        if (self.root != None):
            arvore = self._arv_Intercection(self.root,conjuntoarv2, arv)
            return arvore

    
    def _arv_Intercection(self, nodoatual, conjuntoarv2, arv):
        if nodoatual.val:
            if(conjuntoarv2.get(nodoatual.val)):
                if(arv is None):
                    arv = arvbin(self.metodo)
                    arv.put(copy.deepcopy(nodoatual.val))
                else:
                    arv.put(copy.deepcopy(nodoatual.val))
        if nodoatual.hasLeftChild():
            return  self._arv_Intercection(nodoatual.leftChild,conjuntoarv2,arv)

        if nodoatual.hasRightChild():
            return   self._arv_Intercection(nodoatual.rightChild,conjuntoarv2,arv)
        return arv

    def arv_Union(self, conjuntoarv2, arv):
        if (self.root != None):
            arvore = self._arv_Union(self.root,conjuntoarv2, arv)
            return arvore

    def _arv_Union(self, nodoatual, conjuntoarv2, arv):
        if nodoatual.val:
            if(arv is None):
                arv = copy.deepcopy(conjuntoarv2)
            if(conjuntoarv2.get(nodoatual.val) is None):
                arv.put(copy.deepcopy(nodoatual.val))

        if nodoatual.hasLeftChild():
            return self._arv_Union(nodoatual.leftChild,conjuntoarv2,arv)

        if nodoatual.hasRightChild():
            return self._arv_Union(nodoatual.rightChild,conjuntoarv2,arv)
        return arv

    def arv_Difference(self, conjuntoarv2, arv):
        if (self.root != None):
            arvore = self._arv_Intercection(self.root, conjuntoarv2, arv)
            if(not(arvore is None)):
                arv = copy.deepcopy(self)
                lista = arvore.retorna_em_lista()
                for i in range(len(lista)):
                    if(arv.get(lista[i])):
                        arv.delete(lista[i])
                return arv
        return None


    def printaArvore(self):
        if(self.root != None):
            self._printaArvore(self.root)

    def _printaArvore(self, nodoatual):
        if (nodoatual):
            if nodoatual.hasLeftChild():
               self._printaArvore(nodoatual.leftChild)

            if nodoatual.val:
                nodoatual.val.printa()

            if nodoatual.hasRightChild():
                self._printaArvore(nodoatual.rightChild)

    def minArvore(self):
        if(self.root != None):
            self._minArvore(self.root)

    def _minArvore(self, nodoatual):
        if (nodoatual):
            if nodoatual.hasLeftChild():
               self._minArvore(nodoatual.leftChild)

            if(not(nodoatual.hasLeftChild)):
                return nodoatual.leftChild

    def _percorre_salva_lista(self, nodoatual, lista):
        if nodoatual.hasLeftChild():
            # print("esq")
            self._percorre_salva_lista(nodoatual.leftChild,lista)

        if nodoatual.val:
            lista.append(nodoatual.val)

        if nodoatual.hasRightChild():
            # print("dir")
            self._percorre_salva_lista(nodoatual.rightChild, lista)

        return lista

    def retorna_em_lista(self):
        lista = []

        lista = self._percorre_salva_lista(self.root,lista)
        return lista




    def delete(self, valor):
        if self.size > 1:
            nodeToRemove = self._get(valor, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.metodo(self.root.val,valor)==0:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, nodoAtual):
        if nodoAtual.isLeaf():  # leaf
            if nodoAtual == nodoAtual.parent.leftChild:
                nodoAtual.parent.leftChild = None
            else:
                nodoAtual.parent.rightChild = None
        elif nodoAtual.hasBothChildren():  # interior
            succ = nodoAtual.findSuccessor()
            succ.spliceOut()
            nodoAtual.val = succ.val

        else:  # this node has one child
            if nodoAtual.hasLeftChild():
                if nodoAtual.isLeftChild():
                    nodoAtual.leftChild.parent = nodoAtual.parent
                    nodoAtual.parent.leftChild = nodoAtual.leftChild
                elif nodoAtual.isRightChild():
                    nodoAtual.leftChild.parent = nodoAtual.parent
                    nodoAtual.parent.rightChild = nodoAtual.leftChild
                else:
                    nodoAtual.replaceNodeData(nodoAtual.leftChild.val,
                                              nodoAtual.leftChild.leftChild,
                                              nodoAtual.leftChild.rightChild)
            else:
                if nodoAtual.isLeftChild():
                    nodoAtual.rightChild.parent = nodoAtual.parent
                    nodoAtual.parent.leftChild = nodoAtual.rightChild
                elif nodoAtual.isRightChild():
                    nodoAtual.rightChild.parent = nodoAtual.parent
                    nodoAtual.parent.rightChild = nodoAtual.rightChild
                else:
                    nodoAtual.replaceNodeData(nodoAtual.rightChild.val,
                                              nodoAtual.rightChild.leftChild,
                                              nodoAtual.rightChild.rightChild)



