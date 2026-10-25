# Faça um programa que receba por um usuário (entrada de dados) a medida de um ângulo em graus. 
# Calcule e mostre o quadrante em que se localiza esse ângulo.
# Considere os quadrantes da trigonometria e para ângulos maiores que 360o ou menores que -360o  , reduzi-los, mostrando também o número de voltas e o sentido da volta (horário ou anti-horário).

angulo = int(input('\nDigite a medida do ângulo: '))

if angulo >= 0:
    voltas = angulo / 360
    quadrante = ((angulo % 360) / 90) + 1
    print('\nSENTIDO ANTI-HORÁRIO')  
    print(f'\nQUADRANTE {quadrante:.0f}')
    print(f'\nNúmero de voltas: {voltas:.0f}')
else:
    voltas = abs(angulo) / 360
    quadrante = ((abs(angulo) % 360) / 90) + 1
    print('\nSENTIDO HORÁRIO')  
    print(f'\nQUADRANTE {quadrante:.0f}')
    print(f'\nNúmero de voltas: {voltas:.0f}')


