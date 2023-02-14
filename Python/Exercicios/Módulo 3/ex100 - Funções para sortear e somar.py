from random import randint


def sorteia(lista):
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)


def somaPar(lista):
    soma = 0
    numPar = list()
    for v in lista:
        if v % 2 == 0:
            soma += v
            numPar.append(v)
    print(f'A soma dos numeros PARES {numPar} é {soma}')


# Programa Principal
numeros = list()
sorteia(numeros)
print(f'Numeros sorteados: ', end='')
for i in numeros:
    print(f'{i}  ', end='')
print()
somaPar(numeros)
