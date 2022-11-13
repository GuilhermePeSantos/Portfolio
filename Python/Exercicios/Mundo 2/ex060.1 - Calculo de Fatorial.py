from math import factorial
n = int(input('Digite um numero: '))
f = factorial(n)
print('\033[34m{}!\033[m = '. format(n), end='')
for i in range(n, 0, -1):
    if i == 1:
        print('{} = {}'.format(i, f))
    else:
        print('{} x '.format(i), end='')
