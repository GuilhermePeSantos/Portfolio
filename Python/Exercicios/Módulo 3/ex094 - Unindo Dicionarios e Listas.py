todos = list()
pessoa = dict()
somaIdade = 0
while True:
    pessoa['Nome'] = str(input('NOME: ')).strip().capitalize()
    pessoa['Sexo'] = str(input('SEXO [M/F]: ')).strip().upper()
    while pessoa['Sexo'] not in 'MmFf':
        print('\033[31;1mLetra Invalida\033[m, digite somente M ou F.')
        pessoa['Sexo'] = str(input('SEXO [M/F]: '))
    pessoa['Idade'] = int(input('IDADE: '))
    todos.append(pessoa.copy())
    somaIdade += pessoa['Idade']
    pessoa.clear()
    opcao = str(input('Deseja continuar? [S/N] '))
    while opcao not in 'SsNn':
        print('\033[31;1mLetra Invalida\033[m, digite somente S ou N.')
        opcao = str(input('Deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
print('-' * 40)
print(f'- {len(todos)} pessoas foram cadastradas')
print(f'- A media de idade é {somaIdade / len(todos):.2f} anos')
print('- As mulheres cadastradas foram: ', end='')
for i in todos:
    if i['Sexo'] in 'Ff':
        print(f'[{i["Nome"]}]', end=' ')
print('\n- As pessoas com idade acima da media são: \n', end='')
for i in todos:
    if i['Idade'] >= (somaIdade / len(todos)):
        print('\t', end='')
        for key, value in i.items():
            print(f'{key} = {value}', end='; ')
        print()
