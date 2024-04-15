from random import randint
def sorteio(lista):
    for c in range(5):
        numeros.append(randint(1, 5))
    print(f'O números sorteados foram: {numeros}')

def somapar(lista):
    soma = 0
    for n in numeros:
        if n%2 == 0:
            soma += n
    print(f'A soma dos pares é {soma}.')

numeros = []
sorteio(numeros)
somapar(numeros)

