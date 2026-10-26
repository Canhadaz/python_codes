nomes = []
notas = []

print('Digite 7 nomes:\n')
for i in range(7):
    nome = input(f'Digite o {i+1}º nome:\n--> ')
    nomes.append(nome)
    nota = float(input(f'Digite a nota de {nome}:\n--> '))
    notas.append(nota)

    for j in range(i):
        if notas[i] < notas[i - 1]:
            notas[i], notas[i - 1] = notas[i - 1], notas[i]
            nomes[i], nomes[i - 1] = nomes[i - 1], nomes[i]

print()
for i in range(len(nomes)):
    if notas[i] < 7:
        print(f'Aluno: {nomes[i]}, não está aprovado, precisa de {7 - notas[i]} pontos para aprovação.')

print(f'\n{nomes[6]}, possui a maior nota --> {notas[6]}')