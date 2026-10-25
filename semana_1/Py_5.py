# Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. 
# Faça um programa que receba o salário fixo de um funcionário e o valor de suas vendas, 
# calcule e mostre a comissão e o salário final do funcionário.

# Sugestões:

# Variáveis de entrada de dados: salario_fixo, valor_vendas
# Variável calculada: comissao, salario_final

# comissao = valor_venda * 4 / 100
# salario_final = salario_fixo + comissao

SALÁRIO = 1500

com = float(input('\nQual o valor das vendas que este funcíonario fez ? '))

sal_final = SALÁRIO + ((com / 100) * 4)

print('\nSalário final: ' + str(sal_final))
