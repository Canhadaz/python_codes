# Faça um programa que receba o número de horas trabalhadas (NHT), o valor do salário mínimo (SM) 
# e o número de horas extras trabalhadas (NHET). Calcule e mostre o salário a receber (SR) seguindo as regras a seguir:

# a) a hora trabalhada vale 1/8 do salário mínimo (HT);
# b) a hora extra vale 1/4 do salário mínimo (HE);
# c) o salario bruto (SB) equivale ao número de horas trabalhadas (NHT) multiplicado pelo valor da hora trabalhada (HT);
# d) a quantia a receber (QR) pelas horas extras equivale ao número de horas extras trabalhadas (NHET) multiplicado pelo valor da hora extra (HE);
# e) o salário a receber (RS) equivale ao salário bruto (SB) mais a quantia a receber (QR) pelas horas extras


SM = int(input("\nQual seu salário ? "))
NHT = int(input("Insira a quantidade de horas trabalhadas: "))
NHET =int(input("Insira a quantidade de horas extras: "))

HT = int(SM * 1/8)
HE = int(SM * 1/4)
SB = int(HT * NHT)
QR = int(NHET * HE)

RS = print("\nSeu salário é: " + str(SB + QR))

