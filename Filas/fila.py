from node import Node


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir(self, elem):
        """insere um elemento na fila"""
        node = Node(elem)
        if self.fim is None:
            self.fim = node
        else:
            self.fim.pos_seguinte = node
            self.fim = node
        if self.inicio is None:
            self.inicio = node
        self.tamanho = self.tamanho + 1

    def remover(self):
        """remove o elemento do inicio da fila"""
        if self.inicio is not None:
            elem = self.inicio.dado
            self.inicio = self.inicio.pos_seguinte
            self.tamanho -= 1
            return elem
        else:
            return "A fila está vazia!"

    def consulta(self):
        """retorna o inicio sem remover"""
        if self.inicio is not None:
            elem = self.inicio.dado
            return elem
        else:
            return "A fila está vazia!"

    def tamanho(self):
        """Retorna o tamanho da lista"""
        return self.tamanho

    def mostrar_fila(self):
        """mostra todos itens na fila"""
        if self.tamanho > 0:
            r = ""
            pointer = self.inicio
            while(pointer):
                r = r + str(pointer.dado) + " "
                pointer = pointer.pos_seguinte
            return r
        else:
            return "A fila está vazia!"


# Testes
A = Fila()
A.inserir("A")
A.inserir("B")
A.inserir("C")
A.inserir("D")
A.inserir("E")
print(A.mostrar_fila())
print(A.consulta())

print(A.remover())
print(A.mostrar_fila())
print(A.consulta())
