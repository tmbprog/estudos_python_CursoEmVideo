# Ler o comprimento de 3 retas e dizer se formam um triângulo (Condição de existência de um triângulo)
a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))
x1 = a+b
x2 = a+c
x3 = b+c
#não seria necessário fazer as variáveis X
if a < x3 and b < x2 and c < x1:
    print('Estas retas podem formar um triângulo')
else:
    print('Estas retas não formam um triângulo')
