import time
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

# Medindo o tempo de execução do tableScan
inicio_tableScan = time.perf_counter()
resultado_tableScan = Tabela.tableScan(chave, listaPaginas)
fim_tableScan = time.perf_counter()
tempo_tableScan = (fim_tableScan - inicio_tableScan) * 1000  # converte para milissegundos

inicio_buscaPorCB = time.perf_counter()
resultado_buscaPorCB = Tabela.buscaPorCB(chave, Indice, listaPaginas)
fim_buscaPorCB = time.perf_counter()
tempo_buscaPorCB = (fim_buscaPorCB - inicio_buscaPorCB) * 1000  # converte para milissegundos

print("Resultado do TableScan:", resultado_tableScan)
print("Tempo do TableScan: {:.3f} ms".format(tempo_tableScan))

print("Resultado da BuscaPorCB:", resultado_buscaPorCB)
print("Tempo da BuscaPorCB: {:.3f} ms".format(tempo_buscaPorCB))

print(f"Taxa de colisao: {Indice.getColisao(len(conteudoArquivo)) *100}%")
print(f"Taxa de overflow: {Indice.getOverflow()*100}%")

print("Indices:" + Indice.indice)


bp = 1