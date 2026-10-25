# Uma loja tem 15 clientes cadastrados e deseja enviar uma correspondência a cada um deles anunciando um bônus especial. 

# Faça um programa que leia o nome do cliente e o valor de suas compras no ano passado. 

# Calcule e mostre o nome do cliente e seu respectivo bônus de 10% se o valor das compras for menor que R$ 1.000,00 e de 15%, caso contrário.

nomes = []
compras = []

for i in range(3):
    nome = input(f'\nInforme o nome do {i + 1}º cliente: ').upper()
    nomes.append(nome)
    compra = float(input(f'Informe o valor da compra do {i + 1}º cliente: '))
    compras.append(compra)

for i in range(len(compras)):
    if compras[i] > 1000:
        print(f'\nCliente: {nomes[i]} \nValor das compras: R${compras[i]:.2f} -> Desconto de 15%: R${compras[i] - compras[i] * 15/100:.2f}')
    else:
        print(f'\nCliente: {nomes[i]} \nValor das compras: R${compras[i]:.2f} -> Desconto de 10%: R${compras[i] - compras[i] * 10/100:.2f}')
