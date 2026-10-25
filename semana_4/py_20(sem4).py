import random

matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        valor = round(random.uniform(1, 10), 2)
        linha.append(valor)
    matriz.append(linha)

print("Matriz original:")
for i in range(5):
    for j in range(5):
        print(f"{matriz[i][j]:8.2f}", end=" ")
    print()

diagonal = []
for i in range(5):
    diagonal.append(matriz[i][i])

print("\nElementos da diagonal principal:")
for i in range(5):
    print(f"matriz[{i}][{i}] = {diagonal[i]:.2f}")

matriz_nova = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(matriz[i][j] * diagonal[i])
    matriz_nova.append(linha)

print("\nMatriz após a multiplicação:")
for i in range(5):
    for j in range(5):
        print(f"{matriz_nova[i][j]:8.2f}", end=" ")
    print()