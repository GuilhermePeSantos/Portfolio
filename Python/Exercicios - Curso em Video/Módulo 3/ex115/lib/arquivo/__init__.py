def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        pass
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    cadastro = list()
    try:
        a = open(nome, 'rt')
    except:
        print(f'Falha ao abrir o arquivo {nome}')
    else:
        escreva('Pessoas Cadastradas')
        for i, v in enumerate(open(nome, 'rt').readlines()):
            if v.replace('\n', '') != '':
                cadastro.append(v.replace('\n', '').strip())
                indice = cadastro[-1].find(';')
                print(f'{cadastro[-1][:indice]:<35}{cadastro[-1][indice + 1:]} anos')
    finally:
        a.close()


def novoCadastro(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('Falha ao abrir o arquivo!')
    else:
        try:
            a.write(f'\n{nome};{idade}')
        except:
            print('Erro ao cadastrar!')
        else:
            print('Cadastro realizado com sucesso!')


def escreva(msg, cor='none'):
    cores = {'none': '\033[m',
             'vermelho': '\033[31m',
             'verde': '\033[32m',
             'amarelo': '\033[33m',
             'azul': '\033[34m'}
    print(f'{cores[cor]}{"-" * 40}')
    print(f'{msg:^40}')
    print(f'{"-" * 40}{cores["none"]}')


def leiaInt(frase):
    while True:
        try:
            valor = int(input(frase))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: O valor digitado foi invalido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida!')
            return 0
        else:
            return valor