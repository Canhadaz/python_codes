# Faça um programa que verifique a validade de uma senha fornecida pelo usuário. a senha é "A4533BC". O programa deve mostrar uma mensagem de permissão de acesso ou não.

SENHA = "A4533BC"

sen = input('\nDigite a senha: ')

if sen == SENHA:
    print("\nTA LIBERADO CHEFE!")
else:
    print('\nPode não.')