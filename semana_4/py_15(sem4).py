import random

matriz = [[0 for n in range(5)]for i in range(12)]

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for n in range(12):
    semanas = []
    for i in range(4):
        num = random.randint(10,99)
        matriz[n][i] = num

total = 0
for n in range(12):
    soma = 0
    for i in range(4):
        soma += matriz[n][i]
        matriz[n][4] = soma
    print(f'{meses[n]:<10} --> {matriz[n][:-1]}', end = '')
    print(f' = R$ {matriz[n][4]:<3}')
    total += soma
print(f'TOTAL VENDIDO (ANO) -->           R$ {total}')
