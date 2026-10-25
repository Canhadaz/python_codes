# Crie um programa em Python que simule um sistema de concessão de crédito bancário, usando apenas estruturas de seleção (if/elif/else).

# O programa deve receber três informações do usuário:

# Idade
# Salário mensal
# Número de dependentes
# Com base nesses dados, o programa deve decidir se o crédito é Aprovado, Parcialmente aprovado ou Negado, seguindo as regras:

# Regras de Aprovação

# Negado se:
# Idade < 18 anos, ou
# Salário < R$ 1.500,00, ou
# Mais de 5 dependentes.
# Parcialmente aprovado se:
# Idade entre 18 e 25 anos e salário entre R$ 1.500,00 e R$ 3.000,00, ou
# Idade acima de 25 anos com até 3 dependentes e salário entre R$ 1.500,00 e R$ 2.500,00.
# Aprovado se:
# Idade acima de 25 anos, salário maior que R$ 3.000,00, e até 3 dependentes.
# Além disso, o programa deve mostrar uma mensagem extra:

# Se aprovado, mostrar "Crédito liberado com sucesso!".
# Se parcialmente aprovado, mostrar "Crédito limitado: análise adicional necessária.".
# Se negado, mostrar "Crédito negado: requisitos não atendidos.".

idade = int(input("\nDigite sua idade: "))
salario = float(input("Digite seu salário mensal: "))
dependentes = int(input("Digite o número de dependentes: "))

if idade < 18 or salario < 1500 or dependentes > 5:
    print("Crédito negado: requisitos não atendidos.")
elif 18 <= idade <= 25 and 1500 <= salario <= 3000:
    print("Crédito limitado: análise adicional necessária.")
elif idade > 25 and dependentes <= 3 and 1500 <= salario <= 2500:
    print("Crédito limitado: análise adicional necessária.")
elif idade > 25 and salario > 3000 and dependentes <= 3:
    print("Crédito liberado com sucesso!")
