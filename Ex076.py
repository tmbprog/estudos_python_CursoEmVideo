#tupla com nomes e preços dos produtos na seq. Mostar listagem de preços organizando dados em forma TABULAR
tupla = ('Estojo',5.00, 'Caneta', 3.50, 'Lápis', 1.50, 'Borracha', 0.50, 'Caderno', 10.00,)
print(f"{'=='*5} Lista de compras {'=='*5}")
for itens in range(0, len(tupla),2):
    print(f'{tupla[itens]:.<30}R${tupla[itens+1]:7.2f}')
