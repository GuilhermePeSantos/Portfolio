from time import sleep
x = 0
soma = 0
numA = int(input('Digite o PRIMEIRO valor:'))
numB = int(input('Digite o SEGUNDO valor:'))
while x != 5:
    print('''\n\t\t--MENU--
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa''')
    x = int(input('Digite a opção:'))
    if x == 1:
        soma = numA + numB
        print('SOMA: {} + {} = {}'.format(numA, numB, soma))
    elif x == 2:
        multiplicar = numA * numB
        print('MULTIPLICAÇÂO: {} x {} = {}'.format(numA, numB, multiplicar))
    elif x == 3:
        maior = numA
        if numB > maior:
            maior = numB
        print('O MAIOR é {}'.format(maior))
    elif x == 4:
        numA = int(input('Digite o PRIMEIRO valor:'))
        numB = int(input('Digite o SEGUNDO valor:'))
    elif x == 5:
        print('ENCERRANDO...')
        sleep(1)
    else:
        print('NUMERO INVÁLIDO!, digite novamente')
    sleep(1)
print('\n\033[31mSISTEMA FINALIZADO\033[m')
