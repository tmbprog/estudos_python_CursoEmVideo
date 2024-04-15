#Jogar par ou ímpar com o PC. Jogo interrompindo quando o perder. Mostrar total de vitórias consecutivas.
from random import randint
c = 0
while True:
    npc = randint(0,10)
    player = str(input('Você quer [P]par ou [I]ímpar?')).strip().upper()[0]
    nplayer = int(input('Escolha um número entre 0 e 10: '))
    s = npc + nplayer
    c += 1
    if player not in 'PI':
        print('\033[31mComando Inválido. Tente de novo!\033[m')
    if player == 'I' and s%2 != 0:
        print(f'{nplayer}(vc) + {npc}(pc) é {s}. \nDeu ímpar! Você venceu!!!''')
    elif player == 'I' and s%2 == 0:
        print(f'{npc}(pc) + {nplayer}(vc) é {s}. \nDeu par! Você perdeu.')
        print(f'Total de vitórias: {c - 1}')
        break
    if player == 'P' and s%2 == 0:
        print(f'{nplayer}(vc) + {npc}(pc) é {s}. \nDeu par! Você venceu!!!''')
    elif player == 'P' and s%2 != 0:
        print(f'{npc}(pc) + {nplayer}(vc) é {s}. \nDeu ímpar! Você perdeu.')
        print(f'Total de vitórias: {c - 1}')
        break