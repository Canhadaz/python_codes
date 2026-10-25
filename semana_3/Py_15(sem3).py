# Com base na teoria descrita no material em anexo, referente a conversões numéricas mais utilizadas na computação.

# Faça um algoritmo que receba como entrada de dados um valor decimal  e a opção de conversão. Ao final o programa deverá mostrar o decimal convertido pra base escolhida pelo usuário.

# Opções: 

# 1- Decimal para Binário
# 2 - Decimal para Octal
# 3 - Decimal para Hexadecimal

import random

decimal = random.randint(1, 1000)

print(f'DECIMAL --> {decimal}')

i = 1
while i < decimal:
    i += 1

print('\n' + str(i))
print(f'\n{binario}')