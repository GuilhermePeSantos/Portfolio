valor_casa = float(input('Digite o valor da casa: R$'))
salario_comprador = float(input('Digite seu salario: R$'))
anos = int(input('Digite em quantos anos vai pagar:'))
porcentagem = salario_comprador * 0.30
prestacoes = valor_casa / (anos * 12)

if prestacoes > porcentagem:
    print('\033[1:31mEmprestimo negado!')
else:
    print('\033[1:32m\nEmprestimo concedido!\033[m', end='')
    print(' O valor de cada prestação será R${:.2f}'.format(prestacoes))
