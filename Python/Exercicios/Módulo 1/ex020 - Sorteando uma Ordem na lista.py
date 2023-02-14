from random import shuffle
N1 = str(input('Digite o PRIMEIRO nome:'))
N2 = str(input('Digite o SEGINDO nome:'))
N3 = str(input('Digite o TERCEIRO nome:'))
N4 = str(input('Digite o QUARTO nome:'))
lista = [N1, N2, N3, N4]
shuffle(lista)
print('A ordem de apresentação é: {}'.format(lista))
