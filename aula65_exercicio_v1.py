print('Validação do CPF'.upper())
cpf = input('digite seu cpf [000.000.000-00]: ')
transicao = str.maketrans("", "", ".-")
cpf_sem_pontuacao = cpf.translate(transicao)
nove_numero = cpf_sem_pontuacao[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_numero:
    resultado_digito_1 += (int(digito) * contador_regressivo_1)
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
if digito_1 <= 9:
    digito_1 = digito_1
else:
    digito_1 = 0
# print(digito_1)

dez_numero = cpf_sem_pontuacao[:10]
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_numero:
    resultado_digito_2 += (int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
if digito_2 < 9:
    digito_2 = digito_2
else:
    digito_2 = 0
# print(digito_2)

novo_cpf = f'{nove_numero}{digito_1}{digito_2}'
novo_cpf_1 = int(novo_cpf)
if novo_cpf == cpf_sem_pontuacao:
    print(f'{cpf} é valido.')

else:
    print('CPF inválido')
