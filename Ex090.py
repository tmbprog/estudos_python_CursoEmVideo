#Ler nome e média do aluno, guardando a situação (mínima: 7.0) em um dicionário.
#Mostar o conteúdo na tela
dados = {}
dados['nome'] = str(input('Nome do aluno: '))
dados['media'] = float(input('Média: '))
if dados['media'] <= 7:
    dados['situação'] = 'Reprovado(a)!'.upper()
else:
    dados['situação'] = 'Aprovado(a)!'.upper()
for k, v in dados.items():
    print(f'O {k} é igual a {v}')
