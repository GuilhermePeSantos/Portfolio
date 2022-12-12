from random import randint
from time import sleep
comput = randint(0, 10)
vitorias = 0
jogador = ' '
while True:
    while jogador not in 'PpIi':
        jogador = str(input('Par ou Ímpar? [P/I]: ')).strip()[0]
    num = int(input('Digite um valor: '))

    if jogador in 'Pp':
        print(f'VOCÊ jogou {num} | PAR ')
        print(f'COMPUTADOR jogou {comput} | ÍMPAR')
    else:
        print(f'VOCÊ jogou {num} | ÍMPAR ')
        print(f'COMPUTADOR jogou {comput} | PAR')
    soma = num + comput
    print('\n\033[34mCALCULANDO...\033[m')
    sleep(1)
    if soma % 2 == 0:
        print(f'Resultado: {soma} -> PAR')
        if jogador in 'Pp':
            print('Você \033[32mVENCEU\033[m, Parabéns! Jogue novamente')
            vitorias += 1
        else:
            break
    if soma % 2 == 1:
        print(f'Resultado: {soma} -> ÍMPAR')
        if jogador in 'Ii':
            print('Voce \033[32mVENCEU\033[m, Parabéns! Jogue novamente')
            vitorias += 1
        else:
            break
    print('-' * 35)
print('=' * 30)
print(f'\nVocê \033[31mPERDEU\033[m, após {vitorias} vitorias')