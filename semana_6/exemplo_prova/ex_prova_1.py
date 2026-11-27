import csv

ARQUIVO_SALARIOS = "registro.csv"
ARQUIVO_PRODUTIVIDADE = "produtividade.csv"
ARQUIVO_RESULTADOS = "desempenho.csv"

def ler_arquivo(diretorio: str, coluna: str) -> tuple:
    nomes = []
    matriz = []

    with open(diretorio, "r", newline="", encoding="utf-8") as arq:
        leitor = csv.DictReader(arq)

        for linha in leitor:
            nomes.append(linha["nome"])

            valores = linha[coluna].strip("[]").split(",")
            valores = [float(valor) for valor in valores]

            matriz.append(valores)

    return nomes, matriz


def organizar_produtividade(nomes: list, nomes_prod: list, produtividade: list) -> list:
    matriz = []

    for i in range(len(nomes)):
        encontrado = False

        for j in range(len(nomes_prod)):
            if nomes[i] == nomes_prod[j]:
                matriz.append(produtividade[j])
                encontrado = True
                break

        if not encontrado:
            raise ValueError(f"Funcionário não encontrado: {nomes[i]}")

    return matriz


def calcular_medias(matriz: list) -> list:
    medias = []

    for linha in range(len(matriz)):
        soma = 0.0

        for coluna in range(len(matriz[linha])):
            soma += matriz[linha][coluna]

        medias.append(soma / len(matriz[linha]))

    return medias


def calcular_totais(matriz: list) -> list:
    totais = []

    for linha in range(len(matriz)):
        soma = 0.0

        for coluna in range(len(matriz[linha])):
            soma += matriz[linha][coluna]

        totais.append(soma)

    return totais


def maior_valor(valores: list) -> int:
    maior = valores[0]
    indice = 0

    for i in range(len(valores)):
        if valores[i] > maior:
            maior = valores[i]
            indice = i

    return indice


def custo_por_tarefa(salarios: list, tarefas: list) -> list:
    custos = []

    total_salarios = calcular_totais(salarios)
    total_tarefas = calcular_totais(tarefas)

    for i in range(len(total_salarios)):
        if total_tarefas[i] > 0:
            custos.append(total_salarios[i] / total_tarefas[i])
        else:
            custos.append(None)

    return custos


def gerar_ranking(nomes: list, produtividade: list) -> list:
    ranking = []

    for i in range(len(nomes)):
        ranking.append([nomes[i], produtividade[i]])

    # Bubble Sort - ordem decrescente
    for i in range(len(ranking)):
        for j in range(len(ranking) - 1 - i):

            if ranking[j][1] < ranking[j + 1][1]:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

    return ranking


def exportar_resultados(nomes: list, medias_salarios: list, medias_tarefas: list, custos: list):

    colunas = [
        "nome",
        "media_salarial",
        "media_produtividade",
        "custo_por_tarefa"
    ]

    with open(ARQUIVO_RESULTADOS, "w", newline="", encoding="utf-8") as arq:
        escritor = csv.DictWriter(arq, fieldnames=colunas)

        escritor.writeheader()

        for i in range(len(nomes)):
            escritor.writerow({
                "nome": nomes[i],
                "media_salarial": f"{medias_salarios[i]:.2f}",
                "media_produtividade": f"{medias_tarefas[i]:.2f}",
                "custo_por_tarefa": (
                    f"{custos[i]:.2f}" if custos[i] is not None else "N/A"
                )
            })

def main():

    try:
        nomes, salarios = ler_arquivo(ARQUIVO_SALARIOS, "salarios")

        nomes_prod, produtividade = ler_arquivo(ARQUIVO_PRODUTIVIDADE, "tarefas")

        produtividade = organizar_produtividade(nomes, nomes_prod, produtividade)

        medias_salarios = calcular_medias(salarios)
        medias_tarefas = calcular_medias(produtividade)

        custos = custo_por_tarefa(salarios, produtividade)

        maior_salario = maior_valor(medias_salarios)
        mais_produtivo = maior_valor(medias_tarefas)

        ranking = gerar_ranking(nomes, medias_tarefas)

        print("\n\tMÉDIA SALARIAL\n")

        for i in range(len(nomes)):
            print(f"{nomes[i]:20} --> R$ {medias_salarios[i]:.2f}")

        print("-" * 45)
        print("\n\tMÉDIA DE PRODUTIVIDADE\n")

        for i in range(len(nomes)):
            print(f"{nomes[i]:20} --> {medias_tarefas[i]:.2f}")

        print("-" * 45)
        print("\n\tMAIOR MÉDIA SALARIAL\n")

        print(f"Funcionário: {nomes[maior_salario]}")
        print(f"Salário: R$ {medias_salarios[maior_salario]:.2f}")

        print("-" * 45)
        print("\n\tFUNCIONÁRIO MAIS PRODUTIVO\n")

        print(f"Funcionário: {nomes[mais_produtivo]}")
        print(f"Média: {medias_tarefas[mais_produtivo]:.2f}")

        print("-" * 45)
        print("\n\tCUSTO POR TAREFA\n")

        for i in range(len(nomes)):
            if custos[i] is not None:
                print(f"{nomes[i]:20} --> R$ {custos[i]:.2f}")
            else:
                print(f"{nomes[i]:20} --> Indefinido")

        print("-" * 45)
        print("\n\tRANKING DE PRODUTIVIDADE\n")

        for i in range(len(ranking)):
            print(f"{i + 1}º - {ranking[i][0]:15} --> {ranking[i][1]:.2f}")

        print("-" * 45)

        exportar_resultados(
            nomes, medias_salarios, medias_tarefas, custos
        )

        print("\nRESULTADOS EXPORTADOS COM SUCESSO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")

    except ValueError as erro:
        print(f"VALOR INVÁLIDO: {erro}")

    except OSError as erro:
        print(f"ERRO AO MANIPULAR O ARQUIVO: {erro}")


if __name__ == "__main__":
    main()
