# Ler o peso de 5 pessoas e ao final mostrar o maior e o menor
list = [] #cria uma lista vazia
for c in range(1,6):
    peso = float(input(f'Peso em kg da {c}ª pessoa: '))
    list = list + [peso] #adiciona os valores de peso na lista
print(f'O maior peso foi {max(list)}Kg') #valor máximo
print(f'O menor peso foi {min(list)}Kg') #valor mínimo
