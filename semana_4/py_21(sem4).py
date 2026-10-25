import random

n = int(input("Digite o valor de N (tamanho da matriz): "))
while n < 1:
    n = int(input("N deve ser maior que zero. Digite novamente: "))

matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(random.randint(1, 100))
    matriz.append(linha)

print(f"\nMatriz {n}x{n}:")
for i in range(n):
    for j in range(n):
        print(f"{matriz[i][j]:5d}", end=" ")
    print()

diagonal_dominante = True
soma_acima = 0
soma_abaixo = 0
menor = maior = matriz[0][0]
pos_menor = pos_maior = (0, 0)

for i in range(n):
    soma_outros = 0  

    for j in range(n):
        valor = matriz[i][j]

        if j > i:
            soma_acima += valor
            soma_outros += abs(valor)
        elif j < i:
            soma_abaixo += valor
            soma_outros += abs(valor)

        if valor < menor:
            menor = valor
            pos_menor = (i, j)
        if valor > maior:
            maior = valor
            pos_maior = (i, j)

    if matriz[i][i] < soma_outros:
        diagonal_dominante = False

print()
if diagonal_dominante:
    print("A matriz É diagonal dominante.")
else:
    print("A matriz NÃO é diagonal dominante.")

print(f"\nSoma dos elementos acima da diagonal principal: {soma_acima}")
print(f"Soma dos elementos abaixo da diagonal principal: {soma_abaixo}")

print(f"\nMenor elemento: {menor} na posição [{pos_menor[0]}][{pos_menor[1]}]")
print(f"Maior elemento: {maior} na posição [{pos_maior[0]}][{pos_maior[1]}]")