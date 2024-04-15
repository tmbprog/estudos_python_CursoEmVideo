#Melhorar o jogo do exercício 28
import random
from time import sleep
npc = random.randint(0,5)
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Escolha um número entre 0 e 5:'))
    print('Processando...')
    sleep(1)
    cont += 1
    if jogador == npc:
        acertou = True
        print(f'\033[31mParabéns! Você acertou!\033[m')
        if cont == 1:
            print('E com apenas uma tentativa!')
        if cont > 1:
            print(f'Mas precicou de {cont} tentativas.')
    else:
        print('\033[31mVocê errou! Tente novamente!\033[m')



