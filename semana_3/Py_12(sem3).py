import random

numero = random.randint(1, 10)
v_inicial = random.randint(1,10)

print(f'degraus = {numero}')
print(f'valor_inicial = {v_inicial}\n')

for i in range(1, numero + 1):
    for j in range(i):
        print(v_inicial, end=';')
        v_inicial += 1

    print('')

