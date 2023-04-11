
while True:

    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    simbolo = input('Digite um dos simblos: [+-/*] ')
    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None
        if numero_validos == None:
            print('Você digitou um ou mais campos invalidos!')
            continue

    operador_permitido = '-+/*'
    if simbolo not in operador_permitido:
        print('Operador invalido')
        continue
    if len(simbolo) > 1:
        print('Digite apena um simbolo')
        continue
    if simbolo == '+':
        resposta = num_1 + num_2
        print(f'{numero_1} + {numero_2} : {resposta}')
    elif simbolo == '-':
        resposta = num_1 - num_2
        print(f'{numero_1} - {numero_2} : {resposta}')
    elif simbolo == '*':
        resposta = num_1 * num_2
        print(f'{numero_1} * {numero_2} : {resposta}')
    elif simbolo == '/':
        resposta = num_1 / num_2
        print(f'{numero_1} / {numero_2} : {resposta}')

    resp = input('Deseja continuar: [S/N]'.upper())
    if resp == 'N':
        break
