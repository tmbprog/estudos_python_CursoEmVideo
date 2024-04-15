#Criar uma matriz (3x3) preenchida com valores lidos pelos teclado#no final mostrar a matriz com formatação correta
lista = [[],[],[]]
for c in range(0,3):
    n = int(input(f'Digite um número para a [0 {c}]: '))
    lista[0].append(n)
for c in range(0, 3):
    n = int(input(f'Digite um número para a [1 {c}]: '))
    lista[1].append(n)
for c in range(0, 3):
    n = int(input(f'Digite um número para a [2 {c}]: '))
    lista[2].append(n)
for v in lista:
    print(v)