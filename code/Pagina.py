from Tupla import Tupla

class Pagina:
    tuplas : list[Tupla]
    capacidade : int

    def _init_(self, capacidade):
        self.tuplas = []
        self.capacidade = capacidade

    def setNovaTupla(self, tupla):
        if len(self.tuplas) < self.capacidade:
            self.tuplas.append(tupla)
        else:
            print('Página chegou à capacidade máxima.')