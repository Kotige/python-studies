"""
Python = Linguagem de programação
Sua tipagem é dinâmica e forte. Significa que ele entende o tipo de informação
que está sendo passada para ele. Não há necessidade de informar o tipo de dado.
"""
#
#Strings (srt) = Textos que são colocados dentro de aspas. Pode ser colocado em
# aspas simples ou duplas. O importante é que as aspas abertas sejam as mesmas fechadas.
print('Isso é uma string')
print("Isso também é uma string")
# O escape \ ou r pode ser usado para evitar que o caractere seguinte seja interpretato. Exemplo:
print('Aqui está algo \"entre aspas\"')
print(r"Agora \'esse \' aqui que não será interpretato.")
#Esses fatores de escape podem complicar o código. Uma forma de simplificar, podemos fazer assim:
print('Agora eu posso usar as "aspas"')
#
#
# Números do tipo int e float.
# Int são números inteiros. Exemplo:
print(12, 1, -50, 232, 0)
#Float são números de pontos flutuantes. Exemplo:
print(22.6, -19.67, 0.0) #Sempre se utiliza o ponto (.) para separar a parte inteira das casas decimais.
#
#
# A classe type mostra o tipo de dado em Python. Exemplos:
print(type('Eu sou uma string.')) #retorna str
print(type(12)) #retorna int
print(type(22.6)) #retorna float
#
#
# Tipo de dado boolean (bool)
# É um tipo de dado que aceita apenas dois valores: True e False. 
# São mais utilizados em combinação com operadores lógicos.
# Exemplo:
print(True, False)
print(type(True), type(False))
# Os tipos de dados primitivos podem ser convertidos entre si usando
# as classes int(), srt(), bool(), float(). Devido à sua tipagem forte,
# o python fará as conversões somente se forem possíveis.
# Exemplo:
print(int('1'), type(int('1')))