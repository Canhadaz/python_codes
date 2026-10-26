vetor = []
negativo = 0
soma = 0

for i in range(10):
    num = int(input('Digite um número de -100 até 100\n--> '))
    vetor.append(num)

    if vetor[i] < 0:
        negativo += 1

    if vetor[i] > 0:
        soma += vetor[i]

print(vetor)
print(f'\nQuantidade de números negativos = {negativo}')
print(f'\nValor da soma de todos os números positivos = {soma}')
