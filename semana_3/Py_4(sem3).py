# Faça um programa que leia cinco grupos de quatro valores (A, B, C, D) e mostre-os na ordem lida. Em seguida, mostre-os em ordem crescente e decrescente.

# Não pode usar funções de ordenação já existentes na linguagem de programação.

import random

for grupo in range(5):
    valores = []

    for i in range(4):
        num = random.randint(1, 10)
        valores.append(num)

    print(f'{grupo + 1}º grupo --> ordem lida:        {valores}')

    # crescente
    for i in range(len(valores)):
        for j in range(i + 1, len(valores)): # maneira de fazer valores[i] > valores[i + 1], sem dar erro de indexação.
            if valores[i] > valores[j]:
                valores[i], valores[j] = valores[j], valores[i]

    print(f'{grupo + 1}º grupo --> ordem crescente:   {valores}')

    # decrescente
    for i in range(len(valores)):
        for j in range(i + 1, len(valores)): # maneira de fazer valores[i] > valores[i + 1], sem dar erro de indexação.
            if valores[i] < valores[j]:
                valores[i], valores[j] = valores[j], valores[i]

    print(f'{grupo + 1}º grupo --> ordem decrescente: {valores}\n')