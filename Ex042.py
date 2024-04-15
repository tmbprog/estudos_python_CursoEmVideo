#Refazer o desafio 035 e dizer se o triângulo é equilátero, isóceles ou escaleno
a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))
x1 = a+b
x2 = a+c
x3 = b+c
#não seria necessário fazer as variáveis X
if a < x3 and b < x2 and c < x1:
    print('Estas retas podem formar um triângulo', end=' ')
    if a == b == c:
        print('equilátero.')
    elif a != b != c != a:
        print('escaleno.')
    else:
        print('isóceles.')
else:
    print('Estas retas não formam um triângulo')