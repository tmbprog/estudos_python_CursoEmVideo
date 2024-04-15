def title(escreva):
    linha = '~' * (len(escreva) + 4)
    print(linha)
    print(f'  {escreva}')
    print(linha)
while True:
    title(escreva = str(input('Escreva uma palavra ou frase qualquer: ')))
    op = input('Sair? ')
    if op in 'Ss':
        break
