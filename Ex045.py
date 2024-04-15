#Jokenpô com o PC
from random import randint
from time import sleep
npc = randint(1,3)
print('Escolha PEDRA, PAPEL ou TESOURA:')
print(' [1]PEDRA \n [2]PAPEL\n [3]TESOURA')
p1 = int(input('Com qual você quer jogar? '))
print('JO')
sleep(1)
print('  KEN')
sleep(1)
print('     PÔ!')
sleep(1)
print('=-=-='*5)
if npc == 1 and p1 == 2:
    print('O pc escolheu pedra. \nPapel ganha pedra. \n \033[1mVocê ganhou!!!')
elif npc == 2 and p1 == 3:
    print('O pc escolheu papel. \nTesoura ganha papel. \n \033[1mVocê ganhou!!!')
elif npc == 3 and p1 == 1:
    print('O pc escolheu tesoura. \nPedra ganha tesoura. \n \033[1mVocê ganhou!!!')
elif p1 == 1 and npc == 2:
    print('O pc escolheu papel. \nPapel ganha pedra. \n \033[1mVocê perdeu!!!')
elif p1 == 2 and npc == 3:
    print('O pc escolheu tesoura. \nTesoura ganha papel. \n \033[1mVocê perdeu!!!')
elif p1 == 3 and npc == 1:
    print('O pc escolheu pedra. \nPedra ganha tesoura. \n \033[1mVocê perdeu!!!')
elif npc == p1:
    print('Ops! Foi um \033[1mempate\033[m. Tente de novo!')
print('\033[m=-=-='*5)
#Resolução professor
itens = ('0', 'pedra', 'papel', 'tesoura')
# o 0 foi colocado apenas pq a contagem começa em 0
print(f'O pc escolheu {itens[npc]}')