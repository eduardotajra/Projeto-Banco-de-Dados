from Indice import Indice

class Bucket:
    def _init_(self, chaveBuscaPagina, enderecoPagina,fr = 16):
        self.chaveBuscaPagina = chaveBuscaPagina
        self.enderecoPagina = enderecoPagina
        self.bucket = {
            chaveBuscaPagina : enderecoPagina,
        }
        self.tamanho_atual = 0
        self.fr = fr
        self.proximoBucket = 0

    def addLinha(self, chaveBuscaPagina, enderecoPagina):
        if self.tamanho_atual < self.fr:
            self.bucket[chaveBuscaPagina] = enderecoPagina
        else:
            Indice.addBucket(Bucket(chaveBuscaPagina, enderecoPagina))

