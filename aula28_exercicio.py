nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertidfo é: {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome contem: {len(nome.strip())} letras.')
    print(f'A primeira letra d sue nome: {nome[0]}')
    print(f'A ultima letra do seu nome: {nome[-1]}')
else:
    print(f'Desculpe, você deixou campos vazios')
