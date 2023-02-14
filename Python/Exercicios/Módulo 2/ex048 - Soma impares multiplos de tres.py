soma = 0
total = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        total += 1 # mesma coisa que total = total + 1
        soma += i # mesma coisa que soma = soma + i
print('A soma de todos os {} valores impares multiplos de três é \033[34m{}'.format(total, soma))


'''
soma = 0
total = 0
for i in range(1, 501, 2):
    if i % 2 == 1 and i % 3 == 0:
        total += 1 # mesma coisa que total = total + 1
        soma += i # mesma coisa que soma = soma + i
print('A soma de todos os {} valores impares multiplos de três é \033[34m{}'.format(total, soma))'''