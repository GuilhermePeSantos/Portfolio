sexo = str(input('Digite seu sexo [F/M]:')).upper().strip()
while sexo != 'F' and sexo != 'M': # OU while sexo not in 'MmFf':
    print('\033[31mLETRA INVALIDA!\033[m')
    sexo = str(input('Digite seu sexo [F/M]')).upper().strip()

if sexo == 'M':
    print('\nSexo MASCULINO cadastrado com SUCESSO')
else:
    print('\nSexo FEMININO cadastrado com SUCESSO')
