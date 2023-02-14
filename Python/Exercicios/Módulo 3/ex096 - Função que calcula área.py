def area(l, c):
    a = l * c
    print(f'Um terreno {l:.2f}x{c:.2f} possui {a}m² de área')


# Programa Principal
print(f'{" ÁREA DE TERRENOS ":^30}')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
