from time import sleep
print('Calculadora')


numero_int = 1

while numero_int <= 10:
    contador = 1
    while contador <= 10:
        sleep(0.3)
        resultado = numero_int * contador
        print(f'{numero_int} x {contador} = {resultado}')
        contador += 1
    print('-'*10)
    numero_int += 1
