
def media_abaixo_diagonais(A: list) -> float:
    n = len(A)
    soma = 0
    quantidade = 0

    for i in range(n):
        for j in range(n):
            if i > j and i + j > n - 1:
                soma += A[i][j]
                quantidade += 1

    if quantidade == 0:
        return 0.0

    return soma / quantidade

def main():
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(media_abaixo_diagonais(matriz))
    
main()