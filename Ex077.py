#Tupla com várias palavras. Mostrar as vogais. Ex da saída: Na palavra Aprender temos a e e
tupla = ('aprender','beber','comer','decorar', 'falar', 'programar', 'curso', 'futuro')

#Resolução Guanabara. Muito mais limpa!

for palavras in tupla:
    print(f'\nAs vogais em \033[1m{palavras}\033[m são:', end=' ')
    for vogais in palavras:
        if vogais in 'aeiou':
            print(vogais, end= ' ')



'''print(len(tupla))
for n in range(0,len(tupla)):
   a = tupla[n].count('a')*'a '
   e = tupla[n].count('e')*'e '
   i = tupla[n].count('i')*'i '
   o = tupla[n].count('o')*'o '
   u = tupla[n].count('u')*'u '
   print(f'As vogais em \033[1m{tupla[n]}\033[m são:',end=' ')
   print(a, e, i, o, u)'''
