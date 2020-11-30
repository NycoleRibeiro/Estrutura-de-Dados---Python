class tabela:
    def __init__(self, tamanhoMax):
        self.chaves = [None] * (tamanhoMax + 1)
        self.valores = [None] * (tamanhoMax + 1)
        self.tamanho = 0
        self.fim = tamanhoMax

    def inserir_linear(self, chave, valor):
        # Caso a chave exista, substitui o valor daquela chave
        if chave in self.chaves:
            index = self.consulta_index(chave)
            self.valores[index] = valor
        else:
            # Caso a tabela esteja cheia
            if self.tamanho == self.fim:
                return None
            # Caso a tabela não esteja cheia, acrescenta na ultima posição
            else:
                self.chaves[self.tamanho] = chave
                self.valores[self.tamanho] = valor
                self.tamanho += 1

    def inserir_ordenada(self, chave, valor):
        # Caso a chave exista, substitui o valor daquela chave
        if chave in self.chaves:
            index = self.consulta_index(chave)
            self.valores[index] = valor
        else:
            # Caso a tabela esteja cheia
            if self.tamanho == self.fim:
                return None
            # Caso a tabela não esteja cheia
            else:
                # Caso a chave seja maior que a ultima chave da lista
                # ou caso a tabela esteja vazia
                # insere na próxima linha disponível
                if (self.tamanho == 0) or (self.chaves[self.tamanho-1] < chave):
                    self.chaves[self.tamanho] = chave
                    self.valores[self.tamanho] = valor
                else:
                    # Checa a tabela da ultima até a primeira linha
                    for i in range(self.tamanho-1, -1, -1):
                        key = self.chaves[i]
                        # Se a chave da linha for menor que a chave a ser
                        # acrescentada, a proxima linha recebe a chave e o valor
                        if key < chave:
                            self.chaves[i+1] = chave
                            self.valores[i+1] = valor
                            self.tamanho += 1
                            return
                        # senão a proxima linha recebe a linha anterior
                        self.chaves[i+1] = self.chaves[i]
                        self.valores[i+1] = self.valores[i]
                    # Se depois da checagem a chave não foi maior que nenhuma
                    # chave já presente na tabela, quer dizer que esta chave
                    # será adicionada a primeira linha da tabela
                    self.chaves[0] = chave
                    self.valores[0] = valor
                self.tamanho += 1

    def remover(self, chave):
        if chave in self.chaves:
            index = self.consulta_index(chave)
            if index < self.tamanho-1:
                for i in range(index, self.tamanho):
                    self.chaves[i] = self.chaves[i+1]
                    self.valores[i] = self.valores[i+1]
            # Para remover a ultima linha (não precisa deslocar)
            else:
                self.chaves[index] = None
                self.valores[index] = None
            self.tamanho -= 1
        # Caso a chave não exista
        else:
            return None

    def destruir(self):
        for i in range(self.tamanho):
            self.chaves[i] = None
            self.valores[i] = None
        self.tamanho = 0

    def consulta_valor(self, chave):
        """Retorna os valores da chave"""
        if self.tamanho > 0:
            if chave in self.chaves:
                index = self.consulta_index(chave)
                return self.valores[index]
        return None

    def consulta_index(self, chave):
        """Retorna a linha(posição) da chave"""
        if self.tamanho > 0:
            if chave in self.chaves:
                for i in range(self.tamanho):
                    if self.chaves[i] == chave:
                        return i
        return None

    def consulta_index_binaria(self, chave):
        if self.tamanho > 0:
            if chave in self.chaves:
                inicio = 0
                fim = self.tamanho - 1
                while inicio <= fim:
                    meio = (inicio + fim) // 2
                    if self.chaves[meio] == chave:
                        return meio
                    else:
                        if self.chaves[meio] < chave:
                            inicio = meio + 1
                        else:
                            fim = meio
        return None

    def mostrar_tabela(self):
        if self.tamanho > 0:
            tab = ""
            for i in range(0, self.tamanho):
                tab += f"{self.chaves[i]} {self.valores[i]}\n"
            return tab
        else:
            return None

    def cheia(self):
        if self.tamanho == self.fim:
            return True
        else:
            return False

    def vazia(self):
        if self.tamanho == 0:
            return True
        else:
            return False
