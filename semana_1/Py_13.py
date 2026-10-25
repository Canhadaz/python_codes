# Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:

# a) a idade dessa pessoa em anos;
# b) a idade dessa pessoa em meses;
# c) a idade dessa pessoa em dias;
# d) a idade dessa pessoa em semanas.

from datetime import date

DATA_ATUAL = date.today()

# dia de nascimento e tempo de vida
def Calculo(idade:list, tempo: list):

    print('\nTOTALIZANDO: ')
    print('\n--> ' + str((tempo[0])) + ' anos de vida.')
    print('\n--> ' + str((tempo[0] * 12) + tempo[1]) + ' meses de vida.')
    print(f'\n--> {((tempo[0] * 365) + (tempo[1] * 30) + tempo[2]) / 7:.2f} semanas de vida.')
    print('\n--> ' + str((tempo[0] * 365) + (tempo[1] * 30) + tempo[2]) + ' dias de vida.')

def Formatado(idade: list):

    if any(data < 1 for data in idade) or idade[0] > 2026 or idade[1] > 12 or idade[2] > 30:
        print('\nColoque sua data de nascimento real \nOBS: O sistema não conta meses com mais de 30 dias)')
        exit()

    tempo = [] #tempo de vida
    tempo.append(DATA_ATUAL.year - idade[0])
    tempo.append(DATA_ATUAL.month + (12 - idade[1]))
    tempo.append(DATA_ATUAL.day + (30 - idade[2]))

    print('\nVocê tem: ' + str(tempo[0]) + ' anos ' +
          str(tempo[1]) + ' meses e ' +
          str(tempo[2]) + ' dias desde seu nascimento.') #só finge q todos meses tem 30 dias.

    return tempo

def Main():

    idade = []

    print('\nDigite sua idade no formato AAAA|MM|DD: ')

    for i in range(3):
        idade.append(int(input('Ano == '))) if i == 0 else idade.append(int(input('Mês == '))) if i == 1 else idade.append(int(input('Dia == ')))

    tempo = Formatado(idade)
    Calculo(idade, tempo)

Main()