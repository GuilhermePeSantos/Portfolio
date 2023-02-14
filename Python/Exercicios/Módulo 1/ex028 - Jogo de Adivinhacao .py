from random import randint
from time import sleep #A função sleep deixa um delay no computador
a = randint(0, 5)
n = int(input('Digite um número:'))
print('PROCESSANDO...')
sleep(3)
if n == a:
    print('VOCE ACERTOU!!!')
else:
    print('TENTE NOVAMENTE!!!')
    print('\nO numero sorteado foi {}'.format(a))

