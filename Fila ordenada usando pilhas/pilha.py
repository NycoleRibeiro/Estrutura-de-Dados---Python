from node import Node


class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def consultar(self):
        """retorna o inicio sem remover"""
        if self.topo:
            return self.topo.dado
        else:
            return None

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
            return node.dado
        else:
            return None

    def tamanho(self):
        """Retorna o tamanho da lista"""
        return self.tamanho

    def mostrar_pilha(self):
        """mostra todos itens na pilha"""
        if self.topo:
            r = ""
            pointer = self.topo
            while(pointer):
                r = r + str(pointer.dado) + "\n"
                pointer = pointer.pos_seguinte
            return r
        else:
            return "Lista vazia!"
