# Faça um programa que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma (série harmônica simples):

# s = 1 + 1/2 + 1/3 + 1/4 + . . . + 1/n

n = 10
m = 1

for i in range(10):
    s = 1 / m
    m += 1
    print(f'{s:.3f}')