from random import randint
print('Tente advinhar o número que o computador pensou!')
computador = randint(0, 10)
jogador = int(input('Digite sua tentativa: '))
tentativas = 1
while jogador != computador:
    print('\033[31mERROU!\033[m')
    if jogador > computador:
        print('Um pouco menos...')
    else:
        print('Um pouco mais...')
    jogador = int(input('Digite sua tentativa novamente:'))
    tentativas += 1
print('\n\033[32mVocê Acertou\033[m, com {}° tentativas'.format(tentativas))
