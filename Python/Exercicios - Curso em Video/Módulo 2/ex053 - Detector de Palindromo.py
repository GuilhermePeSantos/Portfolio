#PALÍNDROMO: Frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.

frase = str(input('Digite uma frase:')).strip().upper()
list = frase.split() # coloca a frase em uma lista para remover os espaços
juncao = ''.join(list) # junta a lista sem os espaços
x = len(juncao) # conta o tanto de caracteres da frase sem contar os espaços
total = x
achou = 0

print('\n{} invertido é '.format(juncao), end='')
for y in range(total - 1, -1, -1): # escreve a frase digitada ao contrario
    print('{}'.format(juncao[y]), end='')

for i in range(0, x):
    if juncao[i] != juncao[total - 1]: # verifica se encontra alguma letra diferente
        achou = 1
    total = total - 1 # decrementa a variavel total

if achou == 0:
    print('\n{} \033[32mÉ um palíndromo'.format(frase))
else:
    print('\n{} \033[31mNÃO É um palíndromo'.format(frase))

'''
frase = str(input('Digite uma frase:')).strip().upper()
list = frase.split() 
junto = ''.join(list)
inverso = '' # ou inverso = juncao[::-1] e sem o for
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Nao é um palindromo')
'''