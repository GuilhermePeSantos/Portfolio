num = 0
i = 1
while True:
    num = int(input('Digite o valor que deseja ver sua tabuada: '))
    if num < 0:
        break
    print('-' * 15)
    while i < 11:
        print(f'{num} x {i:<2} = {num * i}')
        i += 1
    i = 1
    print('-' * 15)
print('\nSISTEMA ENCERRADO')