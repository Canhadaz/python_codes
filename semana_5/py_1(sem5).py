def soma(n):
    soma = 0
    for i in range(1, n):
        soma += i
        print(soma)
    return soma


def main():

    while True:
        try:
            n1 = int(input('DIGITE O VALOR: '))

            if n1 < 1:
                raise ValueError
            break
        except ValueError:
            print('\nDIGITE DE NOVO!')

    soma(n1)

main()