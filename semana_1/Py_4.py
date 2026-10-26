# Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, 
# sabendo-se que este sofreu um desconto de 10%.

# Sugestões:

# Variável de entrada de dados: preco
# Variável calculada : novo_preco

# novo_preco = preco - preco * 10 / 100

valor = int(input('Qual o preço do produto ? '))

print('\nNovo valor = ' + str(valor - (valor/10)))