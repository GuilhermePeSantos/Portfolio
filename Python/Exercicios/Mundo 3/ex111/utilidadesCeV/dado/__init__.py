# ex112 - Entrada de dados monetarios

def leiaDinheiro(frase):
    while True:
        valor = str(input(frase)).strip()
        somaPontoVirgula = 0
        achou = False
        for i in valor:
            if i == ',' or i == '.':
                somaPontoVirgula += 1
            if i not in '1234567890.,':
                achou = True
        if achou or valor == '' or somaPontoVirgula > 1:
            print(f'\033[31mERRO: \"{valor}\" é um preço invalido!\033[m')  # \" - printa aspas duplas | \"{valor}\" = "valor"
        else:
            if ',' in valor:
                valor = valor.replace(',', '.')
            break
    return float(valor)


# Outra forma de resolução
'''def leiaDinheiro(frase):
    valido = False
    while not valido:
        valor = str(input(frase)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO: \"{valor}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(valor)'''


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
