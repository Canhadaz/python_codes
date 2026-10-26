# Faça um programa que carrregue um vetor com 15 elementos numéricos inteiros e verifique a existência de elemetos iguais a 30, mostrando as posições em que esses elementos aparecem no vetor.

# Observações:
# Pode usar o comando append() para adicionar os valores no vetor. 
# # Os elementos do vetor devem ser acessados através do seus respectivos índices.

import random
vetor = []
for i in range(15):
    num = random.randint(25,35)
    vetor.append(num)
    if vetor[i] == 30:
        print(i, end = ', ')
print(vetor)