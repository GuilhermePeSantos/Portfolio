from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Numeros sorteados: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO MAIOR numero é: {max(numeros)}')
print(f'O MENOR numero é: {min(numeros)}')


'''
maior = menor = numeros[0]
for i in numeros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print(f'O MAIOR numero é: {maior}')
print(f'O MENOR numero é: {menor}')'''
