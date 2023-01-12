nomes = ('Guilherme', 'Julia', 'Francisco', 'Pio', 10,  'Maria', 'Guilherme', 20, 30)
sobrenomes = ('Santos', 'Silva', 'Moreira', 'Albuquerque', 40, 50, 60)
x = (1.5, 2.2, 3.7, 8.9)
Tm = len(nomes)
for i in nomes:  # i referencia a Tupla nomes
    print(i)

for i in range(0, Tm):
    print(nomes[i])
    
for i, ref in enumerate(nomes):  # ref referencia a Tupla e i referencia a numeração
    print(ref)
    print(i)

print(nomes[-3:])  # Printa a Tupla a partir da posição -3 até o final (fatiamento)
print(sorted(nomes)) # Mostra os valores em ordem alfabetica e os numeros em ordem crescente
print(nomes.count('Guilherme'))  # Conta quantos 'Guilherme' tem na tupla
print(nomes.index('Maria'))  # Mostra a celula em que 'Maria' esta
print(nomes.index('Guilherme', 1))  # Mostra a posição em que 'Guilherme' esta a partir da posição 1
print(nomes + sobrenomes)  # Concatena as Tuplas
print(f'Maior: {max(x)}')  # Mostra o MAIOR numero dentro da tupla
print(f'Menor: {min(x)}')  # Mostra o MENOR numero dentro da tupla
del nomes  # Deleta a tupla
