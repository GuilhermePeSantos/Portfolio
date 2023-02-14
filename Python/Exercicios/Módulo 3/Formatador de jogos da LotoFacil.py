jogo_semipronto = list()
jogo_pronto = list()
jogo_geral = list()
while True:
    jogo = str(input('Digite o Jogo: '))
    jogo_split = jogo.split()
    for i in jogo_split:
        jogo_semipronto.append(i[1:])
    for i in jogo_semipronto:
        if i[0] == '0':
            jogo_pronto.append(int(i[1:]))
        else:
            jogo_pronto.append(int(i))
    jogo_geral.append(jogo_pronto[:])
    jogo_split.clear()
    jogo_semipronto.clear()
    jogo_pronto.clear()
    opcao = str(input('Deseja contiuar? [S/N]: '))
    if opcao in 'Nn':
        break
for i in jogo_geral:
    print(f'{i},\n\t\t\t\t\t', end='')


'''
    if i < (len(jogo_geral) - 1):
        print(f'\t\t\t\t\t{v},\n', end='')
    else:
        print(f'\t\t\t\t\t{v}', end='')'''