# Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:

# A quantidade de pessoas em cada faixa etária;
# a percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas.
# FAIXA ETÁRIA                       IDADE
# ----------------------------------------------------
# 1ª                                         até 15 anos
# 2ª                                        de 16 a 30 anos
# 3ª                                        de 31 a 45 anos
# 4ª                                       de 46 a 60 anos
# 5ª                                       Acima de 61 anos

crianca = 0
adulto = 0
meia_idade = 0
velho = 0
caixao = 0

for i in range(10):
    idade = int(input('Fale sua idade: '))

    if idade <= 15:
        crianca += 1
    elif idade <= 30:
        adulto += 1
    elif idade <= 45:
        meia_idade += 1
    elif idade <= 60:
        velho += 1
    else:
        caixao += 1
     
print(f'\n{(crianca / 10) * 100}% de até 15 anos\n{(adulto / 10) * 100}% de até 30 anos\n{(meia_idade / 10) * 100}% de até 45 anos\n{(velho / 10) * 100}% de até 60 anos\n{(caixao / 10) * 100}% com mais de 60 anos')