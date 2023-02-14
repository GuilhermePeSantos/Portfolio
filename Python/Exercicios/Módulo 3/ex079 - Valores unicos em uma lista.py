numeros = list()
while True:
    numero = int(input('Digite um numero: '))
    if numero in numeros:
        print('Esse numero ja existe, digite outro.')
    else:
        numeros.append(numero)
    opcao = str(input('[S]-Sim [N]-Nao Deseja continuar? '))
    if opcao in 'Nn':
        break
numeros.sort()
print('-' * 30)
print(f'Voce digitou {numeros}')
