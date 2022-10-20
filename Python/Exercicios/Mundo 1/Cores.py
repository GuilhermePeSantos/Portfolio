#1 Forma
print('\033[0;97;41mTESTE\033[m')
print('\033[4;33;44mTESTE\033[m')
print('\033[1;35;43mTESTE\033[m')
print('\033[30;42mTESTE\033[m')
print('\033[mTESTE\033[m')#Cor padrão do terminal
print('\033[7;97mTESTE\033[m')

#2 Forma
nome = str(input('\n\033[1;97mDigite seu nome:\033[m'))
print('Bem vindo ao Python, {}{}{} !!!'.format('\033[4;36m', nome, '\033[m'))

#3 Forma
cores = {'limpa':'\033[m',
         'ciano':'\033[36m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[31m',
         'roxo':'\033[4;35m'}
print('\n{}Tenha{} um {}Bom Dia{}!'.format(cores['roxo'], cores['limpa'], cores['amarelo'], cores['limpa']))
