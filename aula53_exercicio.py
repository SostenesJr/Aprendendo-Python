"""
exercicio
exiba os indices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
# i = 0
# for nome in lista:
#     print(i, nome)
#     i += 1

indices = range(len(lista))
# len enumera quanto itens tem na lista [3]
#  o range define os parametros, que sao de [0, 3]
print(indices)

for indice in indices:
    #  indice é um contador no caso 0 1 2
    #  lista[indice] é cada nome
    #  type(lista[indice]) sao os tipode valores dentro da lista
    print(indece, lista[indice], type(lista[indice]))
