from random import randint
from time import sleep
palpites = list()
jogo = []
print('{:-^40}'.format(' MEGA SENA '))
usuario = int(input('Digite quantos jogos deseja sortear: '))
for i in range(0, usuario):
    for c in range(0, 6):
        x = randint(1, 60)
        while x in jogo:
            x = randint(1, 60)
        jogo.append(x)
    jogo.sort()
    palpites.append(jogo[:])
    jogo.clear()
print('-' * 40)
print('\033[34mGERANDO JOGOS...\033[m')
sleep(2)
for c, i in enumerate(palpites):
    print(f'jogo {c + 1}: {i}')
    sleep(1)
print('\033[32m{:-^40}\033[m'.format(' BOA SORTE! '))
