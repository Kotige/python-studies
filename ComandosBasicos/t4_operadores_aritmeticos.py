#
adicao = 10 + 10  # O operador + pode ser usado para concatenar strings.
print("Adição", adicao)
#
subtracao = 10 - 5
print("Subtração", subtracao)
#
multiplicacao = 10 * 10  # O operador * pode fazer repetição com strings. Ex: 'A' * 10 == AAAAAAAAAA
print("Multiplicação", multiplicacao)
#
divisao = 10 / 2.2  # sempre retorna float
print("Divisão", divisao)
#
divisao_inteira = 10 // 2.2
print("Divisão inteira", divisao_inteira)
#
resto_da_divisao = 10 % 2
print("Resto da divisão", resto_da_divisao)
#
exponenciacao = 2 ** 10
print("Exponenciação", exponenciacao)
#
# Precedência dos Operadores
# Sem precedência:
conta_1 = 1 + 1 ** 5 + 5  # == 7
# Com precedência:
conta_2 = (1 + 1) ** (5+5)  # == 1024 