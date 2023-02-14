numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
cont = ' '
while True:
    opcao = int(input('Digite um numero inteiro de 0 á 20: '))
    if opcao >=0 and opcao <= 20:
        print(f'Voce digitou o número \033[32;1m{numeros[opcao]}\033[m')
        cont = str(input('\033[32;1m[S]-Sim\033[m \033[31;1m[N]-Não\033[m Você deseja continuar? '))
    if cont in 'nN':
        break
