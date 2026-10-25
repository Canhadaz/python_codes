# Simulador de Controle de Tráfego Aéreo
# Você foi contratado para desenvolver um simulador simples de controle de tráfego aéreo para treinar novos operadores.
# O sistema deve permitir que o usuário controle o status de um avião por meio de comandos digitados no terminal.
# Objetivo:
# Criar um programa em Python que simule ações básicas de um avião, utilizando a estrutura match-case para interpretar os comandos do usuário.
# Requisitos:

# O programa deve iniciar com o avião em solo e altitude 0.
# O usuário poderá digitar os seguintes comandos:
# "decolar": muda o status para em voo e define a altitude inicial como 1000 metros.
# "subir": aumenta a altitude em 500 metros.
# "descer": diminui a altitude em 500 metros, sem permitir valores negativos.
# "aterrissar": muda o status para em solo e zera a altitude.
# "status": exibe o status atual e a altitude.
# "sair": encerra o programa.
# Qualquer comando diferente deve gerar uma mensagem de erro: "Comando não reconhecido."
# Restrições:

# Não utilizar listas, tuplas, dicionários ou qualquer estrutura de coleção.
# O controle deve ser feito apenas com variáveis simples e match-case.

altitude = 0
status = "em solo"

print("\nCOMANDOS DISPONÍVEIS:")
print("decolar: muda o status para em voo e define a altitude em 1000 metros.")
print("subir: aumenta a altitude em 500 metros.")
print("descer: diminui a altitude em 500 metros, sem valores negativos.")
print("aterrissar: muda o status para em solo e zera a altitude.")
print("status: exibe o status atual e a altitude.")
print("sair: encerra o programa.")

while True:
    match input("\nDigite um comando: ").lower():
        case "decolar":
            status = "em voo"
            altitude = 1000
            print(f'status {status}, altitude {altitude} metros.')
        case "subir":
            if status == "em voo":
                altitude += 500
                print(f'status {status}, altitude {altitude} metros.')
            else:
                print("Erro: O avião precisa estar em voo para subir.")
        case "descer":
            if status == "em voo":
                altitude -= 500
                if altitude < 0:
                    altitude = 0
                print(f'status {status}, altitude {altitude} metros.')
            else:
                print("Erro: O avião precisa estar em voo para descer.")    
        case "aterrissar":
            if status == "em voo":
                status = "em solo"
                altitude = 0
                print(f'status {status}, altitude {altitude} metros.')
            else:
                print("Erro: O avião já está em solo.")
        case "status":
            print(f'status {status}, altitude {altitude} metros.')
        case "sair":    
            print("Encerrando o programa.")
            exit()
        case _:
            print("Digite um comando valído.")
