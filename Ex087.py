#com a mesma matriz do 86, mostre: a) soma dos pares, b)soma da terceira coluna, c) maior valor da segunda linha
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
soma = soma3 = 0
for l in range(0,3): #linhas
    for c in range(0,3): #colunas
        matriz[l][c] = int(input(f'Valor para [{l} {c}]: '))
        if matriz[l][c]%2 == 0:
            soma += matriz[l][c]
#A segunda estrutura for é para imprimir os elementos de forma individual
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end= ' ')
    print() #para fazer com que fique uma em cima das outras

maior2 = max(matriz[1])
print(f'A soma dos número pares: {soma}')
for l in range(0,3):
    soma3 += matriz[l][2]
print(f'Soma da terceira coluna: {soma3}')
print(f'Maior valor da segunda linha: {maior2}')