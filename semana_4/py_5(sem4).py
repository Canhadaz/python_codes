vendas = []
comissão = []
nomes = []

total = 0

for i in range(10):
    vendas.append(float(input(f'Informe o valor da venda do vendedor {i + 1}: ')))
    comissão.append(float(input(f'Informe a comissão do vendedor {i + 1}, [0 - 100]% :')))
    nomes.append(input(f'Informe o nome do vendedor {i + 1}: ').upper())

    total += vendas[i] + (vendas[i] * (comissão[i] / 100))

    if vendas[i - 1] < vendas[i]:
        menor = vendas[i - 1]
        vendedor_menor = nomes[i - 1]
    else:
        menor = vendas[i]
        vendedor_menor = nomes[i]

    if vendas[i - 1] > vendas[i]:
        maior = vendas[i - 1]
        vendedor_maior = nomes[i - 1]
    else:
        maior = vendas[i]
        vendedor_maior = nomes[i]

print('\nVENDEDORES:\n')
print('\n'.join(nomes))
print(f'\nTotal dos valores de vendas e comissões --> {total:.2f}')
print(f'\nMenor valor de venda --> {menor:.2f}', end='\n')
print(f'Vendedor com menor valor de venda --> {vendedor_menor}')
print(f'\nMaior valor de venda --> {maior:.2f}', end='\n')
print(f'Vendedor com maior valor de venda --> {vendedor_maior}')
