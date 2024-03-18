# Reduzindo ainda mais seu programa


def aumentar(valor=0.0, porcent=0.0, formatar=False):
    porcentagem = float(valor * (porcent / 100))
    result = valor + porcentagem
    return result if not formatar else moeda(result)  # 1 Forma de solução


def diminuir(valor=0.0, porcent=0.0, formatar=False):
    porcentagem = valor * (porcent / 100)
    result = valor - porcentagem
    return result if formatar is False else moeda(result)  # 2 Forma de solução


def dobro(valor=0.0, formatar=False):
    result = valor * 2
    if formatar:  # 3 Forma de solução
        return moeda(result)
    else:
        return result


def metade(valor=0.0, formatar=False):
    result = valor / 2
    if formatar:
        return moeda(result)
    else:
        return result


def moeda(valor=0.00):
    valor = f'{valor:.2f}'
    valorAlterado = valor.replace('.', ' ')
    split = valorAlterado.split()
    valor = ','.join(split)
    return f'R${valor}'


def resumo(valor=0.0, aument=0, reduc=0):
    print(f'{"-" * 40}\n{"Resumo do Valor":^40}\n{"-" * 40}')
    print(f'Preço Analizado: \t{moeda(valor):<10}')
    print(f'Dobro do valor: \t{dobro(valor, True):<10}')
    print(f'Metade do valor: \t{metade(valor, True):<10}')
    print(f'{aument}% de aumento: \t{aumentar(valor, aument, True):<10}')
    print(f'{reduc}% de redução: \t{diminuir(valor, reduc, True): <10}')
    print('-' * 40)
