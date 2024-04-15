# Programa que calcula o salário com 15% de aumento
s = float(input('Salário atual: R$'))
print(f'Novo salário: \033[34mR${s + (s*15/100):.2f}')
