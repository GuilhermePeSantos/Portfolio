jogadores = list()
jogador = dict()
codigo = 0
while True:
    jogador['Nome'] = str(input('NOME: ')).strip().capitalize()
    jogador['Partidas'] = int(input(f'Digite quantas partidas {jogador["Nome"]} jogou? '))
    jogador['Gols'] = list()
    jogador['TotGols'] = 0
    for i in range(0, jogador['Partidas']):
        jogador['Gols'].append(int(input(f'\tGols na {i + 1}° partida: ')))
        jogador['TotGols'] += jogador['Gols'][i]
    jogadores.append(jogador.copy())
    jogador.clear()
    opcao = str(input('Deseja continuar? [S/N] '))
    while opcao not in 'SsNn':
        print('\033[31;1mLetra Invalida\033[m, digite somente S ou N.')
        opcao = str(input('Deseja continuar? [S/N] '))
    print('-' * 40)
    if opcao in 'Nn':
        break
print(f'{"COD":<5}{"NOME":<13}{"PARTIDAS":<10}{"GOLS":<20}{"TOTALGOLS":<9}')
for i, j in enumerate(jogadores):
    print('{:^5}{:<13}{:^10}{:<20}{:^9}'. format(i, j["Nome"], j["Partidas"], str(j["Gols"]), j["TotGols"]))
while True:
    codigo = int(input('Mostrar dados de qual jogador?(999 - parar) [Codigo]: '))
    if codigo < len(jogadores):
        print(f'--- Levantamento do jogador {jogadores[codigo]["Nome"]} ---')
        for i, g in enumerate(jogadores[codigo]['Gols']):
            print(f'\tJogo {i + 1}: {g} gols')
        print('-' * 40)
    else:
        if codigo == 999:
            break
        else:
            print('\033[31;1mCódigo não encontrado\033[m, digite novamente.')
print('\nSISTEMA ENCERRADO')