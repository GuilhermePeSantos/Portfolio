km = float(input('Digite a quantidade de KM rodados: '))
dias = float(input('Digite quantos dias o carro ficou alugado: '))
result = (km * 0.15) + (dias * 60)
print('O carro andou {}km por {} dias por isso irá pagar R${:.2f}'.format(km, dias, result))
