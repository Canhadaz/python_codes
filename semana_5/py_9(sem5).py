import random

def max_min(matriz) -> list:

    maior = 0
    menor = 100

    for i in range(len(matriz)):
        for n in range(len(matriz[i])):
            if maior < matriz[i][n]:
                maior = matriz[i][n]
            if menor > matriz[i][n]:
                menor = matriz[i][n]
    
    return maior, menor



def main():

    matriz = [[random.randint(10,99) for i in range(5)] for n in range(5)]
    print(max_min(matriz))

main()