# O somatório é uma simbologia matemática usada para representar somas sucessivas de termos em uma sequência. 
# Ele é comumente utilizado para representar fórmulas e expressões que envolvem somas sucessivas de elementos, 
# tal como a média aritmética e as fórmulas usadas na área da estatística.
# Simbolicamente, o somatório e seus elementos pontuais podem ser representados da seguinte forma:
# Somatoria_01

# --------------------------------------------------------------------------------------------------------------------------------

# A partir dessa notação e aplicação, desenvolva um algoritmo que calcule, sem usar estruturas de repetição, apenas seqüencial, a seguinte soma: 

#  Somatoria_01

# Os valores de cada elemento do conjunto de X devem ser digitados pelo usuário, o programa deverá mostrar os valores 
# intermediários da soma, ao final, o resultado da  soma completa.

num3 = int(input("Insira o numero 3: "))
num4 = int(input("Insira o numero 4: "))
num5 = int(input("Insira o numero 5: "))
num6 = int(input("Insira o numero 6: "))
num7 = int(input("Insira o numero 7: "))

print("\nSoma 1 : ", str(num3 + num4))
print("Soma 2 : ", str((num3 + num4) + num5))
print("Soma 3 : ", str(((num3 + num4) + num5) + num6))
print("Soma 4 : ", str((((num3 + num4) + num5) + num6) + num7))


