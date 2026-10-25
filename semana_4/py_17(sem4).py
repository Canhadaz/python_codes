import random

matriz = [[random.randint(10, 99) for n in range(7)] for i in range(5)]

primo = 0
maior_primo = 0

for n in range(5):
    for i in range(7):
        if matriz[n][i] % 2 != 0:
            for j in range(3,matriz[n][i]):
                if matriz[n][i] % j == 0:
                    primo = 0
                    break
                else:
                    primo = matriz[n][i]
        if maior_primo < primo:
            maior_primo = primo

    print(matriz[n])
print(maior_primo)


if maior_primo != 0:
    for n in range(5):
        for i in range(7):
            matriz[n][i] = matriz[n][i] * maior_primo
        print(matriz[n])
else:
    print('NÃO TEM PRIMO N PAE')
