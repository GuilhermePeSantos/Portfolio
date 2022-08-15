x = float(input('Digite o valor do produto: '))
AV = x - (x * 0.05)
AP = x + (x * 0.08)
print('O valor deste produto com o preço de R${:.2f}, à vista custará R${:.2f} e à prazo custará R${:.2f}'.format(x,AV,AP))
