"""
Formatação básica de strings
s -- string
d - int
f - float
.<numero de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex.: 0 > -100, .1f
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #adiciona os caracteres faltantes de acordo com a quantidade especificada
print(f'{variavel: <10}')
