class Tupla:
    
    def __init__(self, chaveBusca, dados):
        self.chaveBusca = chaveBusca
        self.dados = dados

    def getDados(self):
        return self.dados
    
    def getChaveBusca(self):
        return self.chaveBusca