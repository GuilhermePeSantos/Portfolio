n = int(input('Digite a quantidade de termos que deseja mostrar: '))
pri = 0
seg = 1
i = 3
print('{} -> {} '.format(pri, seg), end='')
while i <= n:
    terc = pri + seg
    print('-> {} '.format(terc), end='')
    pri = seg
    seg = terc
    i += 1
print('...')
