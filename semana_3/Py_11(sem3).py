valor = float(input('Digite o valor do carro: '))
parcelar = input('Deseja parcelar ? [S/N] ').upper()

if parcelar == 'N':
    print(f'\nValor do carro à vista = {valor - (valor / 5):.2f}')
    exit()

vezes = int(input('Em quantas vezes deseja parcelar ?\n--> 6; 12; 18; 24 .. 60.\n--> '))

if vezes == 0:
    print('\nERRO: Digite um valor de parcelas dentre 6 e 60, que seja divisivel por [6]')
    exit()

i = 1
n = 1

while i < 10:
    if vezes % 6 == 0:
        n += 1
    else:
        print('\nERRO: Digite um valor de parcelas dentre 6 e 60, que seja divisivel por [6]')
        exit()

    i += 1

print(f'\nValor final do carro, com {vezes} parcelas = {valor + (valor * ((n * 3) / 100)):.2f}')