soma = qtd = 0
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        break
    soma += num
    qtd += 1
print(f'\nA soma dos {qtd} valores é de {soma}')
