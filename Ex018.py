# Lê um ângulo qualquer e retorna sen, cos e tang
from math import cos, tan, sin, radians, sqrt
a = float(input('Digite um ângulo: '))
b = radians(a)
print(f'Para {a} temos:\n Seno: {sin(b):.2f};\n Cosseno: {cos(b):.2f};\n Tangente: {tan(b):.2f}')
