import math

valor = int(input('Digite o valor a ser sacado: R$'))
print('=' * 20)
print('{:^20}'.format('SAQUE'))
while True:
    if math.trunc(valor / 50) > 0:
        cedula = math.trunc(valor / 50)
        valor = valor - (cedula * 50)
        print(f'{cedula} cédulas de R$50')
    elif math.trunc(valor / 20) > 0:
        cedula = math.trunc(valor / 20)
        valor = valor - (cedula * 20)
        print(f'{cedula} cédulas de R$20')
    elif math.trunc(valor / 10) > 0:
        cedula = math.trunc(valor / 10)
        valor = valor - (cedula * 10)
        print(f'{cedula} cédulas de R$10')
    elif math.trunc(valor / 1) > 0:
        cedula = math.trunc(valor / 1)
        valor = valor - (cedula * 1)
        print(f'{cedula} cédulas de R$1')
    if valor == 0:
        break
print('=' * 20)
print('SAQUE REALIZADO COM \033[32mSUCESSO\033[m')

'''
#  Outra forma de codigo
import math
valor = int(input('Digite o valor a ser sacado: R$'))
cinquenta = vinte = dez = um = 0
print('=' * 20)
print('{:^20}'.format('SAQUE'))
while True:
    if math.trunc(valor / 50) != 0:
        cinquenta += 1
        valor = valor - 50
    elif math.trunc(valor / 20) != 0:
        vinte += 1
        valor = valor - 20
    elif math.trunc(valor / 10) != 0:
        dez += 1
        valor = valor - 10
    elif math.trunc(valor / 1) != 0:
        um += 1
        valor = valor - 1
    if valor == 0:
        break
print(f'{cinquenta} cédulas de R$50')
print(f'{vinte} cédulas de R$20')
print(f'{dez} cédulas de R$10')
print(f'{um} cédulas de R$1')
print('=' * 20)
print('SAQUE REALIZADO COM \033[32mSUCESSO\033[m')
'''
