

class Bucket:
    def __init__(self, chaveBusca, enderecoPagina):
        self.chaveBusca = f"{chaveBusca}"
        self.enderecoPagina = enderecoPagina
        self.bucket = {
            self.chaveBusca : self.enderecoPagina,
        }
        self.tamanho_atual = 1
        self.fr = 10000
        self.next : Bucket = None

    def getChaveBusca(self):
        return self.chaveBusca
    
    def estaCheio(self):
        if self.tamanho_atual == self.fr:
            return True
        else:
            return False

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next