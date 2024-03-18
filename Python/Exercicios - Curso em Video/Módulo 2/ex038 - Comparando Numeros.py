n1 = int(input('Digite o PRIMEIRO numero:'))
n2 = int(input('Digite o SEGUNDO numero:'))

if n1 > n2:
    print('\nO PRIMEIRO valor é maior! -> {}'.format(n1))
elif n2 > n1:
    print('\nO SEGUNDO valor é maior! -> {}'.format(n2))
else:
    print('\nEsses números são de VALORES IGUAIS: {}'.format(n1))

