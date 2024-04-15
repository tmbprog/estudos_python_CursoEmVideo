#Programa que lê um número qualquer e mostra o fatorial Ex: 5x5x4x3x2x1
n = int(input('Digite um número: '))
c = n #contador
f = 1 #fator de multiplicação
print(f'Calculando {n}!:', end='')
while c > 0:
    f = f*c
    c -= 1
    print(f'{c}', end=' ')
    print('x' if c>1 else ' = ', end=' ')
print(f'{f}')