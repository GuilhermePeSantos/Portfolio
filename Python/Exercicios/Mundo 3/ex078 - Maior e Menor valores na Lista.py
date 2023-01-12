lista = list()
for i in range(0, 5):
    lista.append(int(input(f'Digite o valor da {i}ª posição: ')))
print(f'Voce digitou os valores: {lista}')
print(f'O MAIOR valor digitado foi {max(lista)} e esta nas posições: ', end='')
for c, v in enumerate(lista):
    if max(lista) == v:
        print(f'{c}, ', end='')

print(f'\nO MENOR valor digitado foi {min(lista)} e esta nas posições: ', end='')
for c, v in enumerate(lista):
    if min(lista) == v:
        print(f'{c}, ', end='')
