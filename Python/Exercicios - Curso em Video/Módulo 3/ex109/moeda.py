# Formatando Moedas em Python


def aumentar(valor=0, porcent=0.0, formatar=False):
    porcentagem = float(valor * (porcent / 100))
    result = valor + porcentagem
    return result if not formatar else moeda(result)  # 1 Forma de solução


def diminuir(valor=0, porcent=0.0, formatar=False):
    porcentagem = valor * (porcent / 100)
    result = valor - porcentagem
    return result if formatar is False else moeda(result)  # 2 Forma de solução


def dobro(valor=0, formatar=False):
    result = valor * 2
    if formatar:  # 3 Forma de solução
        return moeda(result)
    else:
        return result


def metade(valor=0, formatar=False):
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