peso = float(input('Digite seu PESO em QUILOS:'))
altura = float(input('Digite sua ALTURA em METROS:'))

IMC = peso / (altura**2)
tipo = ['ABAIXO DO PESO', 'PESO IDEAL', 'SOBREPESO', 'OBESIDADE', 'OBESIDADE MORBIDA']

if IMC < 18.5:
    x = tipo[0]
elif IMC >= 18.5 and IMC <= 25:
    x = tipo[1]
elif IMC > 25 and IMC <= 30:
    x = tipo[2]
elif IMC > 30 and IMC <= 40:
    x = tipo[3]
else:
    x = tipo[4]

print('\nPesando {}kg e com uma altura de {:.2f}m, seu IMC é {:.1f} e voce esta com {}!'.format(peso, altura, IMC, x))


'''
if IMC < 18.5:
    print('\nPesando {} e com uma altura de {:.2f}, voce esta ABAIXO DO PESO!'.format(peso, altura))
elif IMC >= 18.5 and IMC <= 25:
    print('\nPesando {} e com uma altura de {:.2f}, voce esta no PESO IDEAL!'.format(peso, altura))
elif IMC > 25 and IMC <= 30:
    print('\nPesando {} e com uma altura de {:.2f}, voce esta com SOBREPESO!'.format(peso, altura))
elif IMC > 30 and IMC <= 40:
    print('\nPesando {} e com uma altura de {:.2f}, voce esta com OBESIDADE!'.format(peso, altura))
else:
    print('\nPesando {} e com uma altura de {:.2f}, voce esta com OBESIDADE MORBIDA!'.format(peso, altura))'''
