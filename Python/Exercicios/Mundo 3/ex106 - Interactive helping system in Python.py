from time import sleep
cores = {'None': '\033[m',
         'amarelo': '\033[30;43;1m',
         'azul': '\033[30;44;1m',
         'cinza': '\033[30;47;1m',
         'vermelho': '\033[30;41;1m'}


def ajuda(com):
    """
        -> Função de ajuda
    :param com: Recebe o comando
    :return: Sem retorno
    """
    escreva(f'Abrindo documentação da função/biblioteca {com} ...', cor='azul')
    sleep(1)
    print('\033[30;47;1m')
    help(com)
    print('\033[m', end='')
    sleep(1)


def escreva(msg, cor='None'):
    """
        -> Função que formata uma String com cores
    :param msg: Recebe a mesagem que deseja formatar
    :param cor: Recebe o nome da cor
    :return: Sem retorno
    """
    print(cores[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(cores['None'], end='')

while True:
    escreva('SISTEMA DE AJUDA PyHELP', cor='amarelo')
    usuario = str(input('Digite a função/biblioteca: (Digite FIM para sair) '))
    if usuario.lower() in 'fim':
        break
    ajuda(usuario)
escreva('SISTEMA FINALIZADO', cor='vermelho')
