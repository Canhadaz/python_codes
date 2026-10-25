import random

n = int(input('Digite a número fatorial:\n--> '))
fatorial = n

for i in range(1, n, +1):
    fatorial *= (n - i)

print(fatorial)
