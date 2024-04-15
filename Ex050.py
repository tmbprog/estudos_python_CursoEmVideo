#Ler seis números inteiros e mostrar a soma dos pares
soma = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}º número: '))
    if n%2 == 0:
        soma = soma + n
print(f'A soma dos números pares é: {soma}')
