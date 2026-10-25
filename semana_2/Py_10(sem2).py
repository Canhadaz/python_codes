# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do 
# distribuidor e com os impostos, ambos aplicados ao custo de fábrica.

# Sabe-se que as porcentagens são as mesmas que estão na tabela a seguir. 
# Faça um programa que receba o custo de fábrica de um carro e mostre o custo ao consumidor.

# Custo de Fábrica                                             % do distribuidor                 % dos impostos
# ------------------------------------------------------------------------------------------------------------------
# até R$ 12.000,00                                                        5                                          Isento
# entre R$ 12.000,00 e R$ 25.000,00                           10                                           15
# acima de R$ 25.000,00                                             15                                           20

fabrica = int(input('\nInforme o custo de fábrica para a produção deste veículo: '))

if fabrica <= 12000:
    print('\nO custo final do veículo será de: ' + str(fabrica + (fabrica * 5 / 100)))
elif fabrica > 12000 and fabrica <= 25000:
    print('\nO custo final do veículo será de: ' + str(fabrica + (fabrica * 10 / 100) + (fabrica * 15 / 100)))
elif fabrica > 25000:
    print('\nO custo final do veículo será de: ' + str(fabrica + (fabrica * 15 / 100) + (fabrica * 20 / 100)))
else :
    print('\nO custo de fábrica deve ser maior que R$ 0,00.')
