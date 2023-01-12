brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
               'Flamengo', 'Athlético-PR', 'Atlético-MG', 'Fortaleza',
               'São Paulo', 'América-MG', 'Botafogo', 'Santos',
               'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
               'Ceará', 'Athlético-GO', 'Avaí', 'Juventude')
print(f'\033[36m5 PRIMEIROS COLOCADOS:\033[m {brasileirao[0:5]}')
print('-' * 23)
print(f'\033[36mULTIMOS 4 COLOCADOS:\033[m {brasileirao[-4:]}')
print('-' * 23)
print(f'\033[36mTIMES EM ORDEM ALFABÉTICA:\033[m {sorted(brasileirao)}')
print('-' * 23)
posicao = brasileirao.index('Palmeiras') + 1
print(f'O time Palmeiras esta em {posicao}° lugar')

'''sentinela = 0
while True:
    time = str(input('Digite o NOME DE UM TIME e veja sua COLOCAÇÂO: ')).strip()
    for i in brasileirao:
        if i == time:
            sentinela = 1
    if sentinela == 1:
        break
    print('Nome Inválido')
posicao = brasileirao.index(time) + 1
print(f'O time {time} esta em {posicao}° lugar')'''
