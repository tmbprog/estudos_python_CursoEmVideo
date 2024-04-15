# Gerador de palpites na MegaSena. O usuários escolhe quantos palpites quer
from random import randint
from time import sleep
'''
lista = []
n = int(input('Quantas jogos você deseja fazer? '))
for j in range(1, n+1):
    for c in range(0,6): #constrói uma lista com 6 elementos aleatórios
        num = randint(1,60)
        lista.append(num)
        for ele in lista: #verifica se não há elementos repetidos
            if lista.count(ele) > 1: #caso o número de algum elemento for maior do que 1 é sinal de que ele se repete
                lista.remove(ele) #removo o elemento repetido
                new = randint(0, 60) #gera um novo elemento para substituir os repetidos
                lista.append(new)
    lista.sort()
    print(f'Jogo {j}: {lista}')
    sleep(1)
    lista.clear()
print('Boa Sorte!!!')'''
#solução do Guanabara para não repetir números:
from random import randint
lista = []
cont = 0
while True:
    num = randint(1,60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
            break
print(lista)

#solução minimanista encontrada nos comentários
'''from random import sample
for n in range(int(input('Quantos palpites gerar?'))):
    print(sorted(sample(range(1,61),6)))'''

