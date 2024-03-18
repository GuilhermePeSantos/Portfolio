num = int(input('Digite um numero:'))
x = int(input('\nDigite a opcao:'
              '\n1- Binario'
              '\n2- Octal'
              '\n3- Hexadecimal'))
if x == 1:
    conv = format(num, 'b')# forma de fazer a conversao SEM printar o prefixo 0b, 0o, 0x
                           # Há tambem a funcao bin(), oct(), hex() porem printa o prefixo do tipo 0b, 0o, 0x
    print('\nO numero {} em \033[1:32mBINARIO\033[m é {}'.format(num, conv))
elif x == 2:
    conv = format(num, 'o')
    print('\nO numero {} em \033[1;36mOCTAL\033[m é {}'.format(num, conv))
elif x == 3:
    conv = format(num, 'X')
    print('\nO numero {} em \033[1;35mHEXADECIMAL\033[m é {}'.format(num, conv))
else:
    print('\033[1;31m\nOpcao Invalida!\033[m')
