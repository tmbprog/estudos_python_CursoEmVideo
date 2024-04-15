#função que recebe nome e n de gols de um jogador e retorna os valores
def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols no campeonato.')

nome = str(input('Nome do jogador: '))
gols = str(input('Gols: ')) #precisa ser string para aceitar vazio
if gols.isnumeric():
    int(gols) #converte para inteiros
else:
    gols = 0
if nome.strip() == '': #verificar se nada foi digitado
    ficha(g=gols)
else:
    ficha(nome, gols)
