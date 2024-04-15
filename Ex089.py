#Ler nome e duas notas de vários alunos e guarde tudo dentro de uma lista composta
# Mostar: boletim com a média de cada aluno e que permita ao usuário mostrar as notas de cada aluno
'''boletim = []
dados = [[],[]]
while True:
    nome = input('Nome: ')
    dados.insert(0,nome)
    nota1 = float(input('Nota 1: '))
    dados[1].insert(0, nota1)
    nota2 = float(input('Nota 2: '))
    dados[1].insert(1,nota2)
    media = (nota1+nota2)/2
    dados[2].insert(0,media)
    boletim.append(dados[:])
    dados = [[], []]
    op = input('Continuar[S/N]')
    if op in 'Nn':
        break
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
for c in range(len(boletim)):
    print(f'{c:<4}{boletim[c][0]:<10}{boletim[c][2][0]:>8}')
n = 0
while n != 999:
    n = int(input('Digite o nº do aluno que deseja saber a nota (ou 999 para sair): '))
    if n != 999:
        print(boletim[n][1])'''
#Resolução do Professor
ficha = []
while True:
    nome = str(input('Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    #Atenção! Não esquecer dessa possibilidade de montar a estrutura da lista com as variáves dentro do append
    resp = str(input('Quer continuar[S/N]?'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 para interromper):'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Volte Sempre!!')
