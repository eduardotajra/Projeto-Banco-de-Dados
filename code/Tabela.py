from Pagina import Pagina

class Table:
    paginas : list[Pagina]

    def _init_(self, nome, capacidadeTabela):
        self.nome = nome
        self.paginas = []
        self.capacidadeTabela = capacidadeTabela
        self.indice = {}

    def setNovaPagina(self, pagina):
        if len(self.paginas) < self.capacidadeTabela:
            self.paginas.append(pagina)
        else:
            print('A tabela chegou à capacidade máxima.')

    
    

