from lista import Lista

lista = Lista()

lista.adicionar(1)
lista.adicionar(2, inicio=True)
lista.adicionar(3)
lista.adicionar(4, inicio=True)
lista.adicionar(5)
lista.adicionar(6)
lista.adicionar(7, inicio=True)
lista.adicionar(8)
lista.adicionar(9, inicio=True)

lista.show()

lista.remover(3)
lista.remover(8)
lista.remover(6)

lista.show()