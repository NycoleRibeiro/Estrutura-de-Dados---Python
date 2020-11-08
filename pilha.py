from node import Node


class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def inserir(self, elem):
        """insere um elemento na pilha"""
        node = Node(elem)
        node.pos_seguinte = self.topo
        self.topo = node
        self.tamanho += 1

    def remover(self):
        """remove o elemento do topo da pilha"""
        if self.tamanho > 0:
            node = self.topo
            self.topo = self.topo.pos_seguinte
            self.tamanho -= 1
            return node
        else:
            return "A lista está vazia"

    def consulta(self):
        """retorna o inicio sem remover"""
        pass

    def tamanho(self):
        """Retorna o tamanho da lista"""
        return self.tamanho

    def mostrar_pilha(self):
        """mostra todos itens na pilha"""
        pass


# Testes
