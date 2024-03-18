maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso em KG da {}° pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('''\nDentre esses pesos:
O MAIOR é {:.1f}Kg
O MENOR é {:.1f}Kg'''.format(maior, menor))
