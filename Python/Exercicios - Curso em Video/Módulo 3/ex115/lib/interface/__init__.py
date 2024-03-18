def leiaInt(frase):
    while True:
        try:
            valor = int(input(frase))
        except (ValueError, TypeError):
            print('\033[31mERRO: Valor Invalido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m\nERRO: Terminal Interrompido\033[m')
            return 0
        except:
            print('\033[31mERRO!\033[m')
            continue
        else:
            return valor


def escreva(msg, cor='none'):
    cores = {'none': '\033[m',
             'vermelho': '\033[31m',
             'verde': '\033[32m',
             'amarelo': '\033[33m',
             'azul': '\033[34m'}
    print(f'{cores[cor]}{linha()}')
    print(f'{msg:^40}')
    print(f'{linha()}{cores["none"]}')


def linha(tam=40):
    return '-' * tam


def menu(lista):
    for i, v in enumerate(lista):
        print(f'\033[33m[{i + 1}]\033[m - \033[34m{v}\033[m')
    print(linha())
    opcao = leiaInt('\033[34mDigite uma opção: \033[m')
    return opcao
