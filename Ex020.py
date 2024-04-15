#Sortear a ordem de apresentação. Ler o nome de 4 alunos e mostrar a ordem sorteada.
from random import choices, shuffle, sample
a1 = 'Ricardo'
a2 = 'Júlia'
a3 = 'Carlos'
a4 = 'João'
lista = [a1, a2, a3, a4]
# Outra maneira de embaralhar a lista é pelo shuffle(lista). Mas essa opção não funciona dentro do print.
print (f'Alunos: {a1}, {a2}, {a3}, {a4}')
print (f'Ordem de apresentação: {sample(lista, 4)}')
# O número do sample pode ser qualquer um menor que 4. Elepoderia, por exemplo, escolher 2 de 4, 3 de 4...