# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
# shallow copy - faz uma copia do dicionario, porem nao faz copia de lista, ou dicionarios que estao dentro de um dicionario no caso os sub-niveis, ele deixa essa sub-lista ou dicionarios linkada ao original assim, se você mudar na copia tambem vai mudar no orginal

# deepcopy - como o nome ja diz, ele faz uma copia produnda assim pega todos os sub-niveis e nao deixa linkado com o original

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)
