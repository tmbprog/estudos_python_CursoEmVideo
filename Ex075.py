#Ler 4 valores, guardar na tupla e mostrar: a) quantas vezes aparece o 9, b)em qual posição foi digitado o 3, c)quais foram pares?
num = tuple(int(input(f'Digite o {c + 1}º numero: ')) for c in range(4)) #Técnica para por vários "inputs" numa tupla.
print(f'O número 9 aparece {num.count(9)} vezes na tupla')
if 3 not in num:
    print('O número 3 não consta na tupla')
else:
    pos3 = num.index(3)
    print(f'O número 3 aparece na posição {pos3} da tupla')
print('Números pares digitados: ', end='')
for par in num:
    if par%2 == 0:
        print(par, end= ' ')
