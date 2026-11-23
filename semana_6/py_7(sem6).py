import csv
import os

ARQUIVO = "contatos.csv"
COLUNAS = ["nome", "telefone", "email"]

def adicionar_contato():
    print('INFORME OS DADOS DO CONTATO:\n')

    while True:
        try:
            nome     = input("Nome    : ").strip()
            telefone = input("Telefone: ").strip()
            email    = input("Email   : ").strip()

            if not nome or not telefone or not email:
                raise ValueError
            break
    
        except ValueError:
            print("Preencha todos os campos!")

    arquivo_vazio = os.path.exists(ARQUIVO) == 0
    try:
        with open(ARQUIVO, "a", newline = "", encoding = "utf-8") as arq:
            escritor = csv.DictWriter(arq, fieldnames=COLUNAS)

            if arquivo_vazio:
                escritor.writeheader()

            escritor.writerow({
                "nome": nome,
                "telefone": telefone,
                "email": email
            })

            print("CONTATO ADICIONADO COM SUCESSO!")
    except (OSError, csv.Error):
        print("Não foi possível ler os contatos!")
        return None

def listar_contatos():
    try:
        with open(ARQUIVO, "r", newline = "", encoding = "utf-8") as arq:
            leitor = csv.DictReader(arq)

            print("CONTATOS:\n")

            for contato in leitor:
                print(f'Nome    : {contato["nome"]}')
                print(f'Telefone: {contato["telefone"]}')
                print(f'Email   : {contato["email"]}')
                print("")
    except FileNotFoundError:
        print("O arquivo não foi encontrado!")
        return None
    except (OSError, csv.Error):
        print("Não foi possível ler os contatos!")
        return None

def buscar_contato():
    encontrado = False
    nome = input("Digite o nome a ser buscado:\n--> ").lower().strip()

    try:
        with open(ARQUIVO, "r", newline = "", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)

            for contato in leitor:
                if nome in contato["nome"].lower():
                    print(f"Nome    : {contato["nome"]}")
                    print(f'Telefone: {contato["telefone"]}')
                    print(f'Email   : {contato["email"]}')
                    print("")

                    encontrado = True
                
            if not encontrado:
                print("Tem nada aqui com esse nome não")
    except FileNotFoundError:
        print("O arquivo não foi encontrado!")
        return None
    except (OSError, csv.Error):
        print("Não foi possível ler os contatos!")
        return None

def remover_contato():
    nome = input("Nome do contato para remover:\n--> ").strip().lower()
    restantes = []

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)

            for contato in leitor:
                if nome not in contato["nome"].lower():
                    restantes.append(contato)
    
    except FileNotFoundError:
        print("O arquivo não foi encontrado!")
        return None
    except (OSError, csv.Error):
        print("Não foi possível ler os contatos!")
        return None
    
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arq:
        escritor = csv.DictWriter(arq, fieldnames=COLUNAS)

        escritor.writeheader()
        escritor.writerows(restantes)
        print("Removido com sucesso!")

def main():
    while True: 
        print("ESCOLHA UMA DAS OPÇÕES ABAIXO:\n"
        "1. **Adicionar contato**: Solicitar nome, telefone e e-mail do usuário e salvar no arquivo `contatos.csv`.\n"
        "2. **Listar todos os contatos**: Exibir todos os registros presentes no arquivo.\n"
        "3. **Buscar contato por nome**: Permitir que o usuário digite um nome e exibir os dados correspondentes.\n"
        "4. **Remover contato**: Solicitar o nome e excluir o registro correspondente do arquivo.\n"
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

        match resposta:
            case 1:
                adicionar_contato()
            case 2:
                listar_contatos()
            case 3:
                buscar_contato()
            case 4:
                remover_contato()

if __name__ == "__main__":
    main()
    