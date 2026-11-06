import random

def multiplicar_matrizes(matriz_a: list, matriz_b: list) -> list:
    matriz_c = [[0 for n in range(len(matriz_b[0]))] for i in range(len(matriz_a))]
    
    if len(matriz_a) != len(matriz_b[0]):
        print('Não é possível multiplicar as matrizes.')
        return 'Não vai ter como pae!'

    for i in range(len(matriz_a)):
        for j in range(len(matriz_b[0])):
            for k in range(len(matriz_b)):
                matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return matriz_c
        
def main():
    matriz_a = [[random.randint(1,9) for n in range(3)] for i in range(3)]
    matriz_b = [[random.randint(1,9) for n in range(3)] for i in range(3)]

    print('Matriz A:')

    for i in range(len(matriz_a)):
        print(f'{matriz_a[i]}')

    print('\nMatriz B:')

    for i in range(len(matriz_b)):
        print(f'{matriz_b[i]}')

    resultado = multiplicar_matrizes(matriz_a, matriz_b)

    print('\nMatriz C (Resultado):')
    for i in range(len(resultado)):
        print(f'{resultado[i]}')

main()