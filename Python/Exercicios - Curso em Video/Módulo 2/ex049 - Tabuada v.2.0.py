num = int(input('Digite um numero:'))
print('\n{}'.format('-' * 15))
print('{:^15}\n'.format('Tabuada do {}'.format(num)))
for i in range(0, 11):
    print(' {} X {:<2} = {}'.format(num, i, (num * i)))
print('{}'.format('-' * 15))
