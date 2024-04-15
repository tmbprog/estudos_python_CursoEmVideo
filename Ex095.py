#Aprimorar o 93 para vários jogadores
cadastro = {}
aproveitamento = []
cadastro_geral = []
tot = 0
while True:
    cadastro['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Número de partidas jogadas? '))
    for c in range(partidas):
        gols = int(input(f'Quantos gols {cadastro["nome"]} fez na {c+1}º partida: '))
        aproveitamento += [gols]
        tot += gols
    cadastro['aproveitamento'] = aproveitamento
    aproveitamento = []
    cadastro['total_de_gols'] = tot
    tot = 0
    cadastro_geral.append(cadastro.copy())
    op = str(input('Continuar[S/N]? '))
    if op in 'Nn':
        break
print('=='*30)
print(f'{"Cod. Nome"}{"Gols":>10}{" Total"}')
for c in range(len(cadastro_geral)):
    print(f'{c} {cadastro_geral[c]["nome"]:<10}{cadastro_geral[c]["aproveitamento"]}{cadastro_geral[c]["total_de_gols"]}')
print('=='*30)
while True:
    n = int(input('Saber os dados de qual jogador? '))
    if n not in range(0,len(cadastro_geral)) and n != 999:
        print('Erro! Jogador Inexistente! Tente novamente')
    if n == 999:
        break
    if n in range(0,len(cadastro_geral)):
        jogador = cadastro_geral[n]['aproveitamento']
        for pos, c in enumerate(jogador):
            print(f'=> O jogador {n} fez {c} gols no jogo{pos+1}')
print('<< Encerrado >>')
#Obs!
#Parava ver a tabulação de modo correto (alinhado) ver o vídeo novamente!
