# Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário. 
# Calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.

SAL_MINIMO = 1621

salário = int(input('\nDigite o salário do funcionário: '))

print(f'\nO salário deste funcionário é equivalente a {salário / SAL_MINIMO:.3f} salários mínimos')
