# Criar um arquivo com frases

# Crie um programa que solicite ao usuário 3 frases e grave cada uma delas em uma nova linha no arquivo frases.txt.

with open(r"frases.txt", 'w') as frases:
    for i in range(3):
        f = input('Digite uma frase:\n--> ')
        frases.write(f + '\n')

with open( r"frases.txt", 'r') as frases:
    print(frases.read())