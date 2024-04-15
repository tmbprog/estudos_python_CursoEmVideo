#Ler nome e peso de várias pessoas. Agrupar numa lista.
# mostar: a) n de pessoas, b) listagem das mais pesadas c) listagem com as mais leves
lista = []
dados = []
cont = 0
while True:
    dados.append(str(input('Nome: ')))
    cont += 1
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    op = input('Continuar[S/N]?')
    if op in 'Nn':
        break
listaP = []
nmaior = []
nmenor = []
for p in lista:
    listaP.append(p[1])
for n in lista:
    if max(listaP) == n[1]:
        nmaior.append(n[0])
    elif min(listaP) == n[1]:
        nmenor.append(n[0])
print(f'Ao todo, você cadastou {cont} pessoas.')
print(f'O maior peso foi {max(listaP)}. Peso de {nmaior}.')
print(f'O menor peso foi {min(listaP)}. Peso de {nmenor}.')
