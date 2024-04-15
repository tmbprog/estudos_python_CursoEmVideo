#Cadastrar Idade e Sexo e mostrar. A) quantos > 18, B) Quantos H, C) quantas M < 20
Li = Ls = []
p18 = 0 #pessoas > 18
sh = s20 = 0
while True:
    print('Cadastrar Pessoa')
    idade = int(input('Idade: '))
    if idade > 18:
        p18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        sh += 1
    if sexo == 'F' and idade < 20:
        s20 += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    Ls += [sexo]
    if op == 'N':
        break
print(f'Pessoas com mais de 18 anos: {p18}')
print(f'Nº total de homens: {sh}')
print(f'Nº de Mulheres com menos 20 anos: {s20}')