# Programa que lê um número real e mostre na tela apenas sua porção inteira
from math import trunc
n = float(input ('Digite um número real:'))
print (f'O número \033[1m{n}\033[m tem a parte inteira \033[1m{trunc(n)}\033[m')

