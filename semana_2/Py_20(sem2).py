# Crie um programa em Python que simule uma calculadora simples utilizando o comando de seleção match-case.

# O programa deve permitir ao usuário escolher uma operação matemática digitando seu nome (como "soma", "subtrai", "multiplica", "divide" ou "potência"), e aplicar essa operação sobre dois valores digitados pelo usuário.

# ⚙️ Requisitos:

# Os dois valores devem ser armazenados em variáveis simples (por exemplo, a = 12 e b = 4).
# O programa deve utilizar match-case para selecionar a operação com base na string digitada pelo usuário.
# Não é permitido o uso de listas, tuplas ou qualquer estrutura de coleção.
# Deve haver tratamento para divisão por zero.
# A saída deve ser clara e incluir o resultado da operação.

print('\nESCOLHA UMA DAS OPÇÕES ABAIXO:' \
      '\n1º "soma";\n2º "subtrai";\n3º "multiplica";\n4º "divide";\n5º "potência".')

tipo = input('\nOPÇÃO ESCOLHIDA: ').lower()

if tipo != 'soma' and tipo != 'subtrai' and tipo != 'multiplica' and tipo != 'divide' and tipo != 'potência':
    print('\nERRO: TIPO DE OPÇÃO INVALÍDA!')
    exit()

print(f'\nDIGITE OS NÚMEROS PARA O CALCULO DE "{tipo}"')
num1 = int(input('1º número --> '))
num2 = int(input('2º número --> '))

if num1 <= 0 or num2 <= 0:
    print('\nAmbos os números devem ser maiores que "0"')
    exit()

match tipo:
    case "soma":
        print(f'\nRESULTADO: {num1} + {num2} = {num1 + num2}')
    case "subtrai":
        print(f'\nRESULTADO: {num1} - {num2} = {num1 - num2}')
    case "multiplica":
        print(f'\nRESULTADO: {num1} x {num2} = {num1 * num2:.2f}')
    case "divide":
        print(f'\nRESULTADO: {num1} / {num2} = {num1 / num2:.2f}')
    case "potência":
        print(f'\nRESULTADO: {num1} ** {num2} = {num1 ** num2}')
