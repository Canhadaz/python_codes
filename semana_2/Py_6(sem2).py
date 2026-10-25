salario = int(input('Digite o salário do funcionário: '))

print('\nO salário do funcionário reajustado é: ' + str((salario + (salario * 30 / 100)))) if salario <= 500 else print('\nVocê não tem direito ao reajuste.')
