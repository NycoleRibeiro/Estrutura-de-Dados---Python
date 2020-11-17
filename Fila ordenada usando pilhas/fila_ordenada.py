from node import Node
from pilha import Pilha


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def consultar(self):
        """Mostra o item no inicio da fila"""
        if self.inicio:
            return self.inicio.dado
        else:
            return None

    def inserir(self, dado):
        novo = Node(dado)
        if not self.inicio:
            self.inicio = novo
        else:
            self.fim.pos_seguinte = novo
        self.fim = novo

    def excluir(self):
        if self.inicio:
            self.inicio = self.inicio.pos_seguinte

    def destruir(self):
        while self.inicio:
            self.excluir()

    def mostrar_fila(self):
        """mostra todos itens na fila"""
        if self.inicio:
            r = ""
            pointer = self.inicio
            while(pointer):
                r = r + str(pointer.dado) + " "
                pointer = pointer.pos_seguinte
            return r
        else:
            return "Lista vazia!"

    def ordenar(self):
        stack = Pilha()
        stack2 = Pilha()
        while self.inicio is not None:
            if stack.consultar() is None:
                stack.inserir(self.inicio.dado)
                self.excluir()
            else:
                while self.inicio.dado > stack.consultar():
                    stack2.inserir(stack.topo.dado)
                    stack.remover()
                    if stack.consultar() is None:
                        break
                stack.inserir(self.inicio.dado)
                self.excluir()
                while stack2.consultar() is not None:
                    stack.inserir(stack2.topo.dado)
                    stack2.remover()
        while stack.consultar() is not None:
            self.inserir(stack.topo.dado)
            stack.remover()
        return self.mostrar_fila()


# testes
queue = Fila()
queue.inserir(1.7)
queue.inserir(4.4)
queue.inserir(3.2)
queue.inserir(6.1)
queue.inserir(3.1)
queue.inserir(5.8)
queue.inserir(2)

print(">> Fila inicial <<")
print(queue.mostrar_fila())
print("\n>> Fila ordenada <<")
print(queue.ordenar())
