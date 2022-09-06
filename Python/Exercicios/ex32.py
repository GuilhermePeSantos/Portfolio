from datetime import date
ano = int(input('Digite o ano:'))
if ano == 0:
    ano = date.today().year #Usa o ano que o computador esta configurado

if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        print('O ano {} NÃO é BISSEXTO'.format(ano))
    else:
        print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÂO é BISSEXTO'.format(ano))
