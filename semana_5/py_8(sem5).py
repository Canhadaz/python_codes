import random

def diagonal_secundaria(matriz) -> list:

    vetor = []
    for i in range(len(matriz)):
        print(matriz[i])
    
    print('')

    for i in range(len(matriz)):
        coluna_fim = len(matriz[i]) - 1
        for n in range(len(matriz[i])):
            if matriz[i][coluna_fim - i] == matriz[i][n]:
                vetor.append(matriz[i][n])
    if len(matriz) == len(matriz[i]):
        return vetor



def main():

    matriz = [[random.randint(10,99) for i in range(5)] for n in range(5)]
    print(diagonal_secundaria(matriz))

main()