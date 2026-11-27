import csv

ARQUIVO = "salarios.csv"
COLUNAS = ["nome", "salarios"]

# armazenar os nomes em uma lista
# armazenar os salarios em uma matriz

def calcular_media_salarial(salarios: list) -> list:

    media_cada = []

    for linha in range(len(salarios)):
        soma = 0.0
        for coluna in range(len(salarios[linha])):
            soma += salarios[linha][coluna]
        media_cada.append(soma/len(salarios[linha]))

    return media_cada

def mostrar_maior_salario(medias_salarios: list) -> float:

    maior = 0.0

    for i in range(len(medias_salarios)):
        if maior < medias_salarios[i]:
            maior = medias_salarios[i]

    return maior

def main():
    nomes = []
    salarios = []

    with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
        leitor = csv.DictReader(arq)

        salario = []
        for linha in leitor:
            nomes.append(linha["nome"])

            salario = linha["salarios"].strip("[]").split(",")
            salario = [float(sal) for sal in salario]

            salarios.append(salario)

    media_cada = calcular_media_salarial(salarios)
    print("\tMÉDIA SALARIAL:\n")
    for i in range(len(media_cada)):
        print(f"{nomes[i]:20} --> {media_cada[i]:.2f}")
    print("-" * 40)

    maior_salario = mostrar_maior_salario(media_cada)
    print("\tMAIOR SALARIO:")
    print(f"\n{maior_salario:.2f}")
    print("-" * 40)
    
if __name__ == "__main__":
    main()