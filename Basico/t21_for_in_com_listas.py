"""
for in com listas
"""

lista = ['Maria', 'João', 'Luiz', 'Deva']

for nome in lista:
    print(nome)

"""
Exercício: Exibir os índices de cada elemento da lista
"""

i = 0
print('Índice ........... Elemento')
while i <= len(lista) - 1:
    print(f'{i} ................ {lista[i]}')
    i += 1