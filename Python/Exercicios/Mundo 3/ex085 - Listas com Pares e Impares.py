numeros = [[], []]
for i in range(0, 7):
    num = int(input(f'Digite o {i + 1}ª numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 == 1:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('-' * 40)
print(f'Os numeros PARES são: {numeros[0]}')
print(f'Os numeros IMPARES são: {numeros[1]}')
