frase = str(input('Digite uma frase:')).strip()
print('Qnts vezes aparece a letra A: {}'.format(frase.upper().count('A')))
print('Posição da primeira letra A: {}'.format(frase.upper().find('A') + 1))
print('A posição da ultima letra A é {}'.format(frase.upper().rfind('A') + 1))
