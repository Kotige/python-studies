"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
--- Se a letra digitada estiver na palavra secreta, exiba a letra.
--- Se a letra não estiver na palavra digitada, exiba *.
- Faça a contagem de tentativas do seu usuário.
"""
palavra_secreta = 'peixe'
letras_acertadas = ''
palavra_jogo = '*' * len(palavra_secreta)
# print(palavra_jogo)

tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    if len(letra_digitada) > 1 or letra_digitada == ' ':
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)