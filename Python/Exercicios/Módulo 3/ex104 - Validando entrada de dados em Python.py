def leiaInt(frase):
    """
        -> Função que valida numero inteiro
    :param frase: Frase que ira aparecer no terminal
    :return: Retorna o numero inteiro
    """
    achouLetra = False
    num = 0
    while True:
        num = str(input(frase))
        if num.isnumeric():
            num = int(num)
            achouLetra = False
        else:
            achouLetra = True
            print('\033[31mERRO!, Digite um NUMERO INTEIRO\033[m')
        if not achouLetra:
            break
    return num


# Programa Principal
n = leiaInt('Digite um NUMERO INTEIRO: ')
print(f'O numero digitado foi: {n}')
