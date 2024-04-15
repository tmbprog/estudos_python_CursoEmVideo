#Computador escolhe um número entre 0 e 5. E o usuário tenta adivinhar!
import random
from time import sleep
# serve para fazer o pc esperar um pouco
npc = random.randint(0,5)
n = int(input('Escolha um número entre 0 e 5:'))
print('Processando...')
sleep(3)
if n == npc:
    print('Você acertou!!!')
else:
    print(f'Errrrouu!! O número correto era {npc}')