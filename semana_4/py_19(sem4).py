import random

precos = []
for i in range(10):
    preco = round(random.uniform(5, 200), 2)
    precos.append(preco)

estoque = []
for i in range(5):
    linha = []
    for j in range(10):
        qtd = random.randint(0, 100)
        linha.append(qtd)
    estoque.append(linha)

print("Preços dos produtos:")
for j in range(10):
    print(f"Produto {j + 1}: R$ {precos[j]:.2f}")

print("\nEstoque (linhas = armazéns, colunas = produtos):")
for i in range(5):
    print(f"Armazém {i + 1}: {estoque[i]}")

print("\nQuantidade de produtos em cada armazém:")
for i in range(5):
    total_armazem = 0
    for j in range(10):
        total_armazem += estoque[i][j]
    print(f"Armazém {i + 1}: {total_armazem} unidades")

print("\nQuantidade de cada produto em todos os armazéns:")
for j in range(10):
    total_produto = 0
    for i in range(5):
        total_produto += estoque[i][j]
    print(f"Produto {j + 1}: {total_produto} unidades")

maior = estoque[0][0]
coluna_maior = 0
menor = estoque[0][0]

for i in range(5):
    for j in range(10):
        if estoque[i][j] > maior:
            maior = estoque[i][j]
            coluna_maior = j
        if estoque[i][j] < menor:
            menor = estoque[i][j]

print(f"\nProduto com maior estoque em um único armazém: produto {coluna_maior + 1} "
      f"({maior} unidades), preço R$ {precos[coluna_maior]:.2f}")
print(f"Menor estoque armazenado: {menor} unidades")

print("\nCusto de cada armazém:")
for i in range(5):
    custo = 0
    for j in range(10):
        custo += estoque[i][j] * precos[j]
    print(f"Armazém {i + 1}: R$ {custo:.2f}")