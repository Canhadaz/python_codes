import random

nomes = [
    "Maria", "Nicolas", "Marcelo", "Pedro", "Lucas",
    "Laura", "Fabricio", "Victor", "Natan", "Matheus",
    "Luisa", "Danilo", "Felipe", "Gabriel", "Murilo"
]

tabela = [[0 for i in range(5)] for n in range(16)]
materias = ['MATÉRIAS: ','matemática', 'geografia', 'história', 'português', 'inglês']

contador_linha = 0
contador_coluna = 0

for n in range(15):
    contador_linha += 1
    for i in range(5):
        contador_coluna += 1
        nota = random.uniform(0.0, 10.0)
        tabela[contador_linha][i] = nota
    contador_coluna = 0

for n in range(6):
    print(f'{materias[n]}', end = '         ') 

print('\n')

for n in range(15): 
    print(f'{nomes[n]:<10}', end ='  --> ' )
    for i in range(5):
        print(f'{tabela[n + 1][i]:.2f}', end='')
        if tabela[n + 1][i] > 6:
            print('\033[32m| APROVADO  |\033[0m', end = '')
        elif tabela[n + 1][i] > 4:
            print('\033[33m| EXAME     |\033[0m', end = "")
        else:
            print('\033[31m| REPROVADO |\033[0m', end = "")
    print('')