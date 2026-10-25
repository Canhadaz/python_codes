# Um banco concederá um crédito especial aos seus clientes de acordo com o saldo médio no último ano. Faça um programa que receba o saldo médio de um cliente e calcule o valor do crédito, de acordo com a tabela a seguir. Mostre o saldo médio e o valor do crédito.

# Saldo Médio                                                                                        Percentual
# ---------------------------------------------------------------------------------------------------
# Acima de R$ 400,00                                                                       30% do saldo médio
# R$ 400,00 (incluso)  até R$ 300,00 (não incluso)                           25% do saldo médio
# R$ 300,00 (incluso) até R$ 200,00 (não incluso)                            20% do saldo médio
#  Até R$ 200,00 (incluso)                                                                10% do saldo médio

saldo = int(input('\nDigite o saldo medio de sua conta: '))

if saldo <= 200:
    print('\nO creíto especial fornecido será de 10% do saldo médio. Totalizando: ' + str(saldo + (saldo * 10 / 100)))
elif saldo > 200 and saldo <= 300:
    print('\nO creíto especial fornecido será de 20% do saldo médio. Totalizando: ' + str(saldo + (saldo * 20 / 100)))
elif saldo > 300 and saldo <= 400:
    print('\nO creíto especial fornecido será de 25% do saldo médio. Totalizando: ' + str(saldo + (saldo * 25 / 100)))
elif saldo > 400:
    print('\nO creíto especial fornecido será de 30% do saldo médio. Totalizando: ' + str(saldo + (saldo * 30 / 100)))
else:
    print('\nSaldo inválido.')