# Faça um programa que carrregue um vetor de 7 elementos numéricos inteiros, calcule e mostre:

# os números múltiplos de 2;
# os números múltiplos de 3;
# os números múltiplos de 2 e de 3.
# Observações:
# Pode usar o comando append() para adicionar os valores no vetor. 
# Os elementos do vetor devem ser acessados através do seus respectivos índices.

import random

vetor = []

mul_2 = 0
multiplos_2 = []

mul_3 = 0
multiplos_3 = []

mul_2e3 = 0
multiplos_2e3 = []

for i in range(7):
    num = random.randint(1,100)
    vetor.append(num)

    if vetor[i] % 2 == 0:
        mul_2 += 1
        multiplos_2.append(vetor[i])
    if vetor[i] % 3 == 0:
        mul_3 += 1
        multiplos_3.append(vetor[i])
    if vetor[i] % 2 == 0 and vetor[i] % 3 == 0:
        mul_2e3 += 1
        multiplos_2e3.append(vetor[i])

print(vetor)
print(f'\nQuantidade de multiplos de 2 = {mul_2}\nMultiplos de 2 = {multiplos_2}')
print(f'\nQuantidade de multiplos de 3 = {mul_3}\nMultiplos de =3 = {multiplos_3}')
print(f'\nQuantidade de multiplos de 2 e de 3 = {mul_2e3}\nMultiplos de 2 e de 3 = {multiplos_2e3}')
