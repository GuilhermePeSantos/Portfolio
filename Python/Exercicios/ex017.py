import math
CO = float(input('Digite o valor do cateto oposto: '))
CA = float(input('Digite o valor do cateto adjacente: '))
SC = ((CO**2) + (CA**2))
result = SC**(1/2)
print('O comprimento da hipotenusa é {}'.format((result)))
