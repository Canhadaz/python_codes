# Escreva um programa que simule um sistema de aprovação de crédito para um banco. Para um cliente ser aprovado, ele deve atender a todos os seguintes critérios:
# Ter idade entre 25 e 60 anos.
# Ter um salário mensal maior ou igual a R$ 3.000,00.
# Não ter nenhuma dívida pendente. Caso o cliente tenha dívidas, ele ainda pode ser aprovado se:
# O total de suas dívidas não ultrapassar 20% do seu salário.
# Ele tiver realizado pelo menos 2 pagamentos nos últimos 6 meses.
# O programa deve solicitar ao usuário:
# Sua idade (um número inteiro).
# Seu salário mensal (um número real).
# O total de suas dívidas (um número real).
# O número de pagamentos realizados nos últimos 6 meses (um número inteiro).
# O programa deve então verificar os critérios e informar se o crédito foi "aprovado" ou "negado".

idade = int(input('\nDigite a sua idade: '))
salario = float(input('Digite o seu salário mensal: '))
divida = input('Possui alguma divida pendente ? [S/N] ').lower()

if divida != "s" and divida != "n" or len(divida) > 1:
    print('\nDigite um valor valído para a divida.')
    exit()

pagamentos = int(input('Qual o número de pagamentos do cliente realizados nos últimos 6 meses ? '))

if idade >= 25 and idade <= 60:
    if salario >= 3000:
        if divida == "n":
            print('\nVocê está aprovado para crédito!')
        elif pagamentos >= 2:
            print('\nVocê está aprovado para crédito.')
        else:
            print('\nREPROVADO.')
            exit()
    else: 
        print('\nREPROVADO.')
        exit()
else:
    print('\nREPROVADO.')
    exit()