import random

vetor = []
vetor2 = []
soma = 0

vetor_r1 = []
vetor_r2 = []

for i in range(5):
    num = random.randint(1,100)
    vetor2.append(num)
    soma += num

    for j in range(2):
        num = random.randint(1,100)
        vetor.append(num)

for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
        vetor_r1.append(vetor[i])
    else:
        vetor_r2.append(vetor[i])

for i in range(len(vetor_r1)):
    vetor_r1[i] += soma

print(vetor_r2)

for i in range(len(vetor_r2)):
    contador = 0
    for j in range(1, vetor_r2[i] + 1):
        if vetor_r2[i] % j == 0:
            contador += 1

print(vetor)
print(vetor2)
print(vetor_r1)
print(vetor_r2)