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


def leiaFloat(frase):
    while True:
        try:
            valor = float(input(frase))
        except (ValueError, TypeError):
            print('\033[31mERRO: O valor digitado é invalido!\033[m')
        except KeyboardInterrupt:
            print('\nO usuario preferiu nao digitar o valor!')
            return 0
        else:
            return valor


inteiro = leiaInt('Numero Inteiro: ')
real = leiaFloat('Numero Real: ')
print(f'O numero INTEIRO digitado foi {inteiro}, e o numero REAL digitado foi {real}')
