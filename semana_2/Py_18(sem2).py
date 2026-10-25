# Sistema de Classificação de Risco de Investimento
# Você deve criar um programa para um sistema bancário que avalia o risco de investimento de um cliente com base nos seguintes critérios:
# O cliente deve ser classificado em uma das seguintes categorias de risco:
# Baixo Risco: Idade entre 30 e 50 anos, renda mensal superior a R$ 10.000,00 e sem histórico de dívidas nos últimos 2 anos.
# Médio Risco: Idade entre 25 e 60 anos, renda mensal entre R$ 5.000,00 e R$ 10.000,00, e histórico de dívidas inferior a R$ 5.000,00 nos últimos 2 anos.
# Alto Risco: Qualquer cliente que não se enquadre nos critérios acima.
# O programa deve calcular a "Pontuação de Crédito" do cliente com base na seguinte fórmula: Pontuação = (renda mensal / 1000) - (total de dívidas / 2000) + (idade / 2). Use a pontuação para verificar se a classificação de risco pode ser ajustada:
# Se a pontuação for maior que 80, o cliente é movido para uma categoria de risco inferior (por exemplo, de "Médio Risco" para "Baixo Risco").
# Solicite ao usuário as seguintes informações:
# Idade (número inteiro).
# Renda mensal (número real).
# Histórico de dívidas nos últimos 2 anos.
# No final, informe:
# A categoria de risco inicial.
# A pontuação de crédito.
# A categoria de risco ajustada, se aplicável.

idade = int(input('\nIDADE: '))
renda = float(input('Renda mensal: '))
dividas = int(input('Histórico de dividas nos últimos dois anos: '))

print('\n---------------------------')
print('CATEGORIA DE RISCO INICIAL:')

status = 0

if idade >= 25 and idade <= 60:
    if idade >= 30 and idade <= 50:
        if dividas == 0 and renda > 10000:
            print('\nBaixo risco de investimento.')
        elif dividas < 5000 and renda >= 5000:
            print('\nMédio risco de investimento.')
            status = 1
        else:
            print('\nAlto risco de investimento.')
            status = 2
    elif renda >= 5000 and dividas < 5000:
            print('\nMédio risco de investimento.')
            status = 1
    else:
        print('\nAlto risco de investimento.')
        status = 2
else:
    print('\nAlto risco de investimento.')
    status = 2
print('---------------------------')

pontuação = (renda/1000) - (dividas/2000) + (idade/2)

print(f'\nPONTUAÇÃO DE CRÉDITO: {pontuação:.2f}')

if pontuação > 80:
    match status:
        case 1:
            print('\nCategoria de risco ajustada:\n--> Baixo risco de investimento.')
        case 2:
            print('\nCategoria de risco ajustada:\n--> Médio risco de investimento.')
            






