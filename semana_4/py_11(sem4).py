import random

matriz = []
quantidade = 0

for i in range(3):
    linha = []
    for j in range(5):
        num = random.randint(1,20)
        linha.append(num)
    
    matriz.append(linha)    
    print(matriz[i])

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if 15 <= matriz[i][j] <= 20:
            quantidade += 1

print(f'\nquantidade de números dentre 15 e 20 = {quantidade}')