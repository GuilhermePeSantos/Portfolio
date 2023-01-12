lista = [5, 3, 2, 7, 9, 1]
valores = list(range(4, 11))  # Cria uma lista no intervalo de 4, 5, 6, 7, 8, 9, 10 ignorando o ultimo valor (11)
lista.append(10)  # Cria mais uma celula e adiciona o valor no final da lista
lista.insert(0, 4)
len(lista)  # Mostra o tamanho da lista

#formas de deletar valores em listas
del lista[0]  # Deleto de acordo com a CELULA
lista.pop()  # Se nao colocar valor, ele remove o ultimo da lista
lista.pop(0)   # Deleto de acordo com a CELULA
lista.remove(9)   # Deleto de acordo com o VALOR

# Para limpar uma lista
lista.clear()

#Formas de ordenar lista
lista.sort()  # Ordena de forma CRESCENTE (Modifica o objeto lista, modificando a original)
sorted(lista)  # Ordena de forma CRESCENTE (Cria uma nova lista de forma crescente, sem modificar a original)
lista.sort(reverse=True)  # Ordena de forma DECRESCENTE

for c, v in enumerate(lista):
    print(f'Na posicao {c} encontrei o valor {v}')

# Criar lista com definir valores
lista = list()
lista = []

# Ler valores pelo teclado
for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista[1])

a = [3, 4, 5, 6, 7]
b = a  # Cria uma ligação entre as listas
b = a[:]  # b recebe uma copia da lista a

# Listas dentro de Listas
teste = list()
usuario = ['Guilherme', 18]
teste.append(usuario[:])
usuario[0] = 'Maria'
usuario[1] = 19
teste.append(usuario[:])

galera = [['Guilherme', 18], ['Gabriel', 17], ['Maria', 15], ['Sergio', 20]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')
