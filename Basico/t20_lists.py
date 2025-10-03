"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo.
Conhecimentos reutilizáveis - índices e fatiamento.
Métodos úteis: append, insert, pop, del, clear, exted, +
"""

lista = [123, True, 'Vitor Fernandes', 1.2, []]
print(lista)
print(lista[2], type(lista[2])) # os métodos de string funcionam mesmo em str dentro de uma lista
lista[-2] = 'Maria'  # muda o elemento da lista.
print(lista)


# Métodos de list
lista2 = [10, 20, 30, 40]

lista2[2] = 300  # alteração de um elemento da lista

del lista2[2]  # apaga um elemento da lista (Não é muito eficiente em listas muito grandes).
print(lista2)

lista2.append(50) # adiciona um elemento no final da lista.
print(lista2)

lista2.pop() # remove o último elemento da lista (Sem argumento. Com argumento remove um elemento correspondente).
print(lista2)

lista.clear()  # limpa a lista
print(lista)

lista2.insert(1, 'Vitor') # insere um valor na posição desejada da lista.
print(lista2)

### Concatenação de listas

lista_a = [1, 2, 3]
lista_b = [True, 'Vitor', 31]
lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_b)  # leva todos os elementos da lista_b para a lista_a
print(lista_a)