# Faça um programa que leia o arquivo frases.txt e mostre quantas linhas ele possui

with open( r"frases.txt", 'r') as frases:
    print(frases.read())

with open(r'frase.txt', 'r') as frases: 
    qnt_linhas = frases.readlines()
    print(f'Quantidade de linhas: {len(qnt_linhas)}')