from Indice import Indice

class Bucket:
    def _init_(self, chaveBuscaPagina, enderecoPagina):
        self.chaveBuscaPagina = chaveBuscaPagina
        self.enderecoPagina = enderecoPagina
        self.bucket = {
            chaveBuscaPagina : enderecoPagina,
        }
        self.fr = 0
        self.proximoBucket = 0

    def addLinha(self, chaveBuscaPagina, enderecoPagina):
        if self.fr < 16:
            self.bucket[chaveBuscaPagina] = enderecoPagina
        else:
            Indice.addBucket(Bucket(chaveBuscaPagina, enderecoPagina))

