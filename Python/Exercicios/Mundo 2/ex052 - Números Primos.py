num = int(input('Digite um numero:'))
achou = 0
print('Divisões:', end='')
for i in range(1, num + 1):
    if num % i == 0:
        achou += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\n\n\033[mO numero {} foi divisivel {} vezes pelos seus anteriores'.format(num, achou))
if achou == 2:
    print('\033[34m{}\033[m É um numero primo'.format(num))
else:
    print('\033[34m{}\033[m NÃO É um numero primo'.format(num))
