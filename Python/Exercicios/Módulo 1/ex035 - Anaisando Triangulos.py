R1 = float(input('Digite o primeiro valor:'))
R2 = float(input('Digite o segundo valor:'))
R3 = float(input('Digite o terceiro valor:'))
#Verificando o maior valor e somando os menores
maior = R1
soma = R2 + R3
if R2 > R1 and R2 > R3:
    maior = R2
    soma = R3 + R1
if R3 > R1 and R3 > R2:
    maior = R3
    soma = R2 + R1

if soma > maior:
    print('Essas retas PODEM formar um triangulo')
else:
    print('Essas retas NAO PODEM formar um triangulo')

'''OUTRA FORMA
if R1 < R2 + R3 and R2 < R3 + R1 and R3 < R1 + R2:
    print('Essas retas PODEM formar um triangulo!')
else:
    print('Essas retas NÃO PODEM formar um triangulo!')'''


