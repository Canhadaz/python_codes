# Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui. 

# Essa pessoa vai passar por vários países e precisa converter seu dinheiro em:
# dólares, marco alemão e libra esterlina.

# Sabe-se que a cotação do dólar é de R$ 5,70, do marco alemão é de R$ 3,16 e da libra esterlina é de R$ 7,35.

# O programa deve fazer as conversões e mostrá-las.

real = float(input("Insira o valor a ser convertido: "))

print("\nVocê tem " + str(real/5.7) + " em dólares.")

print("\nVocê tem " + str(real/3.16) + " em marcos alemães.")

print("\nVocê tem " + str(real/7.35) + " em libras esterlinas.")

