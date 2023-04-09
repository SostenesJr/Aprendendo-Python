"""
Iterando strings com while
"""

# nome = 'Luiz Otavio'  # Iteraveis


# indice = 0
# while indice <= len(nome):
#     print(f'{nome[indice]}', end='*')
#     indice += 1
# print('FIM')

nome = 'Maria Helena'
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)
