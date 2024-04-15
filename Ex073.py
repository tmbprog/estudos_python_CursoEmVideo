#Tabela do brasileirão. a)lista de times; b) os quatro primeiros; c) os 4 últimos; d) em qual posição está a chape
times20 = ('Corinthians','Palmeiras','Santos','Grêmio', 'Cruzeiro','Flamengo','Vasco da Gama','Chapecoense','Atlético-MG',
           'Botafogo','Athletico-PR','Bahia','São Paulo','Fluminense','Sport','Vitória','Coritiba', 'Avaí', 'Ponte Preta',
           'Atlético-GO')
print(f'Times do Brasileirão 2017 por classificação na tabela:\n {times20}')
print('')
print(f'Os times que participaram do campeonato por ordem alfabédica:\n {sorted(times20)}')
print('')
print(f'O G5 do campeonato foi:\n {times20[0:4]}')
print('')
print(f'O Z4 foi: {times20[-4:]}')
print('')
print(f"A Chapecoense ficou em {times20.index('Chapecoense')+1}º lugar no campeonato")
