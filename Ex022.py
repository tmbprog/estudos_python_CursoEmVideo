# Ler um nome completo e mostrar: o nome em maúsculas, minúsculas, nº de letras total (sem espaço) e nº de letras do 1 nome
nome = str(input('Nome completo: ')).strip()
# o .strip() para eliminar todos os espaçoes inúteis antes e depois do string.
print(f'Nome em maúsculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')
nome2 = nome.split()
nome3 = ''.join(nome2)
print(f'Número de letras sem espaço: {len(nome3)}')
# A opção mais ecômica é usar len(nome) -nome.count(' ')
print(len(nome) - nome.count(' '))
print(f'Número de letras do primeiro nome: {len(nome2[0])}')
# Outra opção é nome.find(' ') i.e encontre o primeiro espaço (sabendo que a contagem inicia em 0, o primeiro espaço = n. de letras do nome)
print(nome.find(' '))