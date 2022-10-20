v = int(input('Digite a velocidade do carro:'))
if v > 80:
    multa = (v - 80) * 7
    print('Você ultrapassou o limite de velocidade e pagará R${} de MULTA!'.format(multa))
else:
    print('Parabéns, você esta dentro do limite de velocidade! Tenha um Bom Dia!')