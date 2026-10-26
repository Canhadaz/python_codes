# Faça um programa para Verificar se um caractere é uma vogal

# Usar lógica proposicional para verificar se o caractere digitado é uma vogal (a, e, i, o, u), 
# considerando letras minúsculas e sem usar if.

# Saída:

# imprimir: "É uma vogal" ou "Não é uma vogal"

letras = input('Digite uma letra: ')

vogal = (letras == "a" or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u')

print('\nÉ vogal' * vogal + '\nnão é vogal' * (not vogal))