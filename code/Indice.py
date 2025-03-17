from Bucket import Bucket

class Indice:
    indice = {}

    @staticmethod
    def getHash(chaveBusca):
        return hash(chaveBusca)
    
    @staticmethod
    def addBucket(bucket):
        bucketHash = Indice.getHash(bucket.getChaveBusca())
        if f"{bucketHash}" in Indice.indice:
            Indice.setBucketUltimoNo(bucket, bucketHash)
        else:
            Indice.addLinhaIndice(bucketHash, bucket)

    @staticmethod
    def addValorBucket( chaveBusca, enderecoPagina):
        bucketRaiz  = Indice.busca(chaveBusca)
        if bucketRaiz is None:
            ultimo = None
        else:
            ultimo = Indice.getUltimoNo(bucketRaiz)
        if ultimo == None or ultimo.estaCheio():
            Indice.addBucket(Bucket(chaveBusca, enderecoPagina))
        else:
            ultimo.bucket[f"{chaveBusca}"] = enderecoPagina
            ultimo.tamanho_atual += 1
        
    @staticmethod
    def addLinhaIndice(hashCode, bucket):
        Indice.indice[f"{hashCode}"] = bucket
            
    @staticmethod
    def busca(chaveBusca):
        return Indice.indice.get(f"{Indice.getHash(chaveBusca)}")

    @staticmethod
    def setBucketUltimoNo(self, bucket, bucketHash):
        noRaiz = self.indice[f"{bucketHash}"]
        ultimoNo = self.getUltimoNo(noRaiz)
        ultimoNo.setNext(bucket)

    def getUltimoNo(noRaiz):
        nextBucket = noRaiz.getNext()
        while nextBucket is not None:
            nextBucket = nextBucket.getNext()
        return nextBucket



