# Entrada de dados

# O atendente insere o nome do aluno e carrega os documentos exigidos: RG, CPF, comprovante de matrícula, histórico escolar e currículo.
# Processamento sequencial

# O sistema verifica cada documento em ordem:
# RG → válido?
# CPF → válido?
# Comprovante de matrícula → atualizado?
# Histórico escolar → dentro do prazo?
# Currículo → presente?
# Estrutura de seleção (decisões)

# Para cada documento:
# Se válido → prossegue para o próximo.
# Se inválido ou ausente → gera mensagem de erro e interrompe o processo.
# Tomada de decisão final

# Se todos os documentos estão corretos → aprovar candidato e gerar protocolo de estágio.
# Se algum documento está incorreto → rejeitar candidatura e emitir relatório de pendências.
# Saída

# Mensagem para o atendente:
# “Candidato aprovado para estágio”
# ou “Documentação incompleta – verificar pendências”.

RG = 250729751
CPF = 55704689000

nome = input('Digite o nome do candidato: ')
rg = int(input('Digite o RG do candidato (sem caracteres de formatação): '))
cpf = int(input('Digite o CPF do candidato (sem caracteres de formatação): '))
comprovante_matricula = input('O comprovante de matrícula do candidato está atualizado? (S/N): ')
he_prazo = input('O histórico escolar do candidato está dentro do prazo de validade? (S/N): ')
curriculo = input('O currículo do candidato está presente? (S/N): ')

# fiquei com preguiça de adicionar a condição de verificar se o usuario digitou uma frase com mais de uma letra.
# não poder usar função faz esse código ficar bizarramente feio.

if comprovante_matricula != 'S' and comprovante_matricula == 's' and comprovante_matricula != 'N' and comprovante_matricula != 'n':
    print('\nResposta inválida.')
    exit()

if he_prazo != 'S' and he_prazo == 's' and he_prazo != 'N' and he_prazo != 'n':
    print('\nResposta inválida.')
    exit()

if curriculo != 'S' and curriculo == 's' and curriculo != 'N' and curriculo != 'n':
    print('\nResposta inválida.')
    exit()

val = True
cur = True

# exibição de status

if rg == RG:
    print('RG: Válido')
else:
    val = False
    print('RG: Inválido')
 
if cpf == CPF:
    print('CPF: Válido')
else:
    val = False
    print('CPF: Inválido')
 
if comprovante_matricula == 'S' or comprovante_matricula == 's':
    print('Comprovante de matrícula: Válido')
else:
    val = False
    print('Comprovante de matrícula: Inválido')
 
if he_prazo == 'S' or he_prazo == 's':
    print('Histórico escolar: Válido')
else:
    val = False
    print('Histórico escolar: Inválido')

if curriculo == 'S' or curriculo == 's':
    print('Currículo: Válido')
else:
    cur = False
    print('Currículo: Inválido')

# resultado final

if val == True and cur == True:
    print(f'\nTodos os documentos do candidato [ {nome} ] estão válidos.\nCandidato aprovado para estágio.')
elif val == True and cur == False:
    print(f'\nTodos os documentos do candidato [ {nome} ] estão válidos, exceto o currículo.\nCandidato aprovado para estágio, mas deve checar as pendências.')
elif val == False and cur == True:
    print(f'\nAlguns documentos do candidato [ {nome} ] estão inválidos, mas o currículo está válido.\nCandidato reprovado para estágio.')
else:
    print(f'\nTodos os documentos do candidato [ {nome} ], incluindo o currículo, estão inválidos.\nCandidato reprovado para estágio.')
