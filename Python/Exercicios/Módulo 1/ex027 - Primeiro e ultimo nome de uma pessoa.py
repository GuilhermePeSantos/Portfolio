nom = str(input('Digite seu nome:'))
split = nom.split()
print('O PRIMEIRO nome é: {}'.format(split[0]))
print('O ULTIMO nome é: {}'.format(split[len(split) - 1]))
