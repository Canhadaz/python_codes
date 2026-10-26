# Escreva um programa que analise os seguintes critérios para determinar se um estudante é elegível para uma bolsa de estudos:
# O estudante deve ter uma média final igual ou superior a 8,5.
# A renda familiar do estudante não pode ultrapassar R$ 2.500,00 mensais.
# Caso a média final do estudante seja inferior a 8,5, ele pode ainda se elegível se tiver média entre 8,0 e 8,4 e tiver pelo menos 30 horas de serviço comunitário comprovadas.
# O programa deve solicitar ao usuário:
# A média final do estudante (um número real).
# A renda familiar mensal (um número real).
# As horas de serviço comunitário (um número inteiro).
# No final, o programa deve informar se o estudante "é elegível" ou "não é elegível" para a bolsa de estudos.

media_f = float(input("\nMédia final do estudante: "))
renda = float(input("Qual a renda familiar ? "))
horas = int(input('Quantas horas de serviço comunitário? '))

if media_f >= 8.5 and renda <= 2500:
    print('\nAPROVADO para a bolsa de estudos!')
elif media_f >= 8.0 and renda <= 2500 and horas >= 30:
        print('\nAPROVADO para a bolsa de estudos! ')
else: 
    print('\nREPROVADO!')