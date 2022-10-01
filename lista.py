from node import Node


class Lista:
    inicio = None

    def __init__(self):
        self.inicio = None


    def adicionar(self, valor, inicio=False):
        if inicio:
            self.adicionar_no_inicio(valor)
        else:
            self.adicionar_no_fim(valor)

    def adicionar_no_inicio(self, valor):
        novo = Node(valor)
        novo.proximo = self.inicio
        self.inicio = novo

    def adicionar_no_fim(self, valor):
        if self.inicio == None:
            self.inicio = Node(valor, None)
        else:
            aux = self.inicio
            while aux.proximo != None:
                aux = aux.proximo

            aux.proximo = Node(valor, None)
            aux.proximo.anterior = aux

    def remover(self, valor):
        aux = self.inicio
        if aux.valor == valor:
            # aux.valor = None
            self.inicio = aux.proximo
        else:
            while aux.proximo != None:
                aux = aux.proximo
                if aux.valor == valor:
                    aux.anterior.proximo = aux.proximo

    def show(self):
        aux = self.inicio
        print("[", end='')
        while aux.proximo != None:
            print(f"{aux.valor}", end=', ')
            aux = aux.proximo
        print(f"{aux.valor}]")
