i = soma = total = 0 # Mesma coisa que i = 0, soma = =, total = 0
x = 1 # Para fazer a contagem 1°, 2°, 3°...
while i != 999:
    i = int(input('Para parar digite 999. Digite o {}° valor: '. format(x)))
    if i != 999:
        soma += i
        total += 1
    x += 1
print('\nA SOMA dos numeros digitados foi de: {}'.format(soma))
print('{} numeros foram digitados'.format(total))
