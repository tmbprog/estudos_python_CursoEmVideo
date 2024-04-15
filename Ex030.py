#Dizer se o número é par ou ímpar
n = int(input('Digite um número: '))
par = n%2
if par == 0:
    print('Você digitou um número par!')
else:
    print('Você digitou um número ímpar!')