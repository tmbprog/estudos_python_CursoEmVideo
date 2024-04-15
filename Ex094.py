#Ler nome, sexo e idade de várias pessoas. Guardar tudo num dict e todos os dicts numa lista.
#Mostrar: a) n de pessoas cadastradas, b) média de idade, c) lista todas as mulheres, d)pessoas com idade acima da média
cadastro = []
cont = soma_id =0
listF = []
while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: '))
    cont += 1
    soma_id += idade
    media = soma_id/cont
    if sexo in 'Ff':
        listF += [nome]
    dados ={'nome': nome, 'idade': idade, 'sexo': sexo}
    cadastro.append(dados.copy())
    op = str(input('Deseja continuar[S/N]? '))
    if op in 'Nn':
        break
print('=='*30)
print(f'O número de pessoas cadastradas foi {cont}.')
print(f'A média de idade do grupo é {media}')
print(f'As mulheres cadastradas foram: {listF}')
print('Pessoas com idade acima da média: ')
for c in range(len(cadastro)):
    if cadastro[c]['idade'] > media:
        print(cadastro[c])
print('<< Encerrado >>')
# outro modo para as mulheres
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} <-- mulheres cadastradas')