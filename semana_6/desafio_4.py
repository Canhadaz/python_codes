import uuid
import os

ARQUIVO = "chamados.txt"

def gerar_id():
    return str(uuid.uuid4())

def cadastrar_chamado():
    try:
        with open(ARQUIVO, "a", encoding="utf-8") as arq:

            identificador = gerar_id()
            nome = input("DIGITE SEU NOME:\n--> ").lower().strip()
            categoria = input("DESCRIÇÃO DO PROBLEMA:\n--> ").lower().strip()
            preco = input("DIGITE O NÍVEL DE PRIORIDADE:\n--> ").lower().strip()
            status = "aberto"

            chamado = [identificador, nome, categoria, preco, status]
            linha = "|".join(chamado)

            arq.write(f"{linha}\n")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:    
        print("NÃO FOI POSSÍVEL LER O ARQUIVO!")

def main():

    while True:
        print("ESCOLHA UMA DAS OPÇÕES ABAIXO:\n"
            "1 - Cadastrar chamado"
            "2 - Listar todos os chamados\n"
            "3 - Buscar chamado por ID\n"
            "4 - Buscar chamados por solicitante\n"
            "5 - Atualizar status do chamado\n"
            "6 - Atualizar prioridade do chamado\n"
            "7 - Remover chamado\n"
            "8 - Listar chamados pendentes\n"
            "9 - Exibir estatísticas\n"
            "10 - Sair\n")

        while True:
            try:
                res = int(input("--> "))

                if 1 > res or res > 10:
                    raise ValueError  

                break
            except ValueError:
                print("DIGITE UM VALOR NUMÉRICO VÁLIDO DENTRE (1 - 10)!")

        match res:
            case 1:
                cadastrar_chamado()
            case 10:
                exit() 


if __name__ == "__main__":
    main()