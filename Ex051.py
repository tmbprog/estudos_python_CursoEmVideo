#Ler o primeiro termo e a razão de uma PA e no final mostre os 10 primeiros termos dessa PA
a1 = int(input('O primeiro termo da P. A é: '))
r = int(input('A razão da P. A é: '))
a10 = a1 + (10-1)*r
s = 0
print('Os 10 primeiros termos da P.A são:')
for c in range(a1, a10+1, r):
    s = s + c
    print(c, end=' ')
print(f'\nA soma dos 10 primeiros termos da progressão é: {s}')