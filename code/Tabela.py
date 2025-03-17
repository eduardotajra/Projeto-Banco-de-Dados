from Tupla import Tupla
from Indice import Indice

class Tabela:

    def __init__(self, nome):
        self.nome = nome
        self.listaTuplas : list[Tupla] = []

    def setTupla(self, valorLinhaArquivo):
        self.listaTuplas.append(Tupla(valorLinhaArquivo, valorLinhaArquivo))

    def getTodasTuplas(self):
        return self.listaTuplas

    def getNomeTabela(self):
        return self.nome
    
    def apontaEndPag(lista, enderecoPagina):
        return lista[enderecoPagina]

    @staticmethod
    def buscaPorCB(chaveBusca, Indice, ListaPag):
        bucket = Indice.busca(chaveBusca)
        endPag = bucket.bucket[chaveBusca]
        # for bucket in listaBuckets:
        #     if bucket.bucket.get(chaveBusca) == None:
        #         pass
        #     else:
        #         endPag = bucket.bucket.get(chaveBusca)
        #         break
        
        pagina = Tabela.apontaEndPag(ListaPag, endPag)
        listaTuplas = pagina.getListaTuplas()
        for tupla in listaTuplas:
            if tupla.getChaveBusca() == chaveBusca:
                return tupla.getDados()

    def tableScan(chaveBusca, listaPaginas):
        for pagina in listaPaginas:
            listaTuplas = pagina.getListaTuplas()
            for tupla in listaTuplas:
                if tupla.getChaveBusca() == chaveBusca:
                    return tupla.getDados()
        

        
    
    

