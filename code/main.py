from Tupla import Tupla
from Indice import Indice
from Tabela import Tabela
from Pagina import Pagina
from Bucket import Bucket


tabelaPrincipal = Tabela('tabelaPrincipal')
listaPaginas = []
with open('words.txt', 'r') as arquivo:
    conteudoArquivo = arquivo.read().split()

rep = 0
for linha in conteudoArquivo:
    novaTupla = Tupla(linha, linha)

    tabelaPrincipal.setTupla(novaTupla)

    Pagina.setNovaTupla(listaPaginas, novaTupla)

    enderecoPagina = int(rep / Pagina.getCapacidade())
    
    Indice.addValorBucket(linha, enderecoPagina)
    rep += 1

chave = input("Digite a chave de busca: ")

print(Tabela.tableScan(chave, listaPaginas))

print(Tabela.buscaPorCB(chave, Indice, listaPaginas))

# print("Indices:" + Indice.indice)

bp = 1
