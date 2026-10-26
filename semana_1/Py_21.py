# Escreva um programa em Python que classifique um número inteiro 
# quanto à sua divisibilidade por 3 e por 5, utilizando apenas lógica proposicional.

# O programa não deve utilizar estruturas de controle como if, else, match, for, while, nem funções ou listas.

# A saída deve ser uma mensagem textual indicando:

# Se o número é divisível por 3 e por 5.

# Se é divisível apenas por 3.

# Se é divisível apenas por 5.

# Se não é divisível por nenhum dos dois.

x = int(input('\nDigite um número: '))

div_3 = x % 3 == 0
div_5 = x % 5 == 0

print('\nO número é divisivel por 3 e 5.' * (div_3 and div_5) +
      '\nO número é divisivel por 3, mas NÃO por 5.' * (div_3 and not div_5) +
      '\nO número é divisivel por 5, mas NÃO por 3.' * (div_5 and not div_3) +
      '\nO número não é divisivel por 3 e nem por 5.' * (not div_3 and not div_5))