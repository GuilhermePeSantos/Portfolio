num = int(input('Digite um numero:'))
x = num - 1
fatorial = num
print('\033[34m{}!\033[m = {} x '.format(num, num), end='')
while x > 0:
    print('{} x '.format(x) if x > 1 else '{} = {}'.format(x, fatorial), end='')
    fatorial = fatorial * x
    x -= 1

'''# Calculando fatorial utilizando o FOR
for x in range(num - 1, 0, -1):
    fatorial = fatorial * x'''

''''# Printando a sequencia utilizando for com o for
print('\033[34m{}!\033[m = '. format(num), end='')
for i in range(num, 0, -1):
    print('{} x '.format(i) if i > 1 else '{} = {}'.format(i, fatorial), end='')'''
