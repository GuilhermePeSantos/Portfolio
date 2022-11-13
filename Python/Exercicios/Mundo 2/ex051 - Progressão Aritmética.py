priTermo = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razao: '))
soma = priTermo
for i in range(0, 9):
    print(soma, end=' -> ')
    soma = soma + razao
print(soma)


'''primeiro = int(input('Primeiro termo:'))
razao = int(input('Razao:'))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{} '.format(i), end='')
print('ACABOU!')'''
