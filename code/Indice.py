from Bucket import Bucket

class Indice:
    def __init__(self):
        self.indice = {}

    @staticmethod
    def getHash(chaveBusca):
        return hash(chaveBusca)
    
    def addBucket(self, bucket):
        bucketHash = self.getHash(bucket.getChaveBusca())
        if f"{bucketHash}" in self.indice:
            self.setBucketUltimoNo(bucket, bucketHash)
        else:
            self.addLinhaIndice(bucketHash, bucket)

    def addValorBucket(self, chaveBusca, enderecoPagina):
        bucketRaiz  = self.busca(chaveBusca)
        ultimo = self.getUltimoNo(bucketRaiz)
        if ultimo.estaCheio():
            self.addBucket(Bucket(chaveBusca, enderecoPagina))
        else:
            ultimo.bucket[f"{chaveBusca}"] = enderecoPagina
            ultimo.tamanho_atual += 1
        

    def addLinhaIndice(self, hashCode, bucket):
        self.indice[f"{hashCode}"] = bucket
            

    def busca(self, chaveBusca):
        return self.indice[f"{self.getHash(chaveBusca)}"]

    @staticmethod
    def setBucketUltimoNo(self, bucket, bucketHash):
        noRaiz = self.indice[f"{bucketHash}"]
        ultimoNo = self.getUltimoNo(noRaiz)
        ultimoNo.setNext(bucket)

    def getUltimoNo(self, noRaiz):
        nextBucket = noRaiz.getNext()
        while nextBucket is not None:
            nextBucket = nextBucket.getNext()
        return nextBucket



