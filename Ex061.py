#refazer o 51 usando o while
a1 = int(input('O primeiro termo da P. A é: '))
r = int(input('A razão da P. A é: '))
n = a1
cont = 1
print('Os dez primeiros termos são: ')
while cont <= 10:
    print(f'{n}', end=' ')
    n = n + r
    cont = cont + 1
