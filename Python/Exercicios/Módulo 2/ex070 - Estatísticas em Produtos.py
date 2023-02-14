total = mais1000 = precoBarato = i = 0
nomeBarato = ''
print('{:^30}'.format('MERCADINHO'))
while True:
    print('-' * 30)
    nome = str(input('Digite o NOME do produto: ')).strip()
    preco = float(input('Digite o PRECO do produto: R$'))
    total += preco
    i += 1
    if i == 1:
        nomeBarato = nome
        precoBarato = preco
    else:
        if preco < precoBarato:
            nomeBarato = nome
            precoBarato = preco
    ''' #  Outra forma mais simplificada
        if i == 1 or preco < precoBarato:
        nomeBarato = nome
        precoBarato = preco
    '''

    if preco > 1000:
        mais1000 += 1
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if opcao in 'Nn':
        print('-' * 30)
        break
print('{:^30}'.format('SISTEMA ENCERRADO'))
print(f'Total gasto nesta compra foi de R${total:.2f}, com {i} produtos comprados')
print(f'Produtos com valor a cima de R$1000: {mais1000} ')
print(f"'{nomeBarato}' foi o produto mais barato custanto R${precoBarato:.2f}")
