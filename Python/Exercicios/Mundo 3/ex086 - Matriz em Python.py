matriz = list()
x = y = 0
for i in range(0, 9):
    matriz.append(int(input(f'Digite o valor da posição [{x}, {y}]: ')))
    y += 1
    if y == 3:
        y = 0
        x += 1
x = y = 0
print('-' * 40)
for i in range(0, 3):
    for x in range(0, 3):
        print(f'[{matriz[y]:^5}] ', end='')
        y += 1
    print()

# Outra forma de Print
'''print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]')
print(f'[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]')
print(f'[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')'''

# Outra forma de solução
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-' * 40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()'''