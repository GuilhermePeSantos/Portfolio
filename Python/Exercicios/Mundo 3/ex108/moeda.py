# Formatando moedas em Python


def aumentar(valor=0, porcent=0.0):
    porcentagem = float(valor * (porcent / 100))
    return valor + porcentagem


def diminuir(valor=0, porcent=0.0):
    porcentagem = valor * (porcent / 100)
    return valor - porcentagem


def dobro(valor=0):
    return valor * 2


def metade(valor=0):
    return valor / 2


def moeda(valor=0.00, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')