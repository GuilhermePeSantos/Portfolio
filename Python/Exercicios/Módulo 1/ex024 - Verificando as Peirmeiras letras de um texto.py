nomC = str(input('Digite o nome de uma cidade: ')).strip()
split = nomC.split()
print('Essa cidade começa com o nome SANTO ? {}'.format('SANTO' in split[0].upper()))
