import random

matriz = [[0 for n in range(5)] for i in range(5)]

soma_linha4 = 0
soma_col2 = 0
dia_main = 0
dia_sec = 0
total = 0

for n in range(5):
    for i in range(5):
        num = random.randint(10,99)
        matriz[n][i] = num
        soma_col2 += matriz[n][i] if matriz[n][i] == matriz[n][1] else 0
        soma_linha4 += matriz[n][i] if matriz[n][i] == matriz[3][i] else 0
        dia_main += matriz[n][i] if n == i else 0
        dia_sec += matriz[n][4 - i] if 4 - n == i else 0
        total += matriz[n][i]
    print(matriz[n])
print(f'soma da 4º linha = {soma_linha4}')
print(f'soma da 2º coluna = {soma_col2}')
print(f'soma da diagonal principal = {dia_main}')
print(f'soma da diagonal secundária = {dia_sec}')
print(f'soma de todos os elementos = {total}')
