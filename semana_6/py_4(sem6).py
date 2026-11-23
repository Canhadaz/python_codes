with open(r"frases.txt", "r", encoding = "utf-8") as arq:
    print(arq.read())

busca = input('Digite a palavra desejada:\n--> ')

with open(r"frases.txt", "r") as arq:
    for linha in arq:
        palavras = linha.lower().split()

        if busca.lower() in palavras:
            print(f'A palavra "{busca}" foi encontrada no arquivo')
            break
    else:
        print(f'A palavra "{busca}" não foi encontrada no arquivo')