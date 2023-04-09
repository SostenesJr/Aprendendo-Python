"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_1 = int(numero)
    if numero_1 % 2 == 0:
        print(f'O {numero_1} que você digitou é par')
    else:
        print(f'O {numero_1} que você digitou é impar')
else:
    print('Você nao digitou um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação coletiva. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('digite a hora: ')
try:
    hora_1 = int(hora)
    if hora_1 >= 0 and hora_1 <= 11:
        print('Bom dia!')
    elif hora_1 >= 12 and hora_1 <= 17:
        print('Boa tarde')
    elif hora_1 >= 18 and hora_1 <= 23:
        print('Boa noite')
    else:
        print('Nao conheço essa hora')
except:
    print('Por favor digite um numero inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print(f'Seu nome {nome} é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print(f'Seu nome {nome} é normal.')
    else:
        print(f'Seu nome {nome} é grande.')
else:
    print('Digite pelo menos uma letra')
