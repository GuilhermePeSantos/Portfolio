numeros = (int(input('Digite o PRIMEIRO numero: ')),
           int(input('Digite o SEGUNDO numero: ')),
           int(input('Digite o TERCEIRO numero: ')),
           int(input('Digite o ULTIMO numero: ')))
print('{}\nValores: \033[32m{}\033[m'.format('-' * 30, numeros))
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    posicao = numeros.index(3) + 1
    print(f'O número 3 esta na {posicao}° posição')
else:
    print('O número 3 não foi digitado')

print('Os numeros PARES digitados são: ', end='')
for ref in numeros:
    if ref % 2 == 0:
        print(ref, end=' ')
