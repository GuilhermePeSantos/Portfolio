palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro', 'aeiou')
print('\033[32m{:^42}\033[m'.format('Mostrando as VOGAIS de cada palavra'))
for i in palavras:
    print(f'\nAs VOGAIS da palavra {i.upper()} são: ', end='')
    for letra in i:
        if letra in 'aeiou':
            print(f' \033[4m{letra}\033[m ', end='')
