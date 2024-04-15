# Programa mostra o preço de um produto com 5% de desconto
p = float(input('Valor do produto: R$'))
print(f'Com desconto de 5% sai por: \033[1mR${p - p*5/100:.2f}')