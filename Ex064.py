#Ler vários n inteiros. Só para com 999. Mostre quantos foram digitados e qual a soma entre eles.
num = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'A soma é {soma}')
#a estratégia de repetir o comando dentro e fora do laço serve para desconsiderar o 999
