priTermo = int(input('Digite o PRIMEIRO termo: '))
razao = int(input('Digite a RAZAO: '))
x = 10 #Armazema a quantidade de repetições
i = 0 #Indice de repeticoes
termos = 1
resultado = priTermo
while termos != 0:
    while i < x:
        print(' {} ->'.format(resultado), end='')
        resultado = resultado + razao
        i += 1
    print(' ...')
    termos = int(input('\nDigite quantos termos quer mostrar a mais: '))
    x += termos
print('\nPrograma Encerrado com {} termos exibidos'.format(x))
