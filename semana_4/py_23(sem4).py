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

    matriz = []
    for i in range(len(palavras)):
        linha = []
        for j in range(len(palavras[i])):
            linha.append(palavras[i][j])
        matriz.append(linha)

    if len(palavras) == 0:
        print("Nenhuma palavra foi digitada.")
    else:
        print("\nVetor de palavras:")
        print(palavras)
        print("\nMatriz de letras:")
        for i in range(len(matriz)):
            print(matriz[i])

        if rodada == 1:
            total_letras = 0
            pos_longa = 0
            pos_curta = 0
            for i in range(len(matriz)):
                total_letras += len(matriz[i])
                if len(matriz[i]) > len(matriz[pos_longa]):
                    pos_longa = i
                if len(matriz[i]) < len(matriz[pos_curta]):
                    pos_curta = i

            print(f"\nQuantidade de palavras: {len(palavras)}")
            print(f"Quantidade total de letras: {total_letras}")
            print(f"Palavra mais longa: {palavras[pos_longa]} ({len(matriz[pos_longa])} letras)")
            print(f"Palavra mais curta: {palavras[pos_curta]} ({len(matriz[pos_curta])} letras)")