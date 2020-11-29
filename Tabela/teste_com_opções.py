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

    # Tabela Linear
    elif opc == 1:
        for i in range(num_itens):
            print("Digite a chave (Deve ser um número inteiro)")
            chave = int(input("> "))

            print("\n\nDigite o(s) valor(es) correspondente(s) a chave:")
            print("(caso seja mais de um valor, separar por espaço)")
            valor = input().split()

            pessoas.inserir_linear(chave, valor)
            limpa()
            print(valor)

        while True:
            print("Digite o número correspondente ao desejado:")
            print("[ 1 ] Inserir item")
            print("[ 2 ] Remover item")
            print("[ 3 ] Consultar valor")
            print("[ 4 ] Consultar número da linha")
            print("[ 5 ] Mostrar tabela")
            print("[ 6 ] Destruir tabela")
            print("[ 7 ] Sair")
            opc = int(input("> "))
            limpa()

            if opc == 7:
                break

            elif opc == 1:
                print("Digite a chave (Deve ser um número inteiro)")
                chave = int(input("> "))

                print("\n\nDigite o(s) valor(es) correspondente(s) a chave:")
                print("(caso seja mais de um valor, separar por espaço")
                valor = input().split()

                pessoas.inserir_linear(chave, valor)
                limpa()

            elif opc == 2:
                print("Digite a chave:")
                chave = int(input("> "))

                pessoas.remover(chave)

            elif opc == 3:
                print("Digite a chave:")
                chave = int(input("> "))

                value = pessoas.consulta_valor(chave)
                if value is None:
                    value = "INEXISTENTE"
                print(f"{chave} {value}\n\n")

            elif opc == 4:
                print("Digite a chave:")
                chave = int(input("> "))

                value = pessoas.consulta_index(chave)
                if value is None:
                    value = "INEXISTENTE"
                else:
                    value += 1
                print(f"{chave} está na linha {value}\n\n")

            elif opc == 5:
                show = f"{pessoas.mostrar_tabela()}\n\n"
                if show is None:
                    print(" ")
                else:
                    print(show)

            elif opc == 6:
                pessoas.destruir()

        break
