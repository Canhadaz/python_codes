# Faça um programa que receba dois números, 
# calcule e mostre a divisão do primeiro número pelo segundo número. 
# Sabe-se que o segundo número não pode ser zero, portanto não é necessário se preocupar com validações.

# Sugestões:
# Variáveis de entrada de dados: N1 e N2
# Variável calculada:  R = N1 / N2 (onde N2 não pode ser zero)
# Informar o usuário que a variável N2 não pode ser zero.

num1 = int(input(''))
num2 = int(input(''))

zero = (num2 == 0)

print(str(num1 / num2) * (not zero))
