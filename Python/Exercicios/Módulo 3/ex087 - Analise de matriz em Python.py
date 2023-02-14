matriz = list()
dados = [[], []]
x = y = somaPares = somaTerc = maior = 0
for i in range(0, 9):
    matriz.append(int(input(f'Digite um valor para a posição [{x}, {y}]: ')))
    y += 1
    if y == 3:
        y = 0
        x += 1
x = y = 0
print('-' * 40)
for i in range(0, 3):
    for x in range(0, 3):
        print(f'[{matriz[y]:^5}] ', end='')
        if x == 2:
            somaTerc += matriz[y]
            dados[1].append(matriz[y])
        if i == 1 and x == 0:
            maior = matriz[y]
        elif i == 1 and (x == 1 or x == 2):
            if matriz[y] > maior:
                maior = matriz[y]
        y += 1
    print()
print('-' * 40)
for i in matriz:
    if i % 2 == 0:
        somaPares += i
        dados[0].append(i)
print(f'A soma dos numeros PARES{sorted(dados[0])} é de: {somaPares}')
print(f'A soma da TERCEIRA COLUNA{dados[1]} é de: {somaTerc}')
print(f'O MAIOR VALOR da segunda linha é: {maior}')
