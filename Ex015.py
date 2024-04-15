# Aluguel de carro. Calcule o total a pagar sendo R$60 a diária e R$0.15 por Km.
d = int(input('Número de dias:'))
km = float(input('Km rodados:'))
print(f'Total a pagar: \033[31mR${d*60+km*0.15:.2f}')

