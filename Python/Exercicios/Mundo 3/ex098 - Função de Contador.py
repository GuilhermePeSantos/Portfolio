from time import sleep


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} ate {fim} ', end='')
    if inicio > fim:  # Contagem DECRESCENTE
        fim -= 1
        if passo == 0:
            passo = -1
        if passo > 0:
            passo *= -1

        print(f'de {passo * -1} em {passo * -1}')
    if inicio < fim:  # Contagem CRESCENTE
        fim += 1
        if passo == 0:
            passo = 1
        if passo < 0:
            passo *= -1
        print(f'de {passo} em {passo}')
    for i in range(inicio, fim, passo):
        print(f'{i} ', end='', flush=True)  # flush=True serve para não ativar o buffer de tela
        sleep(0.4)
    print('...')
    print('-' * 40)


# Programa Principal
contador(1, 10, 1)
contador(10, 0, -2)
print('Personalize sua propria contagem: ')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
contador(inicio, fim, passo)


# Outra solução
'''def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(0.5)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.5)
            cont += p
            print('...')
        else:
            cont = i
            while cont >= f:
                print(f'{cont} ', end='', flush=False)
                cont -= p
            print('...')'''
