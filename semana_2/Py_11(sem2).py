# Faça um programa que receba o  salário de um funcionário e, usando a tabela a seguir, calcule e mostre o valor do aumento e o novo salário.

# Salário                                                                                                Percentual de aumento
# -----------------------------------------------------------------------------------------------------------------------
# até R$ 300,00 (incluso)                                                                                15
# R$ 300,00 (não incluso) até R$ 600,00 (incluso)                                                        10
# R$ 600,00 (não incluso) até R$ 900,00 (incluso)                                                        5
# acima de R$ 900,00                                                                                     0

salario = int(input('Digite o salário do funcionário: '))

if salario <= 300:
    print('\nValor do aumento: 15% [' + str(salario * 15/100) + '].\nNovo salário: ' + str(salario + salario * 15/100))
elif salario > 300 and salario <= 600:
    print('\nValor do aumento: 10% [' + str(salario * 10/100) + '].\nNovo salário: ' + str(salario + salario * 10/100))
elif salario > 600 and salario <= 900:
    print('\nValor do aumento: 5% [' + str(salario * 5/100) + '].\nNovo salário: ' + str(salario + salario * 5/100))
else:
    print('\nNão haverá aumento.')
