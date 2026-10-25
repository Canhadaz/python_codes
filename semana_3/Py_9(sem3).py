import random

velho = 0
media = 0
n = 0
leve = 0

for i in range(1, 26):

    idade = random.randint(1, 100)
    altura = random.uniform(1.0, 2.1)
    peso = random.randint(1, 200)

    if idade >= 50:
        velho += 1

    if idade >= 10 and idade <= 20:
        media += altura
        n += 1

    if peso < 40:
        leve += 1

print(f'{velho} velhos.\n{media / n:.2f} metros.\n{leve} desnutridos.')
