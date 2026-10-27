def conversor(hora, min, seg):
    print(f'\nTEMPO TOTAL: {hora}h, {min}min, {seg}seg')
    print(f'TEMPO TOTAL EM SEGUNDOS: {(hora * 3600) + (min * 60) + seg}seg')

def main():

    hora = int(input('Digite a hora:\n--> '))
    min = int(input('Digite os minutos:\n--> '))
    seg = int(input('Digite os segundos:\n--> '))

    conversor(hora, min, seg)
    
main()