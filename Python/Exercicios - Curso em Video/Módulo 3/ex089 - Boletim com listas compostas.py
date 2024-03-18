sala = list()
aluno = list()
notas = []
media = 0
while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    sala.append(aluno[:])  # sala.append([nome, [nota1, nota2], media])
    aluno.clear()
    notas.clear()

    opcao = str(input('Deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
print('-' * 40)
print(f'{"NumAluno":<9}{"Nome":<10}{"Media"}')
for cont, i in enumerate(sala):
    media = (i[1][0] + i[1][1]) / 2
    print(f'{cont:^9}{i[0]:<10}{media:<5.1f}')
print('-' * 40)
while True:
    opcao = int(input('Digite o numero do aluno que deseja ver a nota (999 para encerrar): '))
    if opcao == 999:
        break
    media = (sala[opcao][1][0] + sala[opcao][1][1]) / 2
    print(f'{sala[opcao][0]} possui as notas: {sala[opcao][1]}')
    print('-' * 35)
print('\033[31mSISTEMA ENCERRADO\033[m')
