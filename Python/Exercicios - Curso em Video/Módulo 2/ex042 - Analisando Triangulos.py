R1 = float(input('Digite a primeira reta:'))
R2 = float(input('Digite a segunda reta:'))
R3 = float(input('Digite a terceira reta:'))

maior = R1
soma = R2 + R3
if R2 > R1 and R2 > R3:
    maior = R2
    soma = R3 + R1
if R3 > R1 and R3 > R2:
    maior = R3
    soma = R2 + R1

if soma > maior:
    print('\nEssas retas formam um triangulo ', end='')
    if R1 == R2 and R1 == R3: #ou R1 == R2 == R3
        print('\033[1;32mEQUILÁTERO!\033[m')
    elif R1 == R2 or R1 == R3 or R2 == R3: #R1 != R2 != R3 != R1
        print('\033[1;36mISÓSCELES!\033[m')
    elif R1 != R2 and R1 != R3 and R2 != R3:
        print('\033[1;34mESCALENO!\033[m')
else:
    print('\nEssas retas \033[1;31mNAO PODEM\033[m formar um triangulo!')


