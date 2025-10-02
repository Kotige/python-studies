"""
Repetições
while
Executa uma ação enquanto uam condição for verdadeira
break -> finaliza um laço em determinado momento mesmo se a condição continuar verdadeira
Exemplo de aplicação:
"""
contador = 0

while contador < 20:
    contador += 1

    if contador == 6:
        continue  # continua o código pulando o 6.

    print(contador)

    if contador ==40:
        break

print('Acabou')

"""
Outros operadores de atribuição:
Além do += que usei acima, existem outros:
-=, *=, /=, //=, **= e %=
"""