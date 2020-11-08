class Node:
    def __init__(self, dado):
        self.dado = dado
        self.pos_seguinte = None


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
        

    def consulta(self):
        # retorna o inicio sem remover
        

    def tamanho(self):
        """Retorna o tamanho da lista"""
        


A = Fila()