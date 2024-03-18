from time import sleep


def maior(* numeros):
    maior = 0
    print(f'Dos {len(numeros)} valores informados: ', end='')
    for i, v in enumerate(numeros):
        if i == 0 or v > maior:
            maior = v
        print(f'{v} ', end='')
        sleep(0.3)
    print(f', o MAIOR é {maior}')
    print('-' * 55)


# Programa Principal
maior(0, 4, 9, 2, 10, 15, 8, 6)
maior(19, 7)
maior(3)
maior(4, 8, 2, 9)
maior()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
