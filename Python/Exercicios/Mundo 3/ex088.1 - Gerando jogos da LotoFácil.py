from random import randint
from time import sleep
jogos = list()  # Lista com todos os jogos prontos
dados = [[], []]  # dados[0] numeros fixos | dados[1] numeros aleatorios
jogadas = int(input('Digite quantos jogos deseja fazer? '))  # Quantidade de jogadas
numFixos = str(input('Deseja colocar numeros fixos? [S/N] '))  # Quer ou não numeros fixos
if numFixos in 'Ss':
    print('-' * 40)
    quantNumFixos = int(input('Digite a quantidade de NUMEROS FIXOS: '))  # Quantidade de numeros fixos
    for i in range(0, quantNumFixos):
        dados[0].append(int(input(f'Digite o {i + 1}° numero fixo: ')))
    for i in range(0, jogadas):  # Cria os jogos
        for c in range(0, (15 - quantNumFixos)):
            x = randint(1, 25)
            while (x in dados[0]) or (x in dados[1]):
                x = randint(1, 25)
            dados[1].append(x)

        for c in range(0, len(dados[0])):  # Alimenta a lista dados[1] com os numeros fixos
            dados[1].append(dados[0][c])
        dados[1].sort()  # Ordena a lista dados[1] com todos os numeros
        jogos.append(dados[1][:])
        dados[1].clear()
if numFixos in 'Nn':
    for i in range(0, jogadas):  # Cria os jogos
        for c in range(0, 15):
            x = randint(1, 25)
            while (x in dados[0]) or (x in dados[1]):
                x = randint(1, 25)
            dados[1].append(x)
        dados[1].sort()  # Ordena a lista dados[1] com todos os numeros
        jogos.append(dados[1][:])  # Adiciona o jogo na lista geral
        dados[1].clear()  # Limpa a lista dados para usar novamente
print('-' * 40)
print('\033[34;1mGERANDO JOGOS...\033[m\n')
sleep(1)
for i, j in enumerate(jogos):
    print(f'Jogo {i + 1}:  ', end='')
    for c in j:
        if c in dados[0]:
            print(f'\033[32;1m{c}\033[m  ', end='')
        else:
            print(f'{c}  ', end='')
    print(f'\n{"-" * 65}')
    sleep(1)
