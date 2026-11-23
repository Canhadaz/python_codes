def contar_vogais(diretorio: str):
    vogais = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    with open(f"{diretorio}", "r", encoding = "utf-8") as arq:
        for linha in arq:
            for letra in linha.lower():
                if letra in vogais:
                    vogais[letra] += 1
    
    for i in vogais:
        print(f"{i} --> {vogais[i]}")

def contar_consoantes(diretorio: str):
    consoantes = dict.fromkeys("bcdfghjklmnpqrstvwxyz", 0)

    with open(f"{diretorio}", "r", encoding = "utf-8") as arq:
        for linha in arq:
            for letra in linha.lower():
                if letra in consoantes:
                    consoantes[letra] += 1
    
    for i in consoantes:
        print(f"{i} --> {consoantes[i]}")

def contagem_completa(diretorio: str):
    alfabeto = dict.fromkeys("abcdefghijklmnopqrstuvwxyz", 0)

    with open(f"{diretorio}", "r", encoding = "utf-8") as arq:
        for linha in arq:
            for letra in linha.lower():
                if letra in alfabeto:
                    alfabeto[letra] += 1
    
    for i in alfabeto:
        print(f"{i} --> {alfabeto[i]}")

def exibir_original(diretorio: str):
    with open(f"{diretorio}", "r", encoding = "utf-8") as arq:
        print(f"\n{arq.read()}")

def main():
    while True: 
        print("ESCOLHA UMA DAS OPÇÕES ABAIXO:\n"
        "1. **Contar vogais**: Abrir o arquivo e exibir a frequência de cada vogal (a, e, i, o, u).\n"
        "2. **Contar consoantes**: Exibir a frequência de cada consoante do alfabeto.\n"
        "3. **Contagem completa**: Mostrar a frequência de todas as letras (a–z), organizadas em ordem alfabética.\n"
        "4. **Exibir texto original**: Mostrar o conteúdo completo do arquivo.\n"
        "5. **Sair**: Encerrar o programa.\n")

        while True:
            try:
                resposta = int(input("--> "))

                if 1 > resposta or resposta > 5:
                    raise ValueError
                break

            except ValueError:
                print('\nDigite um valor numérico válido -> (1 - 5)')

        if resposta == 5:
            break

        while True:
            diretorio = input("DIGITE O DIRETÓRIO DO ARQUIVO:\n--> ")
            try:
                arquivo = open(f"{diretorio}", "r", encoding="utf-8")
                    #print(arq.read())
                if arquivo == False:
                    raise FileNotFoundError
                arquivo.close()
                break

            except FileNotFoundError:
                print('\nArquivo não encontrado!')

        match resposta:
            case 1:
                contar_vogais(diretorio)
            case 2:
                contar_consoantes(diretorio)
            case 3:
                contagem_completa(diretorio)
            case 4:
                exibir_original(diretorio)

if __name__ == "__main__":
    main()
    