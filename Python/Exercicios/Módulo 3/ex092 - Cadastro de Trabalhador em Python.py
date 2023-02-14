from datetime import date, datetime
trabalhador = dict()
trabalhador['Nome'] = str(input('NOME: '))
nascimento = int(input('ANO DE NASCIMENTO: '))
trabalhador['Idade'] = date.today().year - nascimento  # OU datetime.now().year - nascimento
trabalhador['CTPS'] = int(input('CARTEIRA DE TRABALHO (caso não tenha digite 0): '))
if trabalhador['CTPS'] != 0:
    trabalhador['AnoContratação'] = int(input('Digite o ano de contratação: '))
    trabalhador['Salario'] = float(input('Digite o salario: '))
    trabalhador['Aposentadoria'] = (trabalhador['AnoContratação'] + 35) - nascimento
print('-' * 40)
if trabalhador['CTPS'] != 0:
    print(f'NOME: {trabalhador["Nome"]}')
    print(f'IDADE: {trabalhador["Idade"]} anos')
    print(f'CARTEIRA DE TRABALHO: {trabalhador["CTPS"]}')
    print(f'ANO DE CONTRATAÇÃO: {trabalhador["AnoContratação"]}')
    print(f'SALÁRIO: R${trabalhador["Salario"]:.2f}')
    print(f'Idade de APOSENTADORIA: {trabalhador["Aposentadoria"]} anos')
else:
    print(f'NOME: {trabalhador["Nome"]}')
    print(f'IDADE: {trabalhador["Idade"]} anos')
    print(f'AINDA NAO POSSUI CARTEIRA DE TRABALHO(CTPS)')

for key, value in trabalhador.items():
    print(f'\t- {key} possui o valor {value}')
