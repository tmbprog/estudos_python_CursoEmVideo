# Programa que lê a quantidade dólares que uma pessoa pode comprar com o que tem na carteira
r = float(input('Quantos reais você tem na carteira? \n'))
print(f'Com esse valor você pode comprar \033[1m{r/3.27:.2f}\033[m dólares')