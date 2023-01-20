aluno = dict()
aluno['nome'] = str(input('NOME: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 >= aluno['media'] < 7:
    aluno['situacao'] = 'de Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print(f'O aluno {aluno["nome"]} ficou com {aluno["media"]} de media e esta {aluno["situacao"]}')
for k, v in aluno.items():
    print(f'{k} = {v}')
