"""
Operadores Lógicos
and (e), or (ou), not (não)



AND
todas as condições precisam ser verdadeiras
se qualquer valor for falso, a expressão inteira irá retornar falso
São considerados false: 0, 0.0, '', False
Também existe o tipo None, que é usado para representar um não-valor.
Exemplo:
"""
entrada = input('[E]ntrar ou [S]air.')
senha_digitada = input('Senha')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

"""
OR
Pelo menos uma das condições precisa ser verdadeira.
Se apenas uma das condições for verdadeira, a expressão inteira
será considerada verdadeira.
"""

"""
NOT (!=)
Usado para inverter expressões. Torna false o que é true e vice-versa.
"""
print(not True)  # False
print(not False)  # True