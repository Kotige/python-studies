texto = 'Python'


# O for quer receber algo que seja iterável, como é o caso das str.


for letra in texto:
    print(letra)

"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(5, 10, 2)

for numero in numeros:
    print(numero)


# continue, break, else, etc também funcionam com o for