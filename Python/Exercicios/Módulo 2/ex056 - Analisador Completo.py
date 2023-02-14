somaIdade = 0
velho = 0
somaMenores = 0
maisVelho = ''
for i in range(1, 5):
    print('-- {}° PESSOA --'.format(i))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('F - Feminino | M - Masculino, Digite seu sexo: ')).upper().strip()

    somaIdade = somaIdade + idade # soma as idades para fazer a media

    if idade > velho and sexo == 'M':
        velho = idade
        maisVelho = nome

    if idade < 20 and sexo == 'F':
        somaMenores += 1

print('\nA media de idades destas pessoas é {:.1f} anos'. format(somaIdade / 4))
print('O homem mais velho se chama {} com {} anos de idade'.format(maisVelho, velho))
print('Mulheres menores que 20 anos: {}'.format(somaMenores))
