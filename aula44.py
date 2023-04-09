
# senha_salva = '123456'
# senha_digitada = ''
# repetições = 0

# while senha_salva != senha_digitada:
# senha_digitada = input(f'Sua senha ({repeticoes}x): ')

# repetições += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra} '
    print(letra)
print(novo_texto + '*')
