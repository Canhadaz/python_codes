# Faça um programa quer receba duas notas, calcule e mostre a média ponderada dessas notas, 
# considerando peso 2 para primeira nota e peso 3 para a segunda nota.

# Sugestões:
# Variáveis de entrada de dados: nota1, nota2.
# Variável calculada: média

# média = ((nota1 * 2) + (nota2 *  3)) / (2 + 3)

nota1 = int(input('\nNota 1: '))
nota2 = int(input('\nNota 2: '))

média = ((nota1 * 2) + (nota2 *  3)) / (2 + 3)

print("\n" + str(média))