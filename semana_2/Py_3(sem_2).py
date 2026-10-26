# Faça um programa que receba dois números e mostre o menor.

n1 = int(input('Número 1:'))
n2 = int(input('Número 2:'))

if n1 == n2:
    print('\nOs números devem ser diferentes.')
elif n1 > n2:
    print('\nO menor número é: ' + str(n2))
else: 
    print('\nO menor número é: ' + str(n1))