import random
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
opc = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.randint(0, 2)
usuario = int(input('Qual sua jogada?'))

if usuario != 0 and usuario != 1 and usuario != 2: # validação de entrada
    print('\033[1;34mESCOLHA INVÁLIDA!\033[m')
else:
    print('\033[34m-=\033[m' * 9)
    print('Computador: {}'.format(opc[pc]))
    print('Você: {}'.format(opc[usuario]))
    print('\033[34m-=\033[m' * 9)

    if usuario == pc: #Jogadas iguais
        print('\033[1;33mEMPATE!\033[m')
    elif pc == 0: # Computador jogou PEDRA
        if usuario == 1: # Usuario jogou PAPEL
            print('\033[1;32mVOCE GANHOU!\033[m')
        elif usuario == 2: # Usuario jogou TESOURA
            print('\033[1;31mVOCE PERDEU!\033[m')
    elif pc == 1: # Computador jogou PAPEL
        if usuario == 0: # Usuario jogou PEDRA
            print('\033[1;31mVOCE PERDEU!\033[m')
        elif usuario == 2: # Usuario jogou TESOURA
            print('\033[1;32mVOCE GANHOU!\033[m')
    elif pc == 2: # Computador jogou TESOURA
        if usuario == 0: # Usuario jogou PEDRA
            print('\033[1;32mVOCE GANHOU!\033[m')
        elif usuario == 1: # Usuario jogou PAPEL
            print('\033[1;31mVOCE PERDEU!\033[m')


'''import random
usuario = str(input('Pedra, Papel ou Tesoura?')).upper()
pc = random.randint(0, 2)
opc = ['PEDRA', 'PAPEL', 'TESOURA']
print('COMPUTADOR: {}'.format(opc[pc]))

if usuario == opc[pc]:
    print('\n\033[1;33mEMPATE!\033[m')
elif usuario == 'PEDRA':
    if pc == 1:
        print('\n\033[1;31mVOCE PERDEU!\033[m')
    elif pc == 2:
        print('\n\033[1;32mVOCE GANHOU!\033[m')
elif usuario == 'PAPEL':
    if pc == 0:
        print('\n\033[1;32mVOCE GANHOU!\033[m')
    elif pc == 2:
        print('\n\033[1;31mVOCE PERDEU!\033[m')
elif usuario == 'TESOURA':
    if pc == 0:
        print('\n\033[1;31mVOCE PERDEU!\033[m')
    elif pc == 1:
        print('\n\033[1;32mVOCE GANHOU!\033[m')
else:
    print('\n\033[1;34mESCOLHA INVALIDA!')'''