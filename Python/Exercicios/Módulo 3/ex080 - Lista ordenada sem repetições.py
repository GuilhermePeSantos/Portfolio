lista = list()
for i in range(0, 5):
    numero = int(input('Digite um numero: '))
    if len(lista) == 0 or numero < lista[0]:
        print('Numero adicionado na posção 0 da lista')
        lista.insert(0, numero)
    elif numero > lista[len(lista) - 1]:  # Ou lista[-1]
        print('Numero adicionado no final da lista')
        lista.append(numero)
    else:
        for c in range(0, len(lista)):
            if lista[c] < numero < lista[c + 1]:
                print(f'Numero adicionado na {c + 1}ª posição')
                lista.insert(c + 1, numero)
print('-' * 40)
print(f'Lista em ordem crescente: {lista}')
