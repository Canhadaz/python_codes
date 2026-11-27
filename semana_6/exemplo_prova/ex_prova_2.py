import csv

ARQUIVO = "notas.csv"

def calcular_medias(notas: list) -> list:

    medias = []

    for l in range(len(notas)):
        soma = 0
        for c in range(len(notas[l])):
            soma += notas[l][c]
        medias.append(soma/len(notas[l]))

    return medias

def maior_media(medias: list) -> int:

    indice = 0 
    maior = 0

    for i in range(len(medias)):
        if maior < medias[i]:
            maior = medias[i]
            indice = i

    return indice

def menor_media(medias: list) -> int:
    
    indice = 0
    for i in range(len(medias)):
        if medias[indice] > medias[i - 1]:
            indice = i - 1

    return indice

def media_geral(medias: list) -> float:

    soma = 0
    
    for i in range(len(medias)):
        soma += medias[i]
    geral = soma/len(medias)

    return geral

def listar_aprovados(nomes: list, medias: list) -> list:

    aprovados = []

    for i in range(len(medias)):
        if medias[i] >= 6.0:
            aprovados.append(nomes[i])

    return aprovados

def listar_reprovados(nomes: list, medias: list) -> list:

    reprovados = []

    for i in range(len(medias)):
        if medias[i] < 6.0:
            reprovados.append(nomes[i])

    return reprovados

def media_avaliacoes(notas: list) -> list:

    media_avaliacoes = []
    soma = [0 for i in range(len(notas))]
    contador = 0

    for linha in range(len(notas)):
        for coluna in range(len(notas[linha])):
            soma[coluna] += notas[linha][coluna]
        contador += 1

    for i in range(contador):
        media_avaliacoes.append(soma[i]/contador)

    return media_avaliacoes

def main():
    nomes = []
    notas = []

    with open(ARQUIVO, "r", encoding="utf-8", newline="") as arq:
        leitor = csv.DictReader(arq)

        for linha in leitor:
            nomes.append(linha["nome"])

            nota = linha["notas"].strip("[]").split(",")
            nota = [float(n) for n in nota]

            notas.append(nota)

    medias = calcular_medias(notas)
    ma_media = maior_media(medias)
    me_media = menor_media(medias)
    me_geral = media_geral(medias)

    print(f"\tMÉDIAS ALUNOS:\n")
    for i in range(len(medias)):
        print(f"{nomes[i]:15} --> {medias[i]}")
    print("-" * 40)

    print(f"\tMAIOR MÉDIA:\n")
    print(f"{nomes[ma_media]:15} --> {medias[ma_media]}")
    print("-" * 40)

    print(f"\tMENOR MÉDIA:\n")
    print(f"{nomes[me_media]:15} --> {medias[me_media]}")
    print("-" * 40)

    print(f"\tMÉDIA GERAL:\n")
    print(f"{me_geral}")
    print("-" * 40)

    aprovados = listar_aprovados(nomes, medias)
    print(f"\tALUNOS APROVADOS:\n")
    for i in range(len(aprovados)):
        print(aprovados[i])
    print("-" * 40)

    reprovados = listar_reprovados(nomes, medias)
    print(f"\tALUNOS REPROVADOS:\n")
    for i in range(len(reprovados)):
        print(reprovados[i])
    print("-" * 40)

    media_provas = media_avaliacoes(notas)
    print(f"\tMÉDIAS AVALIAÇÕES:\n")
    for i in range(len(media_provas)) :
        print(f"{i + 1:3}° --> {media_provas[i]}")
    print("-" * 40)

if __name__ == "__main__":
    main()