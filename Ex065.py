#Ler vário n inteiros. Mostrar a média de todos os valores, maior e menor. O programa pergunta se o usuário quer ou não continuar.
resp = 'S'
s = cont = 0 #isso é permitido quando todas são = 0
list = []
while resp in 'Ss':
    n = int(input('Digite um número: '))
    s = s+n
    cont = cont+1
    list += [n]
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        print(f'A média dos valores digitados é {s/cont:.2f}')
        print(f'O maior valor digitado foi {max(list)}')
        print(f'O menor valor digitado foi {min(list)}')
    if resp != 'N' and resp != 'S':
        print('\033[31mComando inválido!')
