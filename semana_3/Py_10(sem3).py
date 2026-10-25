import random

v_m = 0
n = 0
azul = 0
r_a = 0
m_a = 0

for i in range(20):

    idade = random.randint(1, 100)
    peso = random.randint(1, 200)
    altura = random.uniform(1.0, 2.1)
    olhos = random.choice(['A','P','V','C'])
    cabelos = random.choice(['P','C','L','R'])

    if idade >= 50 and peso < 60:
        v_m += 1

    if altura < 1.5:
        m_a += altura
        n += 1

    if olhos == 'A':
        azul += 1

    if cabelos == 'R' and olhos != 'A':
        r_a += 1

print(f'{v_m}\n{m_a / n:.2f}\n{(azul/20) * 100:.2f}\n{r_a}')