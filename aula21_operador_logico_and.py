# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' Falso
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]ar: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' e senha_digitada == senha_permitida:
# print('Entrar')
# outro:
# print('Sair')

# Avaliação de curto circuito
print(True and True and True)
print(True and 0 and True)
