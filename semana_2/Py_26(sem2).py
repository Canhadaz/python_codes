# Exercício: Sistema de Classificação para Concurso Público
# Um concurso possui três fases:

# Prova Objetiva (0 a 100)
# Prova Discursiva (0 a 100)
# Teste Físico (Apto/Inapto)
# O programa deve solicitar ao candidato:

# Nota da prova objetiva
# Nota da prova discursiva
# Resultado do teste físico (A para apto e I para inapto)
# Regras
# Primeira etapa: Prova Objetiva
# Se a nota objetiva for menor que 60:

# Candidato ELIMINADO.
# Caso contrário:

# Prossegue para análise da discursiva.
# Segunda etapa: Prova Discursiva
# Se a nota discursiva for menor que 50:

# Candidato ELIMINADO.
# Caso contrário:

# Prossegue para o teste físico.
# Terceira etapa: Teste Físico
# Se for inapto:

# Candidato ELIMINADO.
# Se for apto:

# Calcular a média das duas provas.
# Classificação Final
# Dentro da condição de aprovado no físico:

# Média ≥ 90

# Classificação: APROVADO EM 1ª CHAMADA
# Média entre 80 e 89,99

# Se a nota objetiva ≥ 85:
# APROVADO EM 1ª CHAMADA
# Senão:
# CADASTRO DE RESERVA
# Média entre 70 e 79,99

# Se a nota discursiva ≥ 75:
# CADASTRO DE RESERVA
# Senão:
# LISTA DE ESPERA
# Média abaixo de 70

# REPROVADO
 
# DFD (Diagrama de Fluxo de Dados)
print('-----------------------------------------------')
nota_objetiva = int(input('\nDigite a nota da prova objetiva [0 - 100]: '))
nota_discursiva = int(input('\nDigite a nota da prova discursiva [0 - 100]: '))

#verificação dos valores fornecidos pelo usuário
if nota_objetiva > 100 or nota_objetiva < 0 or nota_discursiva > 100 or nota_discursiva < 0:
    print('\nDIGITE UM VALOR NÚMERO CORRETO PARA AS NOTAS!')
    exit()

nota_fisico = input('\nO candidato foi está apto fisicamente? [A/I]: ')

if nota_fisico != 'i' and nota_fisico != 'I' and nota_fisico != 'A' and nota_fisico != 'a':
    print('\nERRO!\nDIGITE UM VALOR VALÍDO PARA O TESTE FISÍCO!')
    exit()

if len(nota_fisico) > 1:
    print('\nERRO!\nDIGITE UM VALOR VALÍDO PARA O TESTE FISÍCO!')
    exit()

# verificação das etapas.
if nota_objetiva < 60:
    print('\nCANDIDATO ELIMINADO na 1º etapa [prova objetiva]!')
    exit()

if nota_discursiva < 50:
    print('\nCANDIDATO ELIMINADO na 2º etapa [prova discursiva]!')
    exit()

if nota_fisico == 'i' or nota_fisico == 'I':
    print('\nCANDIDATO ELIMINADO na 3º etapa [teste fisíco]!')
    exit()

media_final = (nota_objetiva + nota_discursiva) / 2
print('-----------------------------------------------')
print(f'Média final do candidato: {media_final:.2f}')
print('-----------------------------------------------')

if media_final >= 90:
    print('CANDIDATO APROVADO NA 1º CHAMADA!')
elif media_final >= 80:
    if nota_objetiva >= 85:
        print('CANDIDATO APROVADO NA 1º CHAMADA!')
    else:
        print('STATUS DO CANDIDATO: [CADASTRO DE RESERVA]')
elif media_final >= 70:
    if nota_discursiva >= 75:
        print('STATUS DO CANDIDATO: [CADASTRO DE RESERVA]')
    else:
        print('STATUS DO CANDIDATO: [LISTA DE ESPERA]')
else:
    print('CANDIDATO REPROVADO!')