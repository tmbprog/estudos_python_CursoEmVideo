#Sortear 5 números aleatórios. Armazenar na tupla e mostrar o maior e o menor valor sorteados
from random import randint
nsort = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)) #colocou entre parêntesis e com vírgula vira tupla
print(type(nsort))
print(f'Os números sorteados foram: {nsort[0]} {nsort[1]} {nsort[2]} {nsort[3]} {nsort[4]}') #usando o for tbm
                                                        # dava para fazer os números sem a marcação de tupla
print(f'O menor número sorteado foi: {min(nsort)}')
print(f'O maior número sorteado foi: {max(nsort)}')
