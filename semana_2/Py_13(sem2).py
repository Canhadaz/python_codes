# Faça um programa que receba o salário de um funcionário e, usando a tabela a seguir, calcule e mostre o novo salário:

# Faixa Salarial                                                                                                    % de aumento
# ----------------------------------------------------------------------------------------------------------------------------
# até R$ 300,00                                                                                                      50%
# R$ 300,00 (não incluso)  até  R$ 500,00 (incluso)                                               40%
# R$ 500,00 (não incluso)  até  R$ 700,00 (incluso)                                               30%
# R$ 700,00 (não incluso)  até  R$ 800,00 (incluso)                                               20%
# R$ 800,00 (não incluso)  até  R$ 1000,00 (incluso)                                             10%
# Acima de   R$ 1000,00                                                                                        5%

sal = int(input('\nInforme o salário: '))

if sal <= 300:
    print('\nNOVO SALÁRIO: ' + str(sal + sal * 1/2))
elif sal <= 500:
    print('\nNOVO SALÁRIO: ' + str(sal + sal * 40/100))
elif sal <= 700:
    print('\nNOVO SALÁRIO: ' + str(sal + sal * 30/100))
elif sal <= 800:
    print('\nNOVO SALÁRIO: ' + str(sal + sal * 20/100))
elif sal <= 1000:
    print('\nNOVO SALÁRIO: ' + str(sal + sal * 10/100))
else:
    print('\nNOVO SALÁRIO: ' + str(sal + sal * 5/100))