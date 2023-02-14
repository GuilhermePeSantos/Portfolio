preco = float(input('Digite o preço a ser pago:'))
print('''\n[1] A vista em Dinheiro ou Cheque
[2] A vista no Cartao
[3] 2X o Cartao
[4] 3X ou mais no Cartao''')
x = int(input('Digite a forma de pagamento:'))

if x == 1:
    desc = preco - (preco * 0.10)
elif x == 2:
    desc = preco - (preco * 0.05)
elif x == 3:
    print('\nSua compra sera parcelada em 2X de R${:.2f} SEM JUROS'.format((preco/2)))
elif x == 4:
    desc = preco + (preco * 0.20)
    parcelas = int(input('Quantas parcelas?'))
    print('\nSua compra sera parcelada em {}X de R${:.2f} COM JUROS'.format(parcelas, (desc / parcelas)))
else:
    print('\n\033[31mOPÇÂO INVALIDA\033[m, TENTE NOVAMENTE')
print('O valor final a ser pago sera de R${:.2f}'.format(preco))
