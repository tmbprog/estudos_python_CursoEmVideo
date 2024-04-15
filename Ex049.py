#Refazer o exercício 009 usando um laço de repetição
n = int(input('Digite um número inteiro:'))
print(f"A tabuada de \033[1m{n} \033[mé:\n{'=='*10}")
for c in range(1,11):
    tab = n*c
    print(f'{n}x{c}:{tab}')
print(f"{'=='*10}")
