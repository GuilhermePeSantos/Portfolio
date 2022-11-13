priTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão: '))
i = 0
result = priTermo
while i < 10:
    print('{} -> '.format(result), end='')
    result += razao
    i += 1
print('ACABOU!')
