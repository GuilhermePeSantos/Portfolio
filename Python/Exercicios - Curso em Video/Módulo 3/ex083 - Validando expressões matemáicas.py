analise = list()
expressao = str(input('Digite a expressao: '))
for i in range(0, len(expressao)):
    analise.append(expressao[i])
if analise.count('(') == analise.count(')'):
    print('A expressao esta \033[32;1mCORRETA\033[m')
else:
    print('A expressao esta \033[31;1mINCORRETA\033[m')

'''if expressao.count('(') == expressao.count(')'):
    print('A expressao esta \033[32;1mCORRETA\033[m')
else:
    print('A expressao esta \033[31;1mINCORRETA\033[m')'''