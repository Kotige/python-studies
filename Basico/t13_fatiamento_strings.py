"""
Fatiamento de strings
012345678
Olá Mundo
-987654321

Fatiamento [i:f:p] [::] inicio - fim e passo
Obs.: a função len retorna a quantidade de caracteres da str
"""
variavel = "Olá mundo"
print(variavel[4:]) # o fim e o passo podem ser omitidos. Nesse caso ele vai até o final da str e segue passo 1.
print(variavel[0:4])
print(variavel[:5]) # o inicio também pode ser omitido, assim ele começa do primeiro caracter por padrão.
#
#função len
print(len(variavel)) # retorna a contagem de caracteres (tamanho da str).
#
print(variavel[0:len(variavel):2]) #agora com o passo 2 (também pode ser contado com números negativos. Inverte a str)