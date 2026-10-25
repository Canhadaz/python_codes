import random

matriz = [[random.randint(10,99) for n in range(4)] for i in range(3)]

quantidade_par = 0
quantidade_impar = 0
soma_par = 0
soma_impar = 0

for n in range(3):
    for i in range(4):
        if matriz[n][i] % 2 == 0:
            quantidade_par += 1
            soma_par += matriz[n][i]
        if matriz[n][i] % 2 != 0:
            quantidade_impar += 1
            soma_impar += matriz[n][i]

    print(matriz[n])
print('PAR:')

print(quantidade_par)
print(soma_par)
print(f'{soma_par/quantidade_par:.2f}')

print('\nÍMPAR:')

print(quantidade_impar)
print(soma_impar)
print(f'{soma_impar/quantidade_impar:.2f}')

print(f'\n{(soma_par + soma_impar) / 12:.2f}')
