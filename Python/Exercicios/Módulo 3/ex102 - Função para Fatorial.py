def fatorial(num, show=False):
    """
        -> Função que calcula FATORIAL de um numero
    :param num: Recebe o numero a ser calculado
    :param show: True(Mostra a cadeia de cálculos e o resultado), False(Mostra apenas o resultado)
    :return: Retorna o fatorial de um numero
    """
    result = 1
    for i in range(num, 0, -1):
        if show:
            if i == num:
                print(f'{num}! =', end='')
            if i > 1:
                print(f' {i} x', end='')
            else:
                print(f' {i} = ', end='')
        result *= i
    return result


# Programa Principal
print(fatorial(5))
print(fatorial(5, True))
print(fatorial(5, show=True))
