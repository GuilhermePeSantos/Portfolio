def ficha(nome='<desconhecido>', gols=0):
    """
        -> Função que descreve uma ficha de um jogador
    :param nome: O nome do Jogador
    :param gols: A quantidade de Gols de Jogador
    :return: Sem retorno
    """
    return f'\nO jogador {nome} marcou {gols} gols(s)'


# Programa Principal
Jogador = str(input('NOME do Jogador: ')).strip()
Gols = str(input(f'GOLS de {Jogador}: ')).strip()
if Gols.isnumeric():
    Gols = int(Gols)
else:
    Gols = 0
if Jogador == '':
    print(ficha(gols=Gols))
else:
    print(ficha(Jogador, Gols))
