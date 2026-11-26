import uuid
import csv
import os

ARQUIVO = "produtos.csv"
COLUNAS = ["id", "nome", "categoria", "preco", "quantidade"]

def gerar_id() -> str:
    return str(uuid.uuid4())

def cadastrar_produtos():

    try:
        with open(ARQUIVO, "a", newline="", encoding="utf-8") as arq:
            escritor = csv.DictWriter(arq, fieldnames=COLUNAS)

            arquivo_vazio = os.path.exists(ARQUIVO) == 0

            identificador = gerar_id()
            nome = input("DIGITE O NOME DO PRODUTO:\n--> ").lower().strip()
            categoria = input("DIGITE A CATEGORIA DO PRODUTO:\n--> ").lower().strip()
            preco = float(input("DIGITE O PREÇO DO PRODUTO:\n--> "))
            quantidade = int(input("DIGITE A QUANTIDADE (ESTOQUE) DO PRODUTO:\n--> "))

            if arquivo_vazio:
                escritor.writeheader()

            escritor.writerow({
                "id": identificador,
                "nome": nome,
                "categoria": categoria,
                "preco": preco,
                "quantidade": quantidade
            })

            print("PRODUTO ADICIONADO COM SUCESSO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:    
        print("NÃO FOI POSSÍVEL LER O ARQUIVO!")

def listar_produtos():

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)

            print("\n\t   LISTA DE PRODUTOS:\n")

            for produto in leitor:
                print(f"ID        : {produto["id"]}")
                print(f"Nome      : {produto["nome"]}")
                print(f"Categoria : {produto["categoria"]}")
                print(f"Preço     : {produto["preco"]}")
                print(f"Quantidade: {produto["quantidade"]}")
                print("-" * 50)

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:    
        print("NÃO FOI POSSÍVEL LER O ARQUIVO!")

def buscar_produto():

    encontrado = False

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)

            nome = input("DIGITE O NOME DO PRODUTO:\n--> ").lower().strip()

            print("\n\t   LISTA DE PRODUTOS:\n")

            for produto in leitor:
                if nome in produto["nome"]:
                    print(f"ID        : {produto["id"]}")
                    print(f"Nome      : {produto["nome"]}")
                    print(f"Categoria : {produto["categoria"]}")
                    print(f"Preço     : {produto["preco"]}")
                    print(f"Quantidade: {produto["quantidade"]}")
                    print("-" * 50)

                    encontrado = True

            if not encontrado:
                print("NÃO ENCONTRADO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:    
        print("NÃO FOI POSSÍVEL LER O ARQUIVO!")

def atualizar_preco():

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            produtos = list(csv.DictReader(arq))

            identificador = input("DIGITE O ID DO PRODUTO:\n--> ").lower().strip()
            preco = float(input("DIGITE O NOVO PREÇO DO PRODUTO:\n--> "))

            for produto in produtos:
                if identificador in produto["id"]:
                    produto["preco"] = preco
                    break
            else:
                print("PRODUTO NÃO ENCONTRADO!")
        
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.DictWriter(arq, fieldnames=  COLUNAS)

            escritor.writeheader()
            escritor.writerows(produtos)

            print("PREÇO ALTERADO COM SUCESSO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:    
        print("NÃO FOI POSSÍVEL LER O ARQUIVO!")

def alterar_quantidade():
    
    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            produtos = list(csv.DictReader(arq))

            identificador = input("DIGITE O ID DO PRODUTO:\n--> ").lower().strip()
            quantidade = int(input("DIGITE A NOVA QUANTIDADE (ESTOQUE) DO PRODUTO:\n--> "))

            for produto in produtos:
                if identificador in produto["id"]:
                    produto["quantidade"] = quantidade
                    break
            else:
                print("PRODUTO NÃO ENCONTRADO!")
        
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.DictWriter(arq, fieldnames=  COLUNAS)

            escritor.writeheader()
            escritor.writerows(produtos)

            print("ESTOQUE ALTERADO COM SUCESSO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:    
        print("NÃO FOI POSSÍVEL LER O ARQUIVO!")

def remover_produto():
    restantes = []
    
    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            produtos = csv.DictReader(arq)

            identificador = input("DIGITE O ID DO PRODUTO PARA REMOÇÃO:\n--> ").lower().strip()
            
            for produto in produtos:
                if identificador not in produto["id"]:
                    restantes.append(produto)
        
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.DictWriter(arq, fieldnames=  COLUNAS)

            escritor.writeheader()
            escritor.writerows(restantes)

            print("PRODUTO REMOVIDO COM SUCESSO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:    
        print("NÃO FOI POSSÍVEL LER O ARQUIVO!")

def estoque_baixo():
    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)

            print("\n\t   LISTA DE PRODUTOS:\n")

            for produto in leitor:
                if int(produto["quantidade"]) < 10:
                    print(f"ID        : {produto["id"]}")
                    print(f"Nome      : {produto["nome"]}")
                    print(f"Categoria : {produto["categoria"]}")
                    print(f"Preço     : {produto["preco"]}")
                    print(f"Quantidade: {produto["quantidade"]}")
                    print("-" * 50)

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:    
        print("NÃO FOI POSSÍVEL LER O ARQUIVO!")

def valor_total():
    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)

            identificador = input("DIGITE O ID DO PRODUTO:\n--> ").lower().strip()

            print("\n\t   LISTA DE PRODUTOS:\n")

            for produto in leitor:
                if identificador in produto["id"]:
                    print(f"ID        : {produto["id"]}")
                    print(f"Nome      : {produto["nome"]}")
                    print(f"Categoria : {produto["categoria"]}")
                    print(f"Preço     : {produto["preco"]}")
                    print(f"Quantidade: {produto["quantidade"]}")

                    print(f"\nVALOR TOTAL: {int(produto["quantidade"]) * float(produto['preco'])}")
                    
                    print("-" * 50)
                    break
            else:
                print("NÃO ENCONTRADO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:    
        print("NÃO FOI POSSÍVEL LER O ARQUIVO!")

def main():

    while True:
        print("\n\tESCOLHA UMA DAS OPÇÕES ABAIXO:\n\n"
        "1 - Cadastrar produto\n"
        "2 - Listar produtos\n"
        "3 - Buscar produto\n"
        "4 - Atualizar preço\n"
        "5 - Alterar unidades do estoque\n"
        "6 - Remover produto\n"
        "7 - Listar produtos com estoque baixo\n"
        "8 - Calcular valor total do estoque\n"
        "9 - Sair\n")

        while True:
            try:
                res = int(input("--> "))

                if 1 > res or res > 9:
                    raise ValueError

                break
            except ValueError:
                print("DIGITE UM VALOR NUMÉRICO VALÍDO DENTRE (1 - 10)")
                
        match res:
            case 1:
                cadastrar_produtos()
            case 2:
                listar_produtos()
            case 3:
                buscar_produto()
            case 4:
                atualizar_preco()
            case 5:
                alterar_quantidade()
            case 6:
                remover_produto()
            case 7:
                estoque_baixo()
            case 8:
                valor_total()
            case 9:
                print("ENCERRANDO CÓDIGO!")
                exit()

if __name__ == "__main__":
    main()