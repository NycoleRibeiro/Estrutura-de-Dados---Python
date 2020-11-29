from Tabela import tabela

while True:    
    tam = int(input("Quantas linhas terá? "))
    pessoas = tabela(tam)

    print("""Digite o número correspondente ao desejado:
    [ 1 ] Inserir itens de forma linear
    [ 2 ] Inserir itens de forma ordenada
    [ 3 ] Sair""")
    opc = int(input("> "))
    num_itens = int(input("Quantos itens deseja adicionar? "))

    if opc == 3:
        break
    elif opc == 2:
        for i in range(num_itens):
            print("Digite a chave (Deve ser um número inteiro")
            while True:
                try:
                    chave = int(input("> "))
                    break

            print("Digite o(s) valor(es) correspondente(s) a chave:")
            print("(caso seja mais de um valor, separar por espaço")
            valor = input().split()

            pessoas.inserir_linear(chave, valor)
