import csv
import os

ARQUIVO = "alunos.csv"
COLUNAS = ["matricula", "nome", "curso", "idade"]

def cadastrar_aluno():
    
    while True:
        try:
            matricula = int(input("Digite a matricula do aluno: "))
            nome      = input("Digite o nome do aluno: ").lower().strip()
            curso     = input("Digite o curso do aluno: ").lower().strip()
            idade     = int(input("Digite a idade do aluno: "))

            if not matricula or not nome or not curso or not idade:
                raise ValueError
            
            break
        except ValueError:
            print("TODAS OS ELEMENTOS DEVEM SER PREENCHIDOS!")

    arquivo_vazio = os.path.exists(ARQUIVO) == 0
    with open(ARQUIVO, "a", newline="", encoding="utf-8") as arq:
        escritor = csv.DictWriter(arq, fieldnames=COLUNAS)

        if arquivo_vazio:
            escritor.writeheader()

        escritor.writerow({
            "matricula": matricula,
            "nome": nome,
            "curso": curso,
            "idade": idade 
        })
        print("ALUNO ADICIONADO COM SUCESSO!")

def listar_alunos():

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)

            print("\tLISTA DE ALUNOS:\n")

            for aluno in leitor:
                print(f"Matricula: {aluno["matricula"]}")
                print(f"Nome     : {aluno["nome"]}")
                print(f"Curso    : {aluno["curso"]}")
                print(f"Idade    : {aluno["idade"]}")
                print("-" * 30)

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:
        print("NÃO FOI POSSIVEL LER O ARQUIVO!")

def buscar_matricula():
    
    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)

            res = int(input("DIGITE A MATRICULA DO ALUNO:\n--> "))

            for aluno in leitor:
                if str(res) in aluno["matricula"]:
                    print(f"\nMatricula: {aluno["matricula"]}")
                    print(f"Nome     : {aluno["nome"]}")
                    print(f"Curso    : {aluno["curso"]}")
                    print(f"Idade    : {aluno["idade"]}")
                    print("-" * 30)

                    return aluno["matricula"]
            else:
                print("ALUNO NÃO ENCONTRADO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:
        print("NÃO FOI POSSIVEL LER O ARQUIVO!")

def buscar_curso():
    encontrado = False
    
    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            leitor = csv.DictReader(arq)

            res = input("DIGITE A CURSO DO ALUNO:\n--> ").lower().strip()

            for aluno in leitor:
                if str(res) in aluno["curso"]:
                    print(f"\nMatricula: {aluno["matricula"]}")
                    print(f"Nome     : {aluno["nome"]}")
                    print(f"Curso    : {aluno["curso"]}")
                    print(f"Idade    : {aluno["idade"]}")
                    print("-" * 30)

                    encontrado = True
            if encontrado == False:
                print("ALUNO NÃO ENCONTRADO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:
        print("NÃO FOI POSSIVEL LER O ARQUIVO!")

def atualizar_dados():

    matricula = buscar_matricula()

    while True:
        try:
            nome      = input("Digite o nome do aluno: ").lower().strip()
            curso     = input("Digite o curso do aluno: ").lower().strip()
            idade     = int(input("Digite a idade do aluno: "))

            if not nome or not curso or not idade:
                raise ValueError
            
            break
        except ValueError:
            print("TODAS OS ELEMENTOS DEVEM SER PREENCHIDOS!")

    arquivo_vazio = os.path.exists(ARQUIVO) == 0
    
    try:
        if arquivo_vazio:
            raise FileNotFoundError
        
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            alunos = list(csv.DictReader(arq))

            for aluno in alunos:
                if matricula in aluno["matricula"]:
                    aluno["nome"]  = nome
                    aluno["curso"] = curso
                    aluno["idade"] = idade

        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.DictWriter(arq, fieldnames=COLUNAS)

            escritor.writeheader()
            escritor.writerows(alunos)

            print("ATUALIZADO COM SUCESSO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:
        print("NÃO FOI POSSIVEL LER O ARQUIVO!")

def remover_aluno():

    arquivo_vazio = os.path.exists(ARQUIVO) == 0
    matricula = buscar_matricula()
    restantes = []
    
    try:
        if arquivo_vazio:
            raise FileNotFoundError
        
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arq:
            alunos = list(csv.DictReader(arq))

            for aluno in alunos:
                if matricula not in aluno["matricula"]:
                    restantes.append(aluno)

        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.DictWriter(arq, fieldnames=COLUNAS)

            escritor.writeheader()
            escritor.writerows(restantes)

            print("REMOVIDO COM SUCESSO!")

    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO!")
    except OSError:
        print("NÃO FOI POSSIVEL LER O ARQUIVO!")

def main():
    print("ESCOLHA UMA DAS OPÇÕES ABAIXO:\n"
    "1 - Cadastrar aluno\n"
    "2 - Listar alunos\n"
    "3 - Buscar aluno por matrícula\n"
    "4 - Buscar alunos por curso\n"
    "5 - Atualizar dados do aluno\n"
    "6 - Remover aluno\n"
    "7 - Sair")

    while True:
        try:
            res = int(input("--> "))

            if 1> res or res > 7:
                raise ValueError
            
            break
        except ValueError:  
            print("DIGITE UM VALOR VÁLIDO!")

    if res == 7:
        exit()

    match res:
        case 1:
            cadastrar_aluno()
        case 2:
            listar_alunos()
        case 3:
            buscar_matricula()
        case 4:
            buscar_curso()
        case 5:
            atualizar_dados()
        case 6:
            remover_aluno()


if __name__ == "__main__":  
    main()