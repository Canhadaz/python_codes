# Faça um programa que receba o peso de uma pessoa, calcule e mostre:

# o novo peso se a pessoa engordar 15% sobre o peso digitado
# o novo peso se a pessoa emagrecer 20% sobre o peso digitado.

peso = float(input('\nQual o seu peso? '))

print('\nCaso você engorde 15%, seu peso será: ' + str(peso + ((peso / 100) * 15)))
print('\nCaso você engorde 20%, seu peso será: ' + str(peso + ((peso / 100) * 20)) + '\n')
