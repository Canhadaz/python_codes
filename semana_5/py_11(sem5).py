import random

def compactador(matriz) -> list:
    compactado = []
    contador = 0
    vistas = []

    for n in range(len(matriz)):
        for i in range(len(matriz[n])):
            if matriz[n][i] not in vistas:
                contador = 1
                vistas.append(matriz[n][i])
                for j in range(n, len(matriz)):
                    for k in range(len(matriz[j])):
                        if (j == n and k <= i):
                            continue
                        if matriz[j][k] == matriz[n][i]:
                            contador += 1
                compactado.append((matriz[n][i], contador))
    return compactado

def main():
    matriz = [[chr(random.randint(97,122)) for n in range(5)] for i in range(5)]    

    for i in range(len(matriz)):
        print(f'{matriz[i]}')

    print(f'Compactado: {compactador(matriz)}')

main()