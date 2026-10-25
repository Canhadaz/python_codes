# O cálculo dos dois dígitos verificadores do CPF (os números após o traço) baseia-se nos primeiros 9 dígitos utilizando um algoritmo de módulo 11.

# O processo é dividido em duas etapas.
# Aqui está o passo a passo:
# Exemplo Base: 123.456.789 - D
# 1. Cálculo do Primeiro Dígito (D1)
# 1.     Multiplicação: Multiplique os 9 primeiros dígitos pela seqüência decrescente de 10 a 2.
# 2.     Soma: Some todos os resultados.
# 3.     Resto da Divisão: Pegue a soma total e calcule o resto da divisão por 11 (Soma % 11).
# 4.     Verificação:
# ·         Se o resto for menor que 2, D1 = 0.
# ·         Se o resto for 2 ou mais, D1 = 11 - Resto. 
# 2. Cálculo do Segundo Dígito (D2)
# 1.     Multiplicação: Utilize os 9 primeiros dígitos + o 1º dígito calculado (D1), multiplicando-os pela sequência decrescente de 11 a 2.
# 2.     Soma: Some todos os resultados.
# 3.     Resto da Divisão: Pegue a soma total e calcule o resto da divisão por 11 (Soma % 11).
# 4.     Verificação:
# ·         Se o resto for menor que 2, D2 = 0.
# ·         Se o resto for 2 ou mais, D2 = 11 - Resto. 
# Mostrar uma mensagem ao final: “CPF válido”  ou “CPF inválido”
#
# Não pode usar String, Listas, Tuplas, dicionário.
# Não pode usar o comando de seleção IF.
# Deve usar apenas os conectivos lógicos e os operadores relacionais para resolver o problema.
# Pode usar o comando de entrada input() e de saída print().
# Sugestão, usar uma variável para cada número.

print('\nDigite o CPF (sem os caracteres de formatação "." e "-").')

num1 = int(input(''))
num2 = int(input(''))
num3 = int(input(''))
num4 = int(input(''))
num5 = int(input(''))
num6 = int(input(''))
num7 = int(input(''))
num8 = int(input(''))
num9 = int(input(''))
d1_usuario = int(input(''))
d2_usuario = int(input(''))

soma1 = ((num1 * 10) + (num2 * 9) +(num3 * 8) +(num4 * 7) +(num5 * 6) +(num6 * 5) +(num7 * 4) +(num8 * 3) +(num9 * 2)) % 11

d1_0 = (soma1 < 2)
d1_11 = (soma1 >= 2)

d1 = (d1_0 * 0) + (d1_11 * (11 - soma1))

#torturante isso aq
soma2 = ((num1 * 11) + (num2 * 10) +(num3 * 9) +(num4 * 8) +(num5 * 7) +(num6 * 6) +(num7 * 5) +(num8 * 4) +(num9 * 3) + (d1 * 2)) % 11

d2_0 = (soma2 < 2)
d2_11 = (soma2 >= 2)

d2 = (d2_0 * 0) + (d2_11 * (11 - soma2))

print("CPF invalído." * (d1 != d1_usuario or d2 != d2_usuario) +
      "CPF válido." * (d1 == d1_usuario and d2 == d2_usuario))



