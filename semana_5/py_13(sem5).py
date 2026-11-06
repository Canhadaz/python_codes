def matriz_vetor(matriz: list, num: int) -> list:
    v = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            v.append(matriz[i][j] * num)
    return v

def main():
    M = [ [1, 2, 3, 4, 5, 6],
         [7, 8, 9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18],
         [19, 20, 21, 22, 23, 24],
         [25, 26, 27, 28, 29, 30],
         [31, 32, 33, 34, 35, 36]]

    num = int(input('Digite um número: '))

    print(matriz_vetor(M, num))

main()