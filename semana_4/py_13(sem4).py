import random

matriz = []
posicao = [(0,0),(0,0)]

maior = 0
menor = 101

for n in range(6):
    linha = []
    for i in range(3):
        num = random.randint(1,100)
        linha.append(num)

    matriz.append(linha)
    print(matriz[n])

for n in range(6):
    for i in range(3):
        if maior < matriz[n][i]:
            maior = matriz[n][i]
            posicao[0] = ((n , i))

print(f'MAIOR NÚMERO --> {maior} | POSIÇÃO --> {posicao[0]}')

for n in range(6):
    for i in range(3):
        if menor > matriz[n][i]:
            menor = matriz[n][i]
            posicao[1] = ((n , i))

print(f'MENOR NÚMERO --> {menor} | POSIÇÃO --> {posicao[1]}')