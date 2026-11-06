def trocar_elementos_matriz(A: list) -> list:
    m = len(A)
    n = len(A[0])

    if m >= 8:
        A[1], A[7] = A[7], A[1]
    if n >= 10:
        for i in range(m):
            A[i][3], A[i][9] = A[i][9], A[i][3]
    if m == n:
        for i in range(m):
            A[i][i], A[i][n - 1 - i] = A[i][n - 1 - i], A[i][i]
    if m == n and m >= 10:
        coluna = [A[i][9] for i in range(m)]
        for i in range(m):
            A[i][9] = A[4][i]
            A[4][i] = coluna[i]

    return A

def main():
    matriz = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
]
    matriz = trocar_elementos_matriz(matriz)

    for linha in matriz:
        print(linha)

main()
