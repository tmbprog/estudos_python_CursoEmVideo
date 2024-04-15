#Ler nome e preço de vários produtos. mostrar: a) total da compra, quantos produtos > 1000 e nome do produto mais barato
vt = cont = cont2 = 0
barato = ' ' #string vazia! capaz de receber qualquer "valor"
list = []
print('O que deseja comprar?')
while True:
    prod = str(input('Nome do produto: '))
    v = float(input('Valor: R$'))
    vt += v
    cont += 1
    list += [v]
    op = str(input('Deseja continuar comprando? [S/N]')). strip(). upper()[0]
    while op not in 'SN':
        op = str(input('Deseja continuar comprando? [S/N]')).strip().upper()[0]
    if v > 1000:
        cont2 += 1
    if v == min(list):
        barato = prod
    if op == 'N':
        break
print("")
print('\033[1mDados da compra:\033[m')
print(f'Quantidade de produtos: {cont}')
print(f'Valor total da compra: R${vt:.2f}')
print(f'Produtos custando mais de R$1000.00: {cont2}')
print(f'O produto mais barato foi: {barato}')
