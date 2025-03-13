from Node import Node

class Indice:
    def __init__(self):
        self.indice = {}
        self.listaEncadeada = []

    @staticmethod
    def getHash(chaveBusca):
        return hash(chaveBusca)
    
    def addBucket(self, bucket):
        no = Node(bucket)
        if len(self.listaEncadeada) == 0:
            self.listaEncadeada.append(no)
        else:
            ultimo = self.listaEncadeada[-1]
            ultimo.setNext(no)
            self.listaEncadeada.append(no)

    def addLinhaIndice(self, hashCode,listaEncadeada):
        if f"{hashCode}" in self.indice:
            print("Já existe essa chave hash nesse indice")
        else:
            self.indice[f"{hashCode}"] = listaEncadeada


    def busca(self, chaveBusca):
        return self.indice[f"{self.getHash(chaveBusca)}"]



