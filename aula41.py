
from time import sleep

while True:
    numero_1 = input('Digite o primeiro numero: ')
    numero_2 = input('Digite o primeiro numero: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    try:
        numero_1_foat = float(numero_1)
        numero_2_foat = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None
    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são invaidos')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    print('Realizando sua conta')
    if operador == '-':
        sleep(1)
        resultado = numero_1_foat - numero_2_foat
        print(f'{numero_1_foat} - {numero_2_foat} = {resultado}')

    elif operador == '+':
        sleep(1)
        resultado = numero_1_foat + numero_2_foat
        print(f'{numero_1_foat} + {numero_2_foat} = {resultado}')

    elif operador == '*':
        sleep(1)
        resultado = numero_1_foat * numero_2_foat
        print(f'{numero_1_foat} * {numero_2_foat} = {resultado}')

    elif operador == '/':
        sleep(1)
        resultado = numero_1_foat / numero_2_foat
        print(f'{numero_1_foat} / {numero_2_foat} = {resultado}')

    resposta = input('Deseja continuar? [S/N]').lower()
    if resposta == 'n':
        break
