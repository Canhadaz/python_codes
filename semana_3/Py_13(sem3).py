import random

secreto = random.randint(1, 50)
n = 0

for i in range(7):
    tentativa = int(input(f'Tente adivinhar o número de 1 à 50: [você possui {7 - (i)} tentativas]\n--> '))
    n += 1

    if tentativa == secreto:
        print('\nPARABÉNS, VOCÊ ACERTOU!!')
        exit()
    else:
        if tentativa > secreto:
            print('\nDICA: o número secreto é menor')
        else:
            print('\nDICA: o número secreto é maior')

if n == 7:
    print(f'\nVOCÊ É UM FRACASSO COMO SER HUMANO!!\nO número secreto era: {secreto}')
    exit()
