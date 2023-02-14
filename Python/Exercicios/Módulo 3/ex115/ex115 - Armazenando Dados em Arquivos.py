from time import sleep
from lib.interface import *
from lib.arquivo import *
arquivo = 'cadastro.txt'
if not arqExiste(arquivo):
    criarArq(arquivo)
while True:
    escreva('MENU')
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opcao == 1:
        # Opcao de ler o arquivo
        lerArquivo(arquivo)
    elif opcao == 2:
        # Opcao que cadastra nova pessoa
        escreva('Novo Cadastro')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        novoCadastro(arquivo, nome, idade)
    elif opcao == 3:
        escreva('Sistema Finalizado', cor='vermelho')
        break
    else:
        print('\033[31mOpção Inválida!, digite novamente\033[m')
    sleep(1)
