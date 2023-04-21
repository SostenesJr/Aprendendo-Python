# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total


result = multiply(2, 3, 4, 5, 6, 7)
print(result)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# verificaçao de varios valores


def verification(*args):
    for number in args:
        if number % 2 == 0:
            print(f'{number} é par')
        else:
            print(f'{number} é impar')
    return f''

# verificação de um valor
# def verification(number):
#     item = number % 2 == 0
#     if item == True:
#         return 'Par'
#     else:
#         return 'Impar'

# verificaçao de um valor de forma simplicada


# def verification(number):
#     item = number % 2 == 0
#     if item:
#         return f'{number} is even'
#     return f'{number} is odd'


result = verification(3)
print(result)
