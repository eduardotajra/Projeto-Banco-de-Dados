class Tupla:
    
    def _init_(self, chaveBusca, dados):
        self.chaveBusca = chaveBusca
        self.dados = dados

    def getDados(self):
        return self.dados