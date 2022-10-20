from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento:'))
sexo = str(input('Digite seu sexo:'
                 '\nF- Feminino | M- Masculino'
                 '\nOpcao:')).upper()
idade = atual- nascimento

if sexo == 'M':
    print('\nVoce tem {} anos de idade.'.format(idade))
    if idade < 18:
        media = 18 - idade
        ano = atual + media
        print('Você ainda irá se alistar! Faltam {} anos para o seu alistamento!'.format(media))
        print('Seu alistamento será em {}.'.format(ano))
    elif idade == 18:
        print('Você ja esta no ano de alistamento! Aliste-se o mais rapido possivel!')
    else:
        media = idade - 18
        ano = atual - media
        print('Ja se passaram {} anos do seu alistamento!'.format(media))
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('\nPara mulheres o alistamento NAO É OBRIGATORIO!')
