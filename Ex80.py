#Lista com 5 números que mostre um resultado em ordem sem usar o sort()
lista = []
c = 0
for c in range(1,6):
    n = int(input(f'Digite o {c}º número: '))
    if c == 1 or n > lista[-1]: #[-1] retorna o último número adicionado na lista
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        if n < min(lista):
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista')
        if n > min(lista):
            lista.insert(1, n)
            print('Acicionado na posição 1 da lista')
print(lista)

#Obs! A Solução do professor é diferente!