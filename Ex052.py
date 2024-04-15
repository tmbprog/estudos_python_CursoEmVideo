#Ler um n int e dizer se é ou não primo
num = int(input('Digite um número inteiro: '))
tot = 0 #contador para caso o número seja divisível
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.', end=' ')
if tot == 2:
    print('Logo, é primo.')
else:
    print('Logo, não é primo.')