import random

vetor = []
compactado = []

for i in range(10):
    num = random.randint(-100,100)
    vetor.append(num)

    if not num <= 0:
        compactado.append(num)

print(vetor)
print(compactado)