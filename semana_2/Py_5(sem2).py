# Faça um programa que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário. 

# Escolha do Usuário                                                              Operação
# -----------------------------------------------------------------------------------------------------------

# 1                                                                                           Média entre os números digitados

# 2                                                                                           Diferença do maior pelo menor

# 3                                                                                           Produto entre os números digitados

# 4                                                                                           Divisão do primeiro pelo segundo

# Se a opção digitada for inválida, mostrar uma mensagem de erro e terminar a execução do programa. Lembre-se de que na operação 4 o segundo número deve ser diferente de zero.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('\nEscolha uma das opções abaixo: ')
print('\n1º : Média entre os números digitados')
print('\n2º : Diferença do maior pelo menor')
print('\n3º : Produto entre os números digitados')
print('\n4º : Divisão do primeiro pelo segundo')

opcao = int(input('\nDigite a opção desejada: '))

if opcao == 1:
    print('A média dos números é: ' + str((n1 + n2) / 2))
elif opcao == 2:
    if n1 > n2:
        print('A diferença do maior pelo menor é: ' + str(n1 - n2))
    else:
        print('A diferença do maior pelo menor é: ' + str(n2 - n1))
elif opcao == 3:
    print('O produto dos números é: ' + str(n1 * n2))
elif opcao == 4:
    if n2 <= 0:
        print('O segundo número não pode ser igual ou menor que zero para a divisão.')
    else:
        print('A divisão do primeiro pelo segundo é: ' + str(n1 / n2))
else:
    print('Opção inexistente.')