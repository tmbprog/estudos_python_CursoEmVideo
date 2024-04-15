# Cálculo da hipotenusa
from math import hypot
a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa é: \033[41m{hypot(a,b):.2f}\033[m')