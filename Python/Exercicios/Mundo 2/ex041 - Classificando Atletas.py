from datetime import date
ano = int(input('Digite seu ano de nascimento:'))
idade = date.today().year - ano #date.today().year pega o ano atual referente ao computador

if idade <= 9:
    print('\nEsse atleta possui {} anos, sendo da categoria \033[1;34mMIRIM!\033[m'.format(idade))
elif idade > 9 and idade <= 14:
    print('\nEsse atleta possui {} anos, sendo da categoria \033[1;34mINFANTIL!\033[m'.format(idade))
elif idade > 14 and idade <= 19:
    print('\nEsse atleta possui {} anos, sendo da categoria \033[1;34mJUNIOR!\033[m'.format(idade))
elif idade > 19 and idade <= 25:
    print('\nEsse alteta possui {} anos sendo da categoria \033[1;34mSÊNIOR!\033[m'.format(idade))
else:
    print('\nEsse atleta possui {} anos, sendo da categoria \033[1;34mMASTER!\033[m'.format(idade))
