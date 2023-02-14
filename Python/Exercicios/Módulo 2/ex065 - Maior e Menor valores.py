opcao = ''
soma = total = maior = menor = 0
while opcao != 'N':
    num = int(input('Digite o {}° valor: '.format(total + 1)))
    soma += num
    total += 1
    if total == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Deseja continuar? [S] Sim | [N] Não:')).upper().strip()[0]
    while opcao != 'S' and opcao != 'N':
        print('\033[31mLETRA INVÁLIDA\033[m')
        opcao = str(input('Deseja continuar? [S] Sim | [N] Não:')).upper().strip()[0]
media = soma / total
print('\nA MEDIA dos {} numeros é de {:.2f}'.format(total, media))
print('O MAIOR valor foi {}'.format(maior))
print('O MENOR valor foi {}'.format(menor))
