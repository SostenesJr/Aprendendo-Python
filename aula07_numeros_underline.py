# Variáveis são sadas para salvar algo na memória do computador.
# PEP8: inicie variaveis com letras minúsculas, pode usar
# números e underline _
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável)
# Uso: nome_variavel = expressão

nome_completo = "Sostenes Ramos Conceição Junior"

print(nome_completo)

int_um = int('1')
print(int_um, type(int_um))
nome = 'Luiz'
idade = 30
maior_de_idade = idade >= 18
print('nome: ', nome, 'Idade: ', idade)
if maior_de_idade == True:
    maior_de_idade = 'verdadeiro'
print('É maior?', maior_de_idade)
