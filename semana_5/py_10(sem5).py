import random

def cruz(matriz) -> list:

    posicao= []

    for i in range(1, len(matriz) - 1):
        for n in range(1, len(matriz[i]) - 1):
            if matriz[i][n] == 1:
                if ((matriz[i + 1][n] == 1) and (matriz[i - 1][n] == 1) 
                    and (matriz[i][n - 1] == 1) and (matriz[i][n + 1] == 1)):
                    posicao.append([i,n])
    
    return posicao

def main():

    matriz = [[random.randint(0,1) for i in range(10)] for n in range(10)]

    for i in range(len(matriz)):
        print(f'{i} {matriz[i]}')

    print('')
    print(cruz(matriz))

main()