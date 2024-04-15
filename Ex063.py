#ler um n inteiro e mostre o n primeiros elementos de uma Sequência de Fibonacci. Ex: 0 1 1 2 3 5 8...
#é uma sequência que começando em 0 e 1, vai sempre somando os dois termos anteriores
n = int(input('Quantos termos da sequência de Fibonacci você deseja ver?'))
t1 = 0
t2 = 1
print(f'{t1}{t2}', end='->')
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3 #Com isso, na prática, o t3 vai se transformar em tn...
    cont += 1
    print(f'{t3}', end='->')
print('FIM')