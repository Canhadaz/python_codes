# Faça um programa que receba quatro notas de um aluno, 
# calcule e mostre a média aritmética das notas e a mensagem de APROVADO ou REPROVADO, 
# considerando para aprovação média 6.0.

n1 = int(input('Nota 1:'))
n2 = int(input('Nota 2:'))
n3 = int(input('Nota 3:'))
n4 = int(input('Nota 4:'))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print('\nAPROVADO.')
else:
    print('\nREPROVADO')
