numeros = []
while True:
    numeros.append(int(input('Digite um numero: ')))
    opcao = str(input('[S]-Sim [N]-Nao Deseja continuar? '))
    if opcao in 'Nn':
        break
print('-' * 40)
print(f'Foram digitados {len(numeros)} numeros')
numeros.sort(reverse=True)
print(f'Valores em forma decrescente: {numeros}')
if 5 in numeros:
    print(f'O valor 5 FOI encontrado na lista')
else:
    print('O valor 5 NAO FOI encontrado na lista')
