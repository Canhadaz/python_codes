for rodada in range(2):
    if rodada == 0:
        frase = "ola mundo estou aqui"
        print("=== Tarefa principal ===")
    else:
        print("\n=== Desafio extra ===")
        frase = input("Digite uma frase: ")

    palavras = []
    atual = ""
    for i in range(len(frase)):
        if frase[i] != " ":
            atual += frase[i]
        elif atual != "":
            palavras.append(atual)
            atual = ""
    if atual != "": 
        palavras.append(atual)

    print("Vetor de palavras:")
    print(palavras)

    if rodada == 1:
        print(f"Quantidade de palavras: {len(palavras)}")