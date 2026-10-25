# Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um programa que receba o código e o valor de 15 transações. Calcule  e mostre:

# o valor total das compras à vista;
# o valor total das compras a prazo;
# o valor total das compras efetuadas;
# o valor da primeira prestação das compras a prazo, sabendo-se que essas serão pagas em três vezes.

import random

vista = 0
prazo = 0

for i in range(15):
    
    valor = random.randint(1, 100)
    tipo = random.choice(['V', 'P'])

    if tipo == 'V':
        vista += valor
    else:
        prazo += valor

print(f'Valor à vista: {vista};\nValor a prazo: {prazo};\nValor total:   {vista + prazo};\n1ºPrestação: {prazo / 3:.2f}.')
