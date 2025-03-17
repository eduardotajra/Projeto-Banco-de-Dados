from Tupla import Tupla

class Pagina:
    capacidade = 15
    def __init__(self, capacidade : int = 15):
        self.capacidade = capacidade
        self.listaTuplas = []

    @staticmethod
    def setNovaTupla(listaPaginas, tupla: Tupla):
        if not listaPaginas:
            nova_pagina = Pagina()
            nova_pagina.listaTuplas.append(tupla)
            listaPaginas.append(nova_pagina)
        else:
            ultima_pagina = listaPaginas[-1]
            if len(ultima_pagina.listaTuplas) < ultima_pagina.capacidade:
                ultima_pagina.listaTuplas.append(tupla)
            else:
                nova_pagina = Pagina(ultima_pagina.capacidade)
                nova_pagina.listaTuplas.append(tupla)
                listaPaginas.append(nova_pagina)

    


    
    def getListaTuplas(self):
        return self.listaTuplas

    @staticmethod
    def getCapacidade():
        return Pagina.capacidade

    

        