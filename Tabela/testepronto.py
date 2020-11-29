# 1- todas as operações básicas do TAD Tabela por contiguidade física;
# 2- uma nova operação de inserção ordenada e o algoritmo de busca binária;
# 3- um programa que importe a classe e teste todos os métodos.
from Tabela import tabela

tam = int(input("Tamanho: "))
pessoas = tabela(tam)
pessoas.inserir_ordenada(84265704080, ("Nycole", "19/07/1999", "Feminino"))
pessoas.inserir_ordenada(74582747871, ("Bruno", "05/02/1998", "Masculino"))
pessoas.inserir_ordenada(96191493091, ("Steven", "17/12/1997", "Masculino"))
pessoas.inserir_ordenada(64265704080, ("Kath", "10/08/1999", "Feminino"))
pessoas.inserir_ordenada(24582747871, ("Shawn", "15/05/1998", "Masculino"))
pessoas.inserir_ordenada(46191493091, ("Alex", "07/11/1997", "Não-Binario"))

print("\n\n")
print("CPF (Nome, DataNasc, Genêro)")
pessoas.mostrar_tabela()
print("\n\n")

pessoas.remover(74582747871)
print("CPF (Nome, DataNasc, Genêro)")
pessoas.mostrar_tabela()
print("\n\n")

pessoas.destruir()
print("CPF (Nome, DataNasc, Genêro)")
pessoas.mostrar_tabela()
print("\n\n")
