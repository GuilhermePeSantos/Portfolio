jogador = dict()
jogador['Nome'] = str(input('Nome do Jogador: '))
jogador['Partidas'] = int(input('Partidas Jogadas: '))
jogador['Gols'] = list()
for i in range(0, jogador['Partidas']):
    jogador['Gols'].append(int(input(f'Gols feitos na partida {i + 1}: ')))
jogador['TotGols'] = sum(jogador['Gols'])  # sum() funcao de soma
print('-=' * 30)
print(jogador)
print('-' * 40)
for key, value in jogador.items():
    print(f'{key} possui o valor {value}')
print('-' * 40)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'\tPartida {i + 1}: {jogador["Gols"][i]} gols')
print(f'Total de Gols: {jogador["TotGols"]}')
