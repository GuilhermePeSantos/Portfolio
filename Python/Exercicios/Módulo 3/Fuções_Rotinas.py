def soma(a, b):  # Dentro dos parenteses das funções são os PARAMETROS
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}\n')


# Programa Principal
soma(4, 5)  # Dentro dos parenteses das funções são necessarios colocar os PARAMETROS
soma(a=10, b=5)
soma(b=7, a=9)


# Empacotamento de parametros
def contador(* n):  # Independente da quantidade dos parametros inseridos, o '*' indica que tudo sera colocado em 'n'
    print(f'\n{len(n)} numeros foram digitados: ', end='')
    for v in n:
        print(f'{v}, ', end='')


# Programa Principal
contador(3, 4)
contador(7, 3, 2, 7)
contador(1, 4, 2, 3, 1, 7, 4)


# Utilizando lista nas funções

def dobra(lista):
    pos = 0
    while pos < len(valores):
        lista[pos] *= 2
        pos += 1


# Programa Principal
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(f'\n\n{valores}')


# Interact Help
help(print)  # Funcao que me mostra como funciona cada comando ou biblioteca do python
print(input.__doc__)  # Printa a documentação do comando informado

# Docstrings
def soma(a, b):
    # Aqui é onde fica a DOCSTRING da função criada, dentro de 3 aspas duplas
    """
    -> Função criada para somar 2 valores
    :param a: Primeiro valor da soma
    :param b: Segundo valor da soma
    :return: Sem retorno
    Criada por Guilherme Santos
    """
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}\n')

help(soma)

# Parametros Opcionais
def soma(a, b=0, c=0):  # O parametro 'b' e 'c' é opcional, pode nao ser definido ao chamar a função
    s = a + b + c
    print(f'A soma vale {s}')

soma(2, 5)
soma(c=5, a=4)
soma(7, 3, 1)


# Escopo de variavel
def teste(b):# 'b' é parametro FORMAL
    a = 8  # Variavel 'a' LOCAL(funciona apenas dentro da funcao teste())
    b += 4
    c = 2
    print(f'A dentro vale {a}')  # a = 8
    print(f'B dentro vale {b}')  # b = 9
    print(f'C dentro vale{c}')  # c = 2


'''Programa Principal'''
a = 5  # Varievel 'a' GLOBAL(funciona no programa inteiro)
teste(a)  # 'a' é parametro REAL
print(f'A fora vale {a}')  # a = 5


def teste(b):# 'b' é parametro FORMAL
    global a  # A funcao passa a utilizar a variavel 'a' global
    a = 8  # A partir e agora a funcao passa a utilizar a variavel 'a' GLOBAL
    b += 4
    c = 2
    print(f'A dentro vale {a}')  # a = 8
    print(f'B dentro vale {b}')  # b = 9
    print(f'C dentro vale{c}')  # c = 2


'''Programa Principal'''
a = 5  # Varievel 'a' GLOBAL(funciona no programa inteiro)
teste(a)  # 'a' é parametro REAL
print(f'A fora vale {a}')  # a = 8

# Funçao com retorno
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(7, 1)
r2 = soma(5, 8, 2)
print(f'O resultado das somas é {r1} e {r2}')

# Escopo de Importação
def soma(a=0, b=0, c=0):
    from time import sleep  # Importa somante dentro da função, ocupando assim menos espaço na memoria
    s = (a + b + c)
    sleep(1)
    return s
