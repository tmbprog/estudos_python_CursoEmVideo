# Ler um nome completo e mostrar/selecionar apenas o primeiro e o último
nome = input('Nome Completo: ')
nome2 = nome.split()
print(f'Primeiro nome: {nome2[0]}')
print(f"Último nome: {nome2[len(nome2)-1]}")