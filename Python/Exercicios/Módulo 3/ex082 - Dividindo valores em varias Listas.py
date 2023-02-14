lista = []
while True:
    numero = int(input('Digite um numero (Se quiser parar digite -1): '))
    if numero == -1:
        break
    lista.append(numero)
pares = list()
impares = list()
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'\nOs numeros digitados foram: {lista}')
print(f'Os numeros PARES são: {pares}')
print(f'Os numeros IMPARES são: {impares}')
