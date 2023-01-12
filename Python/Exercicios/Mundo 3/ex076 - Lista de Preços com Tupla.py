lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
x = 0
print('-' * 45)
print(f'{"LISTA DE PREÇOS":^37}')
for i in range(0, 9):
    print(f'{lista[x]:.<30} R$ {lista[x + 1]:>7.2f}')
    x += 2
print('-' * 45)
