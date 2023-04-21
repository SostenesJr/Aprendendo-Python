#  Exercicio - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador_acerto = 0
print(f'Pergunta: {perguntas[0]["Pergunta"]}')
contador = 0
for numero in perguntas[0]['Opções']:
    print(f'{contador}) {numero}', sep='')
    contador += 1
opcao = input('Escolha uma opção: ')
if opcao == '2':
    print('Você acerto 2 + 2 = 4')
    contador_acerto += 1
else:
    print(f'Você errou {opcao} não é a resposta correta')
print()

print(f'Pergunta: {perguntas[1]["Pergunta"]}')
contador = 0
for numero in perguntas[1]['Opções']:
    print(f'{contador}) {numero}', sep='')
    contador += 1
opcao = input('Escolha uma opção: ')
if opcao == '0':
    print('Você acerto 5 * 5 = 25')
    contador_acerto += 1
else:
    print(f'Você errou {opcao} não é a resposta correta')
print()

print(f'Pergunta: {perguntas[2]["Pergunta"]}')
contador = 0
for numero in perguntas[2]['Opções']:
    print(f'{contador}) {numero}', sep='')
    contador += 1
opcao = input('Escolha uma opção: ')
if opcao == '1':
    print('Você acerto 10 / 2 = 5')
    contador_acerto += 1
else:
    print(f'Você errou {opcao} não é a resposta correta')
print()


print(f'Você acertou {contador_acerto} de 3 perguntas.')
