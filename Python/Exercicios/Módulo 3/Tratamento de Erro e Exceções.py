try:  # Tenta esse codigo
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):  # Se der erro no 'try', executa esse except, caso a Exceção for 'ValueError' ou 'TypeError'
    print('Tivemos um problema com tipos de dados que voce digitou!')
except ZeroDivisionError:  # Se de erro no 'try', executa esse except, caso a Exceção for 'ZeroDivisionError'
    print('Não é possivel dividir um numero por ZERO!')
except KeyboardInterrupt:  # Se de erro no 'try', executa esse except, caso a Exceção for 'KeyboardInterrupt'
    print('O usuario preferiu nao informar os dados!')
except Exception as erro:  # Se de erro no 'try' e nenhum dos 'except' anteriores forem executados, executa esse except, guardando informação na variavel 'erro'
    print(f'O erro encontrado foi {erro.__class__}')
else:  # Se caso nao der nenhuma exceção e nenhum except for exucutado, executa-se o 'else', ou seja, se deu certo o 'try' vem pro else
    print(f'O resultado foi {r:.2f}')
finally:  # Executa de qualquer maneira, dando alguma exceção ou nao, de qualquer forma o 'finally' é executado
    print('Volte sempre! Muito Obrigado!')
