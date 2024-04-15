#ler 5 valores, guardar na lista e mostrar menor e maior valor com suas posições
lista = []
for v in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {v}: ')))
print(f'Os valores digitados foram {lista}')
print(f'O menor valor foi {min(lista)} n(a)s posição(ões)', end=' ')
for pos, c in enumerate(lista):
    if min(lista) == c:
        print(f'{pos}...', end=' ')
print(f'\nO maior valor foi {max(lista)} n(a)s posição(ões)', end=' ')
for pos, c in enumerate(lista):
    if max(lista) == c:
        print(f'{pos}...', end=' ')