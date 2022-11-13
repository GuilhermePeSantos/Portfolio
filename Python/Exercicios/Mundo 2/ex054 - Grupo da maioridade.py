import datetime
maiores = 0
menores = 0
atual = datetime.date.today().year # pegando o ano atual

for i in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
    idade = atual - ano
    if idade >= 18:
        maiores += 1 # incrementando a variavel maiores
    else:
        menores += 1 # incrementando a variavel menores

print('\nDENTRE ESTAS PESSOAS:')
print('{} \033[31mAINDA NÃO\033[m atingiram a maior idade'.format(menores))
print('{} \033[32mJÁ\033[m atingiram a maior idade'.format(maiores))
