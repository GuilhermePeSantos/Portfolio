x = str(input('CPF:')).strip()
print('{}{}.{}.{}-{}{}'.format('\033[1;97m', x[:3], x[3:6], x[6:9], x[9:11], '\033[m'))
