# Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:

# a) a idade dessa pessoa em anos;
# b) a idade dessa pessoa em meses;
# c) a idade dessa pessoa em dias;
# d) a idade dessa pessoa em semanas.

atual = (int(input("Insira o ano atual: ")))
nascimento = (int(input("Insira o seu ano de nascimento: ")))

print('Sua idade em anos :' + str(atual - nascimento))
print('Sua idade em meses :' + str((atual - nascimento) * 12))
print('Sua idade em dias :' + str((atual - nascimento) * 315))
print('Sua idade em semanas :' + str(atual - nascimento) * 52)
