frase = 'O python é uma linguagem de programação '\
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'

i = 0
qtd_apr_mais_vezes = 0
letra_apr_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)
    if qtd_apr_mais_vezes < qtd_atual:
        qtd_apr_mais_vezes = qtd_atual
        letra_apr_mais_vezes = letra_atual
    i += 1
print(
    'A letra que apareceu mais vezes foi '
    f'{letra_apr_mais_vezes} que apareceu '
    f'{qtd_apr_mais_vezes}x'
)
