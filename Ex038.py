#Comparar dois números e dar a respostas (maior, menor ou igual)
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
if n1 > n2:
    print('O primeiro valor digitado é o maior!')
elif n2>n1:
    print('O segundo valor digitado é o maior!')
else:
    print('Os valores são iguais!')