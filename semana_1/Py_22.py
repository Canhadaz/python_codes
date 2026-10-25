# Análise de Dígitos Repetidos
# Você deve desenvolver um programa em Python que receba como entrada 3 números inteiros positivo (Variáveis Diferentes).
# O programa deverá analisar esses três dígitos exibir e informar qual o padrão de repetição entre eles.

# Restrições:
# O programa não pode utilizar estruturas de seleção (if, else, match, case) nem estruturas de repetição (for, while).
# Deve-se utilizar apenas comandos de entrada, processamento e saída.
# input( )
# a == b,  a != B,  (a == b) * (b == c) e etc...
# print( )
# O uso de listas, funções ou módulos externos também está proibido.
# Regras de análise:
# O programa deve identificar e exibir uma das seguintes mensagens:

# "Todos os dígitos são iguais." — se os três dígitos forem idênticos.
# "Todos os dígitos são diferentes." — se os três dígitos forem distintos entre si.
# "Dois dígitos são iguais." — se houver exatamente dois dígitos iguais.
# Exemplo de entrada:
# Digite 3 dígitos: 1 2 1
# Exemplo de saída:
# Dois dígitos são iguais.

#(sem função, sem if else, sem repetição (apenas proposicional))

print('\nDigite 3 números.')

num1 = int(input(''))
num2 = int(input(''))
num3 = int(input(''))

print('\nAmbos os números possuem o mesmo valor.' * (num1 == num2 and num2 == num3) +
      '\nTodos os números são diferentes.' * (num1 != num2 and num2 != num3) +
      '\nDois números são iguais.' * (((num1 == num2 and num1 != num3) or (num2 == num3 and num2 != num1) or (num1 != num2 and num1 == num3))))