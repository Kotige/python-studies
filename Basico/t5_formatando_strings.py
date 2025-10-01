nome = 'Vitor Barra'
altura = 1.80
peso = 104.50
imc = peso / altura **2
#
#f no começo da string possibilita usar variáveis dentro das strings.
print(f'{nome} tem {altura}m, pesa {peso}kg e seu IMC é {imc:.2f}.')
#o .2f limita a quantidade de casa decimais a 2.
#
#
# Uma outra maneira de formatar coisas é utilizando a função format().
a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a, b, c)
#
print(formato)