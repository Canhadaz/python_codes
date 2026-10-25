# Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificação.

# Tabela 1 – Percentual de aumento
# -----------------------------------------------------------------------------------
# Preço                                                                %
# -----------------------------------------------------------------------------------
# até R$ 50,00                                                      5
# entre R$ 50,00 e R$ 100,00                             10
# acima de R$ 100,00                                        15
 
# Tabela 2 – Classificações
# ------------------------------------------------------------------------------------------
# Novo Preço                                                                       Classificação
# ------------------------------------------------------------------------------------------
# até R$ 80,00                                                                      Barata
# entre R$ 80,00  e R$ 120,00(inclusive)                              Normal
# entre R$ 120,00  e R$ 200,00(inclusive)                            Caro
# maior que R$ 200,00                                                        Muito Caro

preço = int(input('Digite o valor do produto: '))

novo_p = 0

if preço <= 50:
    novo_p = preço + preço * 5/100
    print(f'\nO aumento do valor do produto será de 5%, totalizando : R${novo_p:.2f}.')
elif preço > 50 and preço <= 100:
    novo_p = preço + preço * 10/100
    print(f'\nO aumento do valor do produto será de 10%, totalizando : R${novo_p:.2f}.')
else:
    novo_p = preço + preço * 15/100
    print(f'\nO aumento do valor do produto será de 15%, totalizando : R${novo_p:.2f}.')

print('\n\nCLASSIFICAÇÃO do novo valor:\n')

if novo_p <= 80:
    print('\nproduto classificado como -- BARATO --')
elif novo_p > 80 and novo_p <= 120:
    print('\nproduto classificado como -- NORMAL --')
elif novo_p > 120 and novo_p <= 200:
    print('\nproduto classificado como -- CARO --')
else:
    print('\nproduto classificado como -- MUITO CARO --')
