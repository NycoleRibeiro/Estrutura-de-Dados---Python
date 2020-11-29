from Tabela import tabela
from os import system


def limpa():
    system('cls')


while True:
    tam = int(input("Quantas linhas terá? "))
    pessoas = tabela(tam)
    limpa()

    print("Digite o número correspondente ao desejado:")
    print("[ 1 ] Inserir itens de forma linear")
    print("[ 2 ] Inserir itens de forma ordenada")
    print("[ 3 ] Sair")
    opc = int(input("> "))
    num_itens = int(input("Quantos itens deseja adicionar? "))
    limpa()

    if opc == 3:
        break
    elif opc == 2:
        for i in range(num_itens):
            print("Digite a chave (Deve ser um número inteiro")
            while True:
                try:
                    chave = int(input("> "))
                    break

            print("\n\nDigite o(s) valor(es) correspondente(s) a chave:")
            print("(caso seja mais de um valor, separar por espaço")
            valor = input().split()

            pessoas.inserir_linear(chave, valor)
            limpa()

        while True:
            print("Digite o número correspondente ao desejado:")
            print("[ 1 ] Inserir item")
            print("[ 2 ] Remover item")
            print("[ 3 ] Consultar valor")
            print("[ 4 ] Consultar linha")
            print("[ 5 ] Mostrar tabela")
            print("[ 6 ] Destruir tabela")
            print("[ 7 ] Sair")
            opc = int(input("> "))