#contador
'''print('=='*30)
print('Contagem de 1 até 10 de 1 em 1:')
for a in range(1, 11):
    print(a, end= ' ')
print('FIM!')
print('=='*30)
print('Contagem de 10 até 0 de 2 em 2:')
for b in range(10, -2, -2):
    print(b, end= ' ')
print('FIM!')
print('=='*30)
print('Agora personalize a contagem!')''' #desnecessário!
#Obs. Solução mais simples usando o while e o teste lógico no início da função:
def contador(i, f, p):
    if p < 0:
        p *= -1 #transforma p em positivo
    if p == 0:
        p = 1 #assume o valor de 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end= ' ')
            c += p
        print('Fim!')
    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ')
            c -= p
        print('Fim!')
'''def contador(inicio, fim, passo):
    print('==' * 30)
    if fim > inicio and passo != 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim+passo, passo):
            print(c, end= ' ')
        print('Fim!')
    if fim < inicio and passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim-passo, - passo):
            print(c, end= ' ')
        print('Fim!')
    if fim < inicio and passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim+passo, passo):
            print(c, end= ' ')
        print('Fim!')
    if fim < inicio and passo == 0:
        print(f'Contagem de {inicio} até {fim} de 1 em 1')
        for c in range(inicio, fim-1, passo-1):
            print(c, end= ' ')
        print('Fim!')
    if fim > inicio and passo == 0:
        print(f'Contagem de {inicio} até {fim} de 1 em 1')
        for c in range(inicio, fim+1, passo+1):
            print(c, end= ' ')
        print('Fim!')'''# solução original

contador (1, 10, 1)
contador(10, 0, 2)
print('Agora personalize a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
