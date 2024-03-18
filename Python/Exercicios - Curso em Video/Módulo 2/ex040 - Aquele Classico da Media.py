nota1 = float(input('Digite sua PRIMEIRA nota:'))
nota2 = float(input('Digite sua SEGUNDA nota:'))
media = (nota1 + nota2) / 2

from time import sleep
print('\033[1;34mPROCESSANDO...\033[m')
sleep(2)

if media < 5:
    print('\n\033[1;31mREPROVADO\033[m | Nota: {:.1f}'.format(media))
elif media >= 5 and media < 7:
    print('\n\033[1;33mRECUPERAÇÃO\033[m | Nota: {:.1f}'.format(media))
else:
    print('\n\033[1;32mAPROVADO\033[m | Nota: {:.1f}'.format(media))
