def menor_valor_abaixo_diagonal_secundaria(A: list) -> int:
    n = len(A)
    menor = None

    for i in range(n):
        for j in range(n):
            if i + j > n - 1:
                if menor is None or A[i][j] < menor:
                    menor = A[i][j]

    return menor

def main():
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print(menor_valor_abaixo_diagonal_secundaria(matriz))
main()