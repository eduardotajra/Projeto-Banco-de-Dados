from Bucket import Bucket

class Indice:
    indice = {}
    colisao = 0 # colisao / len(conteudoArquivo)
    overflow = 0 # overflow /colisao

    @staticmethod
    def getHash(chaveBusca):
        # return hash(chaveBusca)
        return len(chaveBusca)
    
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
            Indice.overflow += 1
            Indice.addBucket(Bucket(chaveBusca, enderecoPagina))
        else:
            ultimo.bucket[f"{chaveBusca}"] = enderecoPagina
            Indice.colisao +=1
            ultimo.tamanho_atual += 1
        
    @staticmethod
    def addLinhaIndice(hashCode, bucket):
        Indice.indice[f"{hashCode}"] = bucket
            
    @staticmethod
    def busca(chaveBusca):
        return Indice.indice.get(f"{Indice.getHash(chaveBusca)}")

    @staticmethod
    def setBucketUltimoNo(bucket, bucketHash):
        noRaiz = Indice.indice[f"{bucketHash}"]
        ultimoNo = Indice.getUltimoNo(noRaiz)
        ultimoNo.setNext(bucket)

    def getUltimoNo(noRaiz):
        teste = 0
        if noRaiz.getNext() == None:
            return noRaiz
        nextBucket = noRaiz.getNext()
        while nextBucket.getNext() is not None:
            teste += 1
            nextBucket = nextBucket.getNext()
        return nextBucket



