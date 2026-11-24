ARQUIVO = "tarefas.txt"

def adicionar_tarefa():
    tarefa = input("Informe qual a tarefa a ser adicionada:\n--> ").strip()

    try:
        with open(ARQUIVO, "a", encoding="utf-8") as arq:
            arq.write(f"\n{tarefa}")

        print("TAREFA ADICIONADA COM SUCESSO!")
        
    except OSError:
        print("NÃO FOI POSSIVEL ADICIONAR TAREFA!")
        return None

def listar_tarefas():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            print(arq.read())

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
        return None
    except OSError:
        print("NÃO FOI POSSIVEL LER TAREFA!")
        return None   

def buscar_tarefa():
    tarefa = input("Informe a tarefa para busca:\n--> ").strip().lower()

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            for linha in arq:
                if tarefa in linha.lower():
                    print("TAREFA JÁ PRESENTE NO DOCUMENTO!")
                    break
            else:
                print("NÃO ENCONTRADO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
        return None
    except OSError:
        print("NÃO FOI POSSIVEL LER TAREFA!")
        return None   

def remover_tarefa():
    remover = input("Informe a tarefa para remoção:\n--> ").strip().lower()
    restantes = []

    try:    
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            for linha in arq:
                if remover not in linha.lower():
                    restantes.append(linha)

        if not restantes:
            print("DIGITE UMA TAREFA!")
            return 

        with open(ARQUIVO, "w", encoding="utf-8") as arq:
            arq.writelines(restantes)
            print("REMOVIDO COM SUCESSO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
        return None
    except OSError:
        print("NÃO FOI POSSIVEL LER TAREFA!")
        return None

def limpar_tarefas():
    try:    
        with open(ARQUIVO, "w", encoding="utf-8") as arq:
            arq.write("")
            print("REMOVIDO COM SUCESSO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
        return None
    except OSError:
        print("NÃO FOI POSSIVEL LER TAREFA!")
        return None


def main():
    print("ESCOLHA UMA DAS OPÇÕES ABAIXO:\n"
    "1 - Adicionar tarefa\n"
    "2 - Listar tarefas\n"
    "3 - Buscar tarefa\n"
    "4 - Remover tarefa\n"
    "5 - Limpar todas as tarefas\n"
    "6 - Sair\n")

    while True:
        try:
            res = int(input("--> "))

            if 1 > res or res > 6:
                raise ValueError

            break

        except ValueError:
            print("DIGITE UM VALOR VÁLIDO DE (1 - 6)!")

    if res == 6:
        exit()

    match res:
        case 1:
            adicionar_tarefa()
        case 2:
            listar_tarefas()
        case 3:
            buscar_tarefa()
        case 4:
            remover_tarefa()
        case 5:
            limpar_tarefas()

if __name__ == "__main__":
    main()