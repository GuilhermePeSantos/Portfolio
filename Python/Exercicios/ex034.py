salario = float(input('Digite seu salario:'))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print('Seu salario de R${:.2f} recebeu um aumento de R${:.2f}'.format(salario, aumento))
print('Salario atual: R${:.2f}'.format(salario + aumento))
