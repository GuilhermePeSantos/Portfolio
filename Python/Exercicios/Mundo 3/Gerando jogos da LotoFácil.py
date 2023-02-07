from random import randint
from time import sleep
from operator import itemgetter

# Variaveis
somaNumeros = 0
jogosProntos = list()  # Lista com todos os jogos prontos
dados = [[], []]  # dados[0] numeros fixos | dados[1] numeros aleatorios
# jogosBase['Jogos'] - Lista geral com varias listas dos jogos alimentados manualmente | jogosBase['TotalNumeros'] - Lista com o total de cada numero
jogosBase = {'Jogos': [[1, 4, 5, 6, 8, 10, 11, 13, 14, 15, 17, 19, 22, 23, 24],
                       [1, 2, 3, 4, 6, 7, 8, 12, 15, 19, 20, 21, 22, 23, 25],
                       [2, 3, 4, 5, 9, 10, 11, 14, 15, 16, 17, 20, 21, 22, 24],    # Mais antigo: 20/08/2022
                       [1, 4, 6, 8, 9, 10, 13, 14, 15, 17, 18, 19, 20, 21, 24],
                       [2, 4, 6, 7, 11, 12, 13, 14, 15, 17, 18, 19, 22, 23, 25],  # Mais recente: 31/01/2023
                       [2, 3, 5, 6, 8, 9, 11, 13, 16, 17, 18, 21, 23, 24, 25],
                       [2, 3, 5, 6, 7, 8, 9, 12, 15, 18, 19, 20, 21, 22, 24],
                       [2, 3, 8, 11, 12, 13, 16, 17, 18, 19, 20, 22, 23, 24, 25],  # 23 18 6 17 7
                       [1, 3, 4, 8, 11, 12, 15, 16, 18, 19, 20, 22, 23, 24, 25],
                       [1, 2, 3, 4, 7, 10, 11, 12, 13, 14, 16, 17, 20, 24, 25],
                       [1, 2, 3, 5, 9, 10, 11, 12, 13, 19, 21, 22, 23, 24, 25],
                       [1, 2, 3, 5, 6, 13, 14, 16, 18, 19, 21, 22, 23, 24, 25],
                       [1, 2, 4, 5, 8, 9, 10, 11, 14, 15, 16, 17, 18, 21, 25],
                       [1, 3, 4, 7, 8, 9, 10, 11, 12, 13, 15, 18, 21, 22, 25],
                       [2, 3, 4, 7, 8, 9, 14, 16, 17, 18, 19, 20, 22, 24, 25],
                       [2, 5, 7, 8, 9, 10, 11, 12, 13, 16, 18, 19, 20, 21, 23],
                       [1, 2, 5, 7, 9, 10, 12, 13, 14, 17, 19, 20, 21, 23, 24],
                       [1, 2, 4, 6, 7, 10, 14, 15, 16, 17, 18, 19, 21, 23, 25],
                       [1, 3, 4, 5, 7, 9, 12, 14, 16, 18, 19, 21, 22, 23, 25],
                       [3, 4, 5, 6, 7, 9, 13, 14, 16, 17, 19, 21, 22, 24, 25],
                       [1, 3, 4, 6, 7, 8, 11, 13, 14, 15, 16, 20, 22, 23, 24],
                       [1, 2, 3, 4, 5, 8, 9, 10, 12, 17, 20, 22, 23, 24, 25],
                       [2, 5, 6, 9, 10, 11, 13, 14, 15, 18, 19, 20, 21, 22, 25],
                       [1, 2, 3, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 18, 22],
                       [1, 2, 8, 9, 10, 11, 12, 13, 15, 17, 20, 21, 23, 24, 25],
                       [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 23, 24],
                       [3, 7, 8, 9, 10, 13, 14, 15, 16, 19, 20, 21, 22, 24, 25],
                       [1, 2, 3, 4, 6, 8, 9, 11, 13, 14, 15, 20, 21, 22, 24],
                       [1, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17, 19, 21, 22, 23],
                       [1, 3, 5, 8, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 25],
                       [1, 2, 3, 4, 5, 6, 8, 12, 18, 20, 21, 22, 23, 24, 25],
                       [1, 2, 3, 6, 7, 8, 10, 12, 15, 17, 20, 21, 22, 23, 24],
                       [1, 3, 5, 6, 8, 12, 13, 14, 17, 19, 20, 21, 22, 24, 25],
                       [1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 14, 17, 22, 23, 24],
                       [2, 5, 6, 8, 9, 10, 11, 14, 16, 17, 18, 19, 20, 21, 23],
                       [2, 3, 4, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23],
                       [1, 2, 3, 4, 5, 9, 10, 11, 13, 14, 16, 17, 18, 20, 22],
                       [1, 2, 6, 9, 10, 11, 12, 13, 15, 17, 18, 19, 21, 24, 25],
                       [1, 3, 5, 6, 7, 8, 11, 12, 15, 17, 18, 20, 21, 23, 24],
                       [2, 3, 4, 5, 8, 9, 10, 14, 15, 16, 18, 21, 22, 23, 24],
                       [2, 4, 5, 6, 7, 8, 10, 11, 14, 16, 17, 18, 20, 22, 25],
                        [3, 4, 5, 6, 7, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                        [1, 3, 4, 5, 7, 8, 9, 13, 14, 15, 16, 19, 20, 21, 24],
                        [4, 5, 6, 7, 8, 9, 11, 16, 17, 18, 20, 21, 22, 24, 25],
                        [2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 20, 22, 23, 25],
                        [1, 2, 3, 4, 8, 10, 11, 12, 13, 14, 20, 21, 22, 23, 25],
                        [3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 19, 23, 24],
                        [2, 4, 7, 8, 10, 12, 13, 14, 16, 17, 18, 19, 21, 22, 24],
                        [1, 2, 4, 5, 9, 10, 11, 13, 15, 16, 17, 19, 20, 23, 24],
                        [4, 5, 6, 7, 8, 9, 10, 12, 13, 16, 19, 20, 22, 24, 25],
                        [2, 4, 5, 6, 7, 8, 9, 10, 11, 15, 16, 17, 20, 22, 24],
                        [1, 3, 4, 6, 8, 10, 11, 12, 14, 16, 17, 18, 21, 22, 24],
                        [2, 6, 8, 9, 11, 13, 14, 15, 16, 18, 19, 21, 22, 23, 25],
                        [2, 4, 7, 9, 10, 12, 13, 14, 16, 18, 20, 22, 23, 24, 25],
                        [1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 14, 15, 16, 20, 25],
                        [2, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15, 20, 22, 23, 24],
                        [2, 3, 5, 6, 9, 10, 11, 13, 15, 16, 17, 19, 21, 22, 24],
                        [1, 2, 5, 7, 8, 9, 10, 11, 12, 13, 18, 20, 21, 22, 25],
                        [1, 3, 5, 7, 8, 13, 15, 17, 18, 19, 21, 22, 23, 24, 25],
                        [1, 4, 6, 7, 8, 9, 10, 11, 14, 15, 19, 20, 21, 24, 25],
                        [1, 3, 5, 8, 9, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24],
                        [1, 2, 3, 4, 8, 9, 10, 11, 13, 15, 19, 20, 23, 24, 25],
                        [2, 3, 4, 7, 8, 10, 11, 12, 13, 19, 20, 21, 22, 23, 24],
                        [3, 6, 7, 8, 9, 11, 12, 13, 15, 16, 18, 19, 20, 21, 25],
                        [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18, 23, 24, 25],
                        [1, 3, 5, 6, 7, 11, 12, 13, 14, 16, 18, 19, 21, 22, 25],
                        [3, 4, 5, 6, 9, 10, 12, 13, 14, 16, 17, 19, 20, 22, 23],
                        [1, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 17, 18, 22, 25],
                        [1, 2, 3, 6, 8, 10, 13, 14, 15, 16, 18, 19, 21, 24, 25],
                        [1, 3, 5, 7, 10, 11, 13, 15, 18, 19, 20, 21, 22, 23, 24],
                        [1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15, 16, 18, 21, 24],
                        [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 16, 17, 21, 24],
                        [2, 3, 4, 7, 9, 10, 11, 12, 13, 17, 18, 19, 20, 21, 25],
                        [1, 5, 6, 8, 9, 11, 13, 14, 15, 16, 19, 20, 21, 22, 23],
                        [1, 3, 5, 6, 9, 10, 13, 15, 16, 17, 19, 20, 21, 24, 25],
                        [2, 3, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 20, 21],
                        [1, 3, 4, 5, 6, 8, 10, 12, 14, 15, 16, 17, 19, 24, 25],
                        [3, 4, 10, 11, 12, 13, 15, 16, 17, 18, 19, 22, 23, 24, 25],
                        [2, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15, 18, 19, 20, 22],
                        [2, 3, 6, 7, 8, 10, 12, 14, 15, 16, 17, 19, 20, 23, 24],
                        [4, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 25],
                        [1, 3, 4, 5, 6, 9, 10, 13, 16, 17, 18, 19, 22, 24, 25],
                        [2, 3, 6, 8, 9, 10, 12, 13, 14, 15, 17, 20, 22, 23, 25],
                        [1, 2, 3, 5, 6, 7, 11, 12, 13, 14, 15, 17, 18, 20, 24],
                        [1, 2, 5, 6, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20],
                        [1, 2, 3, 4, 6, 9, 11, 12, 13, 16, 18, 19, 20, 22, 25],
                        [2, 4, 5, 8, 9, 13, 14, 15, 16, 17, 19, 20, 21, 22, 24],
                        [1, 3, 4, 5, 7, 8, 9, 12, 13, 14, 17, 19, 20, 23, 24],
                        [3, 6, 7, 9, 10, 11, 12, 14, 15, 16, 18, 19, 21, 22, 25],
                        [2, 3, 7, 8, 9, 11, 12, 14, 15, 16, 18, 20, 21, 22, 24],
                        [2, 4, 5, 9, 10, 12, 14, 15, 18, 19, 21, 22, 23, 24, 25],
                        [2, 4, 5, 8, 9, 10, 12, 13, 19, 20, 21, 22, 23, 24, 25],
                        [1, 3, 4, 5, 7, 8, 9, 10, 11, 13, 15, 18, 22, 24, 25],
                        [2, 4, 5, 6, 8, 10, 11, 13, 14, 15, 17, 20, 21, 23, 25],
                        [1, 2, 3, 4, 7, 9, 10, 14, 15, 16, 18, 20, 21, 22, 24],
                        [1, 3, 4, 6, 9, 11, 12, 14, 15, 16, 17, 18, 19, 24, 25],
                        [1, 4, 5, 7, 9, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22],
                        [2, 4, 5, 6, 7, 8, 11, 14, 17, 18, 19, 20, 21, 23, 24],
                        [1, 2, 3, 6, 8, 9, 10, 13, 14, 16, 17, 20, 21, 22, 25],
                        [2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 14, 19, 21, 22, 25],
                        [1, 4, 9, 10, 11, 12, 13, 14, 15, 17, 20, 21, 22, 23, 25],
                        [1, 3, 7, 8, 9, 10, 13, 14, 16, 17, 20, 21, 22, 24, 25],
                        [3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 17, 20, 22, 23, 24],
                        [3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 18, 19, 20, 21, 25],
                        [2, 4, 5, 7, 8, 12, 14, 17, 18, 20, 21, 22, 23, 24, 25],
                        [1, 4, 5, 6, 7, 10, 11, 12, 13, 15, 16, 18, 22, 23, 24],
                        [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 17, 19, 20, 25],
                        [2, 3, 4, 5, 7, 9, 10, 11, 12, 14, 15, 20, 22, 23, 25],
                        [1, 2, 3, 5, 7, 9, 10, 11, 13, 14, 15, 16, 18, 19, 23],
                        [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15, 16, 17, 20, 25],
                        [1, 2, 3, 4, 5, 6, 7, 9, 11, 16, 17, 18, 19, 20, 25],
                        [1, 3, 5, 6, 7, 8, 10, 11, 12, 13, 17, 18, 22, 24, 25],
                        [1, 2, 3, 4, 6, 7, 9, 10, 12, 14, 16, 18, 21, 22, 25],
                        [2, 3, 5, 6, 8, 9, 10, 14, 15, 17, 19, 20, 21, 22, 25],
                        [1, 2, 3, 4, 6, 10, 13, 16, 17, 19, 20, 21, 23, 24, 25],
                        [1, 2, 3, 5, 6, 8, 11, 14, 15, 16, 18, 19, 20, 21, 25],
                        [1, 3, 6, 9, 10, 11, 13, 16, 17, 18, 19, 20, 21, 23, 25],
                        [2, 3, 4, 5, 6, 7, 8, 13, 14, 15, 17, 19, 21, 22, 25],
                        [1, 3, 5, 7, 8, 9, 10, 11, 12, 15, 16, 17, 20, 22, 24],
                        [3, 5, 6, 7, 9, 11, 12, 15, 17, 18, 19, 20, 21, 24, 25],
                        [1, 2, 4, 8, 9, 11, 12, 14, 15, 17, 18, 19, 23, 24, 25],
                        [1, 3, 5, 7, 8, 9, 10, 14, 16, 17, 18, 22, 23, 24, 25],
                        [3, 6, 7, 8, 9, 10, 11, 14, 16, 18, 19, 20, 21, 23, 24],
                        [1, 2, 5, 7, 9, 11, 12, 15, 16, 19, 21, 22, 23, 24, 25],
                        [4, 5, 6, 7, 9, 12, 13, 14, 15, 16, 18, 19, 20, 22, 23]
                        ],
             'TotalNumeros': {}}
jogosBase_SN = str(input('DESEJA USAR OUTROS JOGOS COMO BASE? [S/N]: ')).strip()[0]  # Pergunta se deseja colocar jogos como base
while jogosBase_SN not in 'SsNn':
    print('\033[31;1mLetra invalida\033[m, digite somente S ou N.')
    jogosBase_SN = str(input('DESEJA USAR OUTROS JOGOS COMO BASE? [S/N]: ')).strip()[0]  # Pergunta se deseja colocar jogos como base
print('-' * 40)
if jogosBase_SN in 'Ss':
    for x in range(1, 26):   # Verifica e soma a quantidade de cada numero, 1 à 25
        jogosBase['TotalNumeros'][f'{x}'] = 0  # Cria as keys de 'TotalNumeros' e igua-la elas a 0
        for i, v in enumerate(jogosBase['Jogos']):  # Varre as listas de jogos
            for valor_lista in v:  # Varre os valores das listas de jogos
                if x == valor_lista:
                    somaNumeros += 1
        jogosBase['TotalNumeros'][f'{x}'] = somaNumeros
        somaNumeros = 0
    TotalNumeros_Decrescente = sorted(jogosBase['TotalNumeros'].items(), key=itemgetter(1), reverse=True)  # Coloca em ordem decrescente os numeros mais sorteados
    print(f'\t\t{"Numeros":<7} | {"QtdSorteada":<11} | {"QtdJogosLidos":<13}')  # Printa o rank de numeros mais sorteados
    for i, v in enumerate(TotalNumeros_Decrescente):  # Printa o rank de numeros mais sorteados
        if i == 0:
            print(f'{i + 1}°\t\t{int(v[0]):^7}-->{v[1]:^11}   {len(jogosBase["Jogos"]):^13}')
        else:
            print(f'{i + 1}°\t\t{int(v[0]):^7}-->{v[1]:^11}')
    print('-' * 40)
    quantNumFixos = int(input('DIGITE A QUANTIDADE QUE DESEJA USAR DE NUMEROS MAIS SORTEADOS: '))
    print('-' * 40)
    for i in range(0, quantNumFixos):
        dados[0].append(int(TotalNumeros_Decrescente[i][0]))
    jogadas = int(input('DIGITE QUANTOS JOGOS DESEJA FAZER? '))  # Quantidade de jogadas
    print('-' * 40)
    for i in range(0, jogadas):  # Cria os jogos
        for c in range(0, (15 - len(dados[0]))):
            x = randint(1, 25)  # Sorteia numeros aleatorios
            while (x in dados[0]) or (x in dados[1]):  # Nao deixa sortear numeros iguais
                x = randint(1, 25)
            dados[1].append(x)  # Adiciona em dados[1] o numero sorteado

        for c in range(0, len(dados[0])):  # Alimenta a lista dados[1] com os numeros fixos
            dados[1].append(dados[0][c])
        dados[1].sort()  # Ordena a lista dados[1] com todos os numeros
        jogosProntos.append(dados[1][:])
        dados[1].clear()

elif jogosBase_SN in 'Nn':
    jogadas = int(input('DIGITE QUANTOS JOGOS DESEJA FAZER? '))  # Quantidade de jogadas
    print('-' * 40)
    numFixos_SN = str(input('DESEJA COLOCAR NUMEROS FIXOS? [S/N]: ')).strip()[0]  # Quer ou não numeros fixos
    while numFixos_SN not in 'SsNn':
        print('\033[31;1mLetra invalida\033[m, digite somente S ou N.')
        numFixos_SN = str(input('DESEJA COLOCAR NUMEROS FIXOS? [S/N]: ')).strip()[0]  # Quer ou não numeros fixos
    if numFixos_SN in 'Ss':
        print('-' * 40)
        quantNumFixos = int(input('Digite a quantidade de NUMEROS FIXOS: '))  # Quantidade de numeros fixos
        for i in range(0, quantNumFixos):
            dados[0].append(int(input(f'\tDigite o {i + 1}° numero fixo: ')))
        for i in range(0, jogadas):  # Cria os jogos
            for c in range(0, (15 - quantNumFixos)):
                x = randint(1, 25)  # Sorteia numero aleatorio
                while (x in dados[0]) or (x in dados[1]):  # Nao deixa sortear numero iguai
                    x = randint(1, 25)
                dados[1].append(x)  # Adiciona em dados[1] o numero sorteado

            for c in range(0, len(dados[0])):  # Alimenta a lista dados[1] com os numeros fixos
                dados[1].append(dados[0][c])
            dados[1].sort()  # Ordena a lista dados[1] com todos os numeros
            jogosProntos.append(dados[1][:])
            dados[1].clear()
    if numFixos_SN in 'Nn':
        for i in range(0, jogadas):  # Cria os jogos
            for c in range(0, 15):
                x = randint(1, 25)
                while (x in dados[0]) or (x in dados[1]):
                    x = randint(1, 25)
                dados[1].append(x)
            dados[1].sort()  # Ordena a lista dados[1] com todos os numeros
            jogosProntos.append(dados[1][:])  # Adiciona o jogo na lista geral
            dados[1].clear()  # Limpa a lista dados para usar novamente
    print('-' * 40)

# Gera os jogos
print('\033[34;1mGERANDO JOGOS...\033[m\n')
sleep(1)
for i, j in enumerate(jogosProntos):
    print(f'Jogo {i + 1}:  ', end='')
    for c in j:
        if c in dados[0]:
            print(f'\033[32;1m{c}\033[m  ', end='')
        else:
            print(f'{c}  ', end='')
    print(f'\n{"-" * 65}')
    sleep(1)
