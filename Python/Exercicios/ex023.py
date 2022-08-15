num = str(input('Digite um número:'))
soma = len(num)
n = int(num)
print('Unidade: {}'.format(num[soma - 1]))
print('Dezena: {}'.format(num[soma - 2]))
print('Centena: {}'.format(num[soma - 3]))
print('Milhar: {}'.format(num[soma - 4]))

'''print('Unidade {}'.format(num[3]))
print('Dezena {}'.format(num[2]))
print('Centena {}'.format(num[1]))
print('Milhar {}'.format(num[0]))'''

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('\nUnidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
