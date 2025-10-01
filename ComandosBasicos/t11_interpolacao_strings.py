"""
Interpolação básica de strings
s -string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Vitor'
preco = 1000.987
variavel = '%s, o preço é R$ %.2f.' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %X' %(1384000, 1384000)) # converte o número para hexadecimal. (Pode usar x também.)