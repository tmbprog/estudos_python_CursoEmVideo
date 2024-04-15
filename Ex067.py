# Tabuada que fica executando até que seja solicitado um número negativo
c = 0
while True:
    n = int(input('Você quer ver a tabuada de qual número [digite n<0 para sair]?'))
    if n < 0:
        break
    for c in range (1,11):
        r = n*c
        print(f'{n}x{c}: {r}')
print('FIM')