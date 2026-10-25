# Faça um programa que leia um valor inteiro e positivo  (n).

# Em seguida, calcule e mostre a seguinte soma:
# Observação:
# Em vez de somar frações simples (1/n) ,  agora usamos fatoriais no denominador.

# Essa soma é interessante porque se aproxima do número   

# (a base dos logaritmos naturais), muito usado em matemática e ciências.

n = 7
soma = 0
s = 1

for m in range(0, n, +1):
    for i in range(n - m, 0, -1):
        s *= i
        soma += s
    print(f'1 / {n - m}! = {1 / s:.4f} --> [{n - m}! = {s}]')
    s = 1

print(f'\nSomatório = {soma:.2f}')


