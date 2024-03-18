from time import sleep
calculo = 0
impar = ''
par = ''
lista = ['Impar', 'Par']
jogador = int(input('\n0 - Impar | 1- Par: '))

for i in range(0, 2):
    nome = str(input('Digite seu NOME: '))
    num = int(input('Digite seu numero: '))

    if jogador == 0:
        impar = nome
        if i == 0:
            print('\nProximo jogador: Par')
        jogador = 1
    else:
        par = nome
        if i == 0:
            print('\nProximo jogador: Impar')
        jogador = 0
    calculo += num

print('\n{} jogou \033[33mIMPAR\033[m'.format(impar))
print('{} jogou \033[34mPAR\033[m'.format(par))
print('\n\033[37mCALCULANDO...\033[m')
sleep(2)
print('A soma dos numeros é {}, portanto'.format(calculo), end='')
if calculo % 2 == 0:
    print(' PAR\nO jogador(a) \033[32m{}\033[m GANHOU'.format(par))
else:
    print(' IMPAR\nO jogador(a) \033[32m{}\033[m GANHOU'.format(impar))
