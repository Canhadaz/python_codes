import random

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
d = random.randint(1, 100)

for i in range(4):
    for j in range(4):
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if c > d:
            c, d = d, c
    
media = (a + b + c + d) / 4
mediana = (b + c) / 2
    
print(f'\nO maior número é: {d}')
print(f'O menor número é: {a}')
print(f'A mediana é: {mediana:.2f}')
print(f'A média aritmetica é: {media:.2f}')


