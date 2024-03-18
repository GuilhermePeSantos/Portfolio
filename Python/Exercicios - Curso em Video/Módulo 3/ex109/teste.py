import moeda
preco = float(input('Digite um valor R$'))
print(f'\nA metade do valor {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro do valor {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando o valor {moeda.moeda(preco)} em 15% temos, {moeda.aumentar(preco, 15, True)}')
print(f'Diminuindo o valor {moeda.moeda(preco)} em 27% temos, {moeda.diminuir(preco, 27, True)}')