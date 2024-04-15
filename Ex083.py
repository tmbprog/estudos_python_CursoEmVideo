#Programa que analisa se os parêntesis na expresão matemática foram usados de modo correto
# Ex: ((a+b)*c) ->válida; ((a+b)*c))
# o número de '(' e ')' dentro da lista precisam ser iguais
exp = str(input('Digite a expressão: '))
pilha = []
for c in exp: #lembrando que toda string também é uma lista
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop() #Assim a pilha é zerada toda vez que um parêntesis encontra seu par
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

''' 
solução que parece que funciona, mas é prblemática:

exp = input('Digite uma expressão: ')
a = exp.count('(')
b = exp.count(')')
if a == b:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
'''
