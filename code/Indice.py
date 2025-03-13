from Node import Node

class Indice:
    def __init__(self):
        self.indice = {}
        self.listaEncadeada = []

    def getHash(chaveBusca):
        return hash(chaveBusca)
    
    def addBucket(self, bucket):
        if self.listaEncadeada.length == 0:
            self.listaEncadeada.append(Node(bucket))
        else:
            self.listaEncadeada[self.listaEncadeada.length-1].setNext(bucket)

    def addLinhaIndice(self, hashCode,listaEncadeada):
        if f"{hashCode}" in self.indice:
            print("Já existe essa chave hash nesse indice")
        else:
            self.indice[f"{hashCode}"] = listaEncadeada


    def busca(self, chaveBusca):
        return self.indice[f"{getHash(chaveBusca)}"]



