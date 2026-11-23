with open(r"frases.txt", "r") as arq:
    linhas = arq.readlines()

print(len(linhas))
    
for i in range(len(linhas) -1, -1 , -1):
    if linhas[i] == "" or linhas[i] == '\n':
        del linhas[i]

with open(r"frases.txt", "w") as arq:
    arq.writelines(linhas)

with open(r"frases.txt", "r") as arq:
    print(arq.read())