pessoas = {'nome': 'Guiherme', 'idade': 18, 'sexo': 'M'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.items())  # Printa os ITENS do dicionario, as CHAVES(KEYS) e os VALORES(VALUES)
print(pessoas.keys())  # Printa as CHAVES(KEYS), as celulas do dicionario, nesse caso 'nome', 'idade', 'sexo'
print(pessoas.values())  # Printa os VALORES do dicionario, nesse caso 'Guilherme', '18', 'M'
del pessoas['sexo']

for k, v in pessoas.items():  # k são armazenados as KEYS, e v são armazenados os VALORES | Assemelha ao enumerate das listas e tuplas
    print(f'{k} = {v}')

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

pessoas['nome'] = 'Leandro'  # troca o nome 'Guilherme' por 'Leandro'
pessoas['peso'] = 59  # Como nao tem a chave 'peso' no dicionario ele adiciona 'peso' = 59, NAO PRECISA DE USAR O APPEND
pessoas['sexo'] = 'M'  # Adicionou 'sexo' novamente, NAO PRECISA DE USAR O APPEND
print(pessoas.items())


# Dicionario dentro de lista
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['uf'])
print(brasil[0]['sigla'])
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')

brasil.append(estado1.copy())  # Para copiar dicionarios tem um metodo interno copy(), fatiamento não funciona [:]
