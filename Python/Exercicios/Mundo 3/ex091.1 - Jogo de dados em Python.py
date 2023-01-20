from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('---- JOGADAS ----')
for k, v in jogo.items():
        sleep(1)
        print(f'{k} jogou {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'\n{" RANK ":-^17}')
for i, v in enumerate(ranking):
        print(f'{i + 1}° lugar = {v[0]} com {v[1]}')
        sleep(1)
