# Faça um programa que verifique e mostre os números entre 1.000 e 2.000 (inclusive) que, quando divididos por 11, produzam resto igual a 5.

i = 1000
n = 1
while i < 2000:
    i += 1
    if i % 11 == 5:
        print(f'{n}º Número -> {i}')
        n += 1
