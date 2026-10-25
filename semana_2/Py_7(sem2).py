n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('\nEscolha uma das opções abaixo: ')
print('\n1º : Média entre os números digitados')
print('\n2º : Diferença do maior pelo menor')
print('\n3º : Produto entre os números digitados')

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
else:
    print('Opção inexistente.')