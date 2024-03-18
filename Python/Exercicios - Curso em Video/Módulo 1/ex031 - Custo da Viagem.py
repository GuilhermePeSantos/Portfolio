km = float(input('Digite a distancia em KM:'))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
#OU ->  preco = km * 0.50 if km <= 200 else km * 0.45
print('Percorrendo {}Km, essa viagem custará R${:.2f}'.format(km, preco))
