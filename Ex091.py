#4 jogadores lançam um dado. Guardar resultados num dicionário e mostrar o ranking(do maior ao menor)
from random import randint
from operator import itemgetter
from time import sleep
jogadores = {}
print('Valores sorteados: ')
for c in range(1,5):
    dado = randint(1,6)
    print(f'Jogador{c} tirou {dado}')
    jogadores[c] = dado
    sleep(1)
#é preciso criar uma outra variável, pois irá retornar lista com tupla
ordenado = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#A função 'sorted' recebe os ítens do dicionário e ordena de acordo com a chave ('key') escolhida, que pode ser
# o primeiro (0) ou o segundo (1) elementos das tuplas
# Passando o '1' para o itemgetter, vc ordenará o dicionário pelos valores.
print('======== RANKING ========')
for c in range(4):
    print(f' O {c+1}º lugar foi o Jogador{ordenado[c][0]} que tirou {ordenado[c][1]}')
    sleep(1)
