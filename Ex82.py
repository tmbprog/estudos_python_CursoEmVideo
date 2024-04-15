#Ler vários números. Gravar na lista. Mostrar: a) todos, b) só os pares c) só os ímpares
listaT = []
listaP = []
listaI = []
while True:
    n = int(input('Digite um número: '))
    listaT.append(n)
    op = input('Continuar[S/N]? ')
    if op == 'N':
        break
print(f'A lista com todos os números digitados é: {listaT}')
for c in listaT:
    if c%2 == 0:
        listaP.append(c)
    else:
        listaI.append(c)
print(f'A lista só com os pares é: {listaP}')
print(f'A lista só com os ímpares é: {listaI}')
