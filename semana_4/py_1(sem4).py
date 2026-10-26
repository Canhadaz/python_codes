# Faça um programa que carrregue um vetor de seis elementos numéricos inteiros, calcule e mostre:

# a quantidade de números pares;
# quais os números pares;
# a quantidade de números ímpares;
# quais os números ímpares
# Observações:
# Pode usar o comando append() para adicionar os valores no vetor. 
# Os elementos do vetor devem ser acessados através do seus respectivos índices.

vetor = []

par_quantidade = 0
pares = []

impar_quantidade = 0
impares = []

for i in range(6):
    num = int(input('Digite o número: '))
    vetor.append(num)
    if vetor[i] % 2 == 0:
        par_quantidade += 1
        pares.append(vetor[i])
    if vetor[i] % 2 != 0:
        impar_quantidade += 1
        impares.append(vetor[i])

print(vetor)
print(f'\nQuantidade de número pares -> {par_quantidade}\nPares -> {pares}')
print(f'\nQuantidade de número impares -> {impar_quantidade}\nImpares -> {impares}')

