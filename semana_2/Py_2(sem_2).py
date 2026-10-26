# Faça um programa que receba duas notas, calcule e mostre a média aritmética e a mensagem que esta na tabela abaixo:

 

#         Média Aritmética                                               Mensagem
# --------------------------------------------------------------------------------------

# 0.0 (incluso)  <-> 4.0 (não incluso)                           Reprovado

# 4.0(incluso)  <-> 7.0 (não incluso)                            Exame

# 7.0(incluso) <-> 10.0 (incluso)                                   Aprovado

n1 = int(input('Nota 1:'))
n2 = int(input('Nota 2:'))

if ((n1 + n2) / 2) <= 4:
    print('\nReprovado')
elif ((n1 + n2) / 2) <= 7 and ((n1 + n2) / 2) > 4:
    print('\nExame')
else:
    print('\nAprovado')