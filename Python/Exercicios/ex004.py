x = str(input('Digite um valor: '))
print('O seu tipo é: {}'.format(type(x)))
print('é alfabetico? R: {}'.format(x.isalpha()))
print('é numerico? R: {}'.format(x.isnumeric()))
print('é alfanumero? R: {}'.format(x.isalnum()))
print('é decimal? R: {}'.format(x.isdecimal()))
print('pode ser impresso? R: {}'.format(x.isprintable()))
print('está em caixa alta?? R: {}'.format(x.isupper()))
print('Esta capitalizada? R: {}'.format(x.istitle()))
