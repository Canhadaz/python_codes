# Faça um programa para calcular e mostrar o salário reajustado de um funcionário. Sabe-se que o percentual de aumento é o mesmo da tabela a seguir:

 
# Salário                                                  Percentual de Aumento
# ------------------------------------------------------------------------------
# Até R$ 300,00                                                   35%
# Acima de R$ 300,00                                         15%

salario = int(input('Digite o salário: '))

print('\nO salário reajustado com o percentual de aumento de 35% é:' + str((salario + (salario * 30/100)))) if salario <= 300 else print('\nO salário reajustado com percentual de aumento de 15% é:' + str((salario + (salario * 15/100))))