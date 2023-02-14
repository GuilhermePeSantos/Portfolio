mais18 = homens = mulheres = 0

print('\033[34m-> CADASTRO DE PESSOAS <-\033[m')
while True:
    print('--' * 15)
    idade = int(input('Digite a IDADE: '))
    sexo = str(input('Digite o SEXO [F/M]: ')).strip()
    while sexo not in 'FfMm':
        sexo = str(input('Digite o SEXO [F/M]: ')).strip()
    if idade > 18:
        mais18 += 1
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        mulheres += 1
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('\nDeseja continuar? [S/N]: ')).strip()
    if opcao in 'Nn':
        print('--' * 15)
        break
print('\nDentre essas pessoas,')
print(f'{mais18} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres tem menos que 20 anos.')
