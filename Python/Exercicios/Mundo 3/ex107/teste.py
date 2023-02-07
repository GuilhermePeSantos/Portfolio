import moeda
valor = float(input('Digite o preco R$'))
print(f'A metade do R${valor} é R${moeda.metade(valor)}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor, 10)}')
