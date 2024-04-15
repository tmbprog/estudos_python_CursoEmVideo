#Aproveitamento de jogador. Recebe: nome, partidas [gols/partida numa lista].
# Tudo guardado no dict, incluindo total de gols
cadastro = {}
aproveitamento = []
tot = 0
cadastro['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Número de partidas jogadas? '))
for c in range(partidas):
    gols = int(input(f'Quantos gols {cadastro["nome"]} fez na {c+1}º partida: '))
    aproveitamento += [gols]
    tot += gols
cadastro['aproveitamento'] = aproveitamento[:]
cadastro['total_de_gols'] = tot
print('=='*30)
print(cadastro)
print('=='*30)
for k, v in cadastro.items():
    print(f'O campo {k} tem valor {v}')
print('=='*30)
print(f'O jogador {cadastro["nome"]} fez {partidas} partidas')
for c in range(partidas):
    print(f'    =>Na partida {c+1} fez {aproveitamento[c]}')
print(f'Foi um total de {tot} gols')
