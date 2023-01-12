pessoas = list()
dados = []
maiorPeso = menorPeso = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    peso = float(input('Digite o peso: '))
    dados.append(peso)
    pessoas.append(dados[:])
    if len(pessoas) == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
    dados.clear()
    opcao = str(input('Deseja continuar? [S/N]: '))
    if opcao in 'Nn':
        break
print('-' * 40)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'As pessoas mais pesadas possuem {maiorPeso:.2f}Kg: ', end='')
for p in pessoas:
    if maiorPeso == p[1]:
        print(f'[{p[0]}] ', end='')
print(f'\nAs pessoas mais leves possuem {menorPeso:.2f}Kg: ', end='')
for p in pessoas:
    if menorPeso == p[1]:
        print(f'[{p[0]}] ', end='')
