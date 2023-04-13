"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []
while True:
    print()
    print('Selecione uma opção:'.upper())
    opcao = input(' [i]nserir, [a]pagar, [l]istar, [s]air: ')
    if opcao == 'i':
        os.system('cls')
        item = input('Digite o que seseja inserir: ')
        lista.append(item)
    elif opcao == 'a':
        os.system('cls')
        if len(lista) == 0:
            print('Não a informações no momento.'.upper())
            continue
        for indice, item in enumerate(lista):
            print(f'{indice} - {item}')
        numero = input('Digite numero que deseja apagar: ')
        try:
            numero_1 = int(numero)
            del lista[numero_1]
        except ValueError:
            # erro especifico
            print('Por favor digite um numero inteiro')
        except IndexError:
            # erro especifico
            print('Por favor digite um valor existente')
        except Exception:
            # erro de forma geral
            print('ERRO DESCONHECIDO')
    elif opcao == 'l':
        os.system('cls')
        for indice, item in enumerate(lista):
            print(f'{indice} - {item}')
        if len(lista) == 0:
            print('Por favor insira alguma informação'.upper())
    elif opcao == 's':
        break
    else:
        print(f'Por favor escolha uma opção valida.'.upper())
print('Fim do programa'.upper())
