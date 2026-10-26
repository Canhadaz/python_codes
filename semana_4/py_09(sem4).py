# Faça um programa que carregue três vetores com dez posições cada um (valores digitados pelo usuário). 
# O primeiro vetor de dez produto. O segundo vetor com os códigos dos dez produtos e  o terceiro vetor com os preços dos produtos.
# Mostre um relatório APENAS com o nome, o código, o preço e o novo preço dos produtos que sofrerão aumento.
# Sabe-se que os produtos que sofrerão aumento são aqueles que possuem código PAR ou PREÇO SUPERIOR a R$ 1.000,00.
# Sabe-se ainda que se o produto satisfaz as duas condições acima (código e preço), o aumento do preço será de 20%. 
# Se satisfaz apenas a condição de código; o aumento será de 15%; se satisfaz apenas a condição de preço, o aumento será de 10%.


# Observações:
# Pode usar o comando append() para adicionar os valores no vetor. 
# Os elementos do vetor devem ser acessados através do seus respectivos índices.

import random

estoque = ['Smartphone', 'Air Fryer', 'Livro Impresso', 'Tênis Esportivo', 'Cafeteira Elétrica', 'Canudo de Vidro Reutilizável', 'Kit de Ferramentas com Maleta', 'Protetor Solar', 'Conjunto de Pincéis de Maquiagem','Aspirador de Pó']

produtos = []
codigos = []
valores = []

contador = 0
aumento = []

print('\n             PRODUTOS               |   CÓDIGOS   |   VALORES   |   NOVO_VALOR\n')

for i in range(10):
    produto = random.choice(estoque)
    produtos.append(produto)
    
    codigo = i + 100
    codigos.append(codigo)

    valor = random.randint(1,10000)
    valores.append(valor)

    if not codigos[i] % 2 == 0 and not valores[i] > 1000:
        print(f'{i + 1:<2} {produtos[i]:<32} --> {codigos[i]:<9} --> {valores[i]:<9} --> não sofrerá aumento.')
    elif codigos[i] % 2 == 0 or valores[i] > 1000:
        aumento.append(valores[i] + ((valores[i]/100) * 15))
        print(f'{i + 1:<2} {produtos[i]:<32} --> {codigos[i]:<9} --> {valores[i]:<9} --> {aumento[contador]:.2f}')
        contador += 1
    elif codigos[i] % 2 == 0 and valores[i] > 1000:
        aumento.append(valores[i] + ((valores[i]/100) * 20))
        print(f'{i + 1:<2} {produtos[i]:<32} --> {codigos[i]:<9} --> {valores[i]:<9} --> {aumento[contador]:.2f}')
        contador += 1

print()