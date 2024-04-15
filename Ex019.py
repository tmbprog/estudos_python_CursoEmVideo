# Sorteio com nomes (4 alunos)
from random import choice
a1 = 'José'
a2 = 'Maria'
a3 = 'Ana'
a4 = 'João'
lista = [a1, a2, a3, a4]
print(f'{a1}, {a2}, {a3}, {a4}')
print(f' O aluno escolhido foi: {choice(lista)}')