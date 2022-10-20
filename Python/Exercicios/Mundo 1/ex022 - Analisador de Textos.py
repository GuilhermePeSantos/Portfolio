nom = str(input('Digite o seu nome completo:'))
split = nom.split()
print('Letras maiúsculas - {}'.format(nom.upper()))
print('Letras minúsculas - {}'.format(nom.lower()))
print('Total de letras do nome - {}'.format(len(nom) - nom.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(split[0], len(split[0])))

'''guilherme pereira dos santos'''
