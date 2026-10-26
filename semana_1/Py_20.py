# Escreva um programa em Python que classifique um número inteiro quanto 
# à sua paridade (par ou ímpar) e ao seu sinal (positivo, negativo ou zero), utilizando apenas lógica proposicional.
# O programa não deve utilizar estruturas de controle como if, else, match, for, while, nem funções ou listas.
# A saída deve ser uma mensagem textual indicando a classificação correta do número digitado.

 
# Como funciona:
# As variáveis booleanas devem virar 0 ou 1.

# Multiplicamos essas variáveis para gerar a mensagem correta.

# O programa exibe a mensagem correta sem usar if, else, match, for, while, funções ou listas.

x = int(input('\nDigite um número: '))

par = x % 2 == 0
impar = x % 2 != 0

zero = x == 0
positivo = x > 0
negativo = x < 0

print('\nPar e positivo' * (par and positivo) +
      '\nImpar e positivo' * (impar and positivo) +
      '\nPar e negativo' * (par and negativo) +
      '\nImpar e negativo' * (impar and negativo) +
      '\nZero' * zero)