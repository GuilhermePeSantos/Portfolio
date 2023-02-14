def notas(*num, sit=False):
    """
        -> Funçõo que analisa notas
    :param num: Recebe varias notas
    :param sit: False(Não mostra a situação da turma), True(Mostra a situação da turma)
    :return: Retorna um dicionario com todas as informações
    """
    turma = dict()
    qtd_notas = len(num)
    turma['QTD Notas'] = qtd_notas
    maior = menor = 0
    for i, v in enumerate(num):
        if i == 0 or v > maior:
            maior = v
        if i == 0 or v < menor:
            menor = v
    turma['Maior Nota'] = maior  # Ou usar a função max(num)
    turma['Menor Nota'] = menor  # Ou usar a função min(num)
    media_turma = sum(num) / len(num)
    turma['Media'] = media_turma
    if sit:
        if media_turma < 5:
            turma['Situção'] = 'Ruim'
        elif 5 <= media_turma <= 7:
            turma['Situação'] = 'Boa'
        elif media_turma > 7:
            turma['Situação'] = 'Ótima'
    return turma


# Programa Principal
#resposta = notas(10, 8, 3.5, 7.2, 10, 7, 10, sit=True)
resposta = notas(5.5, 9.5, 10, 6.5, sit=True)
print('-' * 40)
for k, v in resposta.items():
    if k == 'Media':
        print(f'{k} = {v:.2f}')
    else:
        print(f'{k} = {v}')
help(notas)
