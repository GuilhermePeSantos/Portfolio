from random import randint
from time import sleep
jogo = list()
jogador = {}
x = 0
print('\033[34;1m{:-^20}\033[m'.format(' JOGADAS '))
for i in range(1, 5):
    jogador['nome'] = f'jogador{i}'
    jogador['jogada'] = randint(1, 6)
    jogo.append(jogador.copy())
    print(f'{jogador["nome"]} jogou {jogador["jogada"]}')
    sleep(1)
    jogador.clear()
jogadas = list()
for i in range(0, 4):
    jogadas.append(jogo[i]['jogada'])
jogadas.sort(reverse=True)
print('\n\033[32;1m{:-^20}\033[m'.format(' RANK '))
for i in range(0, 4):
    while True:
        if jogadas[i] == jogo[x]['jogada']:
            print(f'{i + 1}° - {jogo[x]["nome"]} = {jogo[x]["jogada"]}')
            jogo[x]['jogada'] = -1
            x = 0
            break
        x += 1
