# Uma agência bancária possui três tipos de investimentos, conforme o quadro a seguir. Faça um programa que receba o tipo de investimento e o valor do investimento e que calcule e mostre o valor corrigido de acordo com o tipo de investimento. 

# Tipo                                                      Descrição                                                           Rendimento mensal
# -------------------------------------------------------------------------------------------------------------------------------------
# 1                                                            Poupança                                                             3%
# 2                                                            Fundos de renda fixa                                                 4%
# 3                                                            Fundos de renda variável                                             5%

valor = int(input('\nQual o valor do investimento ? '))
tipo = int(input('QUAL O TIPO DO INVESTIMENTO?\n 1 = POUPANÇA\n 2 = FUNDO DE RENDA FIXA\n 3 = FUNDOS DE RENDA VARÍAVEL\n -->'))

if tipo == 1:
    print('\nInvestimento na poupança: ' + str(valor + valor * 3/100))
elif tipo == 2:
    print('\nInvestimento no fundo de renda fixa: ' + str(valor + valor * 4/100))
elif tipo == 3:
    print('\nInvestimento no fundo de renda varíavel: ' + str(valor + valor * 5/100))
else:
    print('\nINFORME UM VALOR VALÍDO')    
