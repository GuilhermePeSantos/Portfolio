soma = 0
cont = 0
ordem = ['PRIMEIRO', 'SEGUNDO', 'TERCEIRO', 'QUARTO', 'QUINTO', 'SEXTO']
for i in range(0, 6):
    num = int(input('Digite o {} numero:'.format(ordem[i])))
    if num % 2 == 0:
        soma += num
        cont += 1
print('\nVoce digitou {} numeros PARES e soma deles é {}'.format(cont, soma))
