import random

soma = 0
matriz = []
quantidade = 0
quantidade_pares = 0

for i in range(2):
    linha = []
    for j in range(4):
        num = random.randint(1,20)
        linha.append(num)
    
    matriz.append(linha)    
    print(matriz[i])

for i in range(len(matriz)):
    quantidade = 0
    for j in range(len(matriz[i])):
        if 15 <= matriz[i][j] <= 20:
            quantidade += 1
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
            quantidade_pares += 1
    print(f'\nquantidade de números dentre 15 e 20 = {quantidade}')

soma = soma / (quantidade_pares)

print(f'media dos números pares = {soma:.2f}')


