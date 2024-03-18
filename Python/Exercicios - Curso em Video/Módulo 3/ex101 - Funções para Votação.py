

def voto(anoNasc):
    from datetime import datetime
    """ HELP
        -> Função que calcula se ja pode votar
    :param anoNasc: Ano de Nascimento
    :return: Retorna uma String com a resposta 
    """
    idade = datetime.today().year - anoNasc
    if idade < 16:
       return f'\nCom {idade} anos, NÂO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'\nCom {idade} anos, VOTO OPCIONAL'
    elif 18 <= idade < 70:
        return f'\nCom {idade} anos, VOTO OBRIGATORIO'


# Programa Principal
nascimento = int(input('Digite o ano de seu nascimento: '))
print(voto(nascimento))
