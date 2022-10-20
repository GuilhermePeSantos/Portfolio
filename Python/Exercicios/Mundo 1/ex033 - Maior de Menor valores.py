N1 = int(input('Digite o primeiro numero:'))
N2 = int(input('Digite o segundo numero:'))
N3 = int(input('Digite o terceiro numero:'))
#Verificando o menor valor
menor = N1
if N2 < N1 and N2 < N3:
    menor = N2
if N3 < N2 and N3 < N1:
    menor = N3
#Verificando o maior valor
maior = N1
if N2 > N1 and N2 > N3:
    maior = N2
if N3 > N1 and N3 > N2:
    maior = N3
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))


#Outra forma de encontrar
'''if N1 < N2 < N3:
    print('Maior {}'.format(N3))
    print('MENOR {}'.format(N1))
if N1 < N2 > N3:
    if N1 < N3:
        print('MAIOR {}'.format(N2))
        print('MENOR {}'.format(N1))
    else:
        print('MAIOR {}'.format(N2))
        print('MENOR {}'.format(N3))
if N1 > N2 < N3:
    if N1 < N3:
        print('MAIOR {}'.format(N3))
        print('MENOR {}'.format(N2))
    else:
        print('MAIOR {}'.format(N1))
        print('MENOR {}'.format(N2))
if N1 > N2 > N3:
    print('MAIOR {}'.format(N1))
    print('MENOR {}'.format(N3))'''

