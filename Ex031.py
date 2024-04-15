# Custo da Viagem. Gasolina 0.50 até 200km. 0.45 acima de 200.
d = float(input('Sua viagem será de quantos quilômetros? '))
v1 = float(d*0.5)
v2 = float(d*0.45)
if d <= 200:
    print(f'sua viagem custará: R${v1:.2f}')
else:
    print(f'Sua viagem custará: R${v2:.2f}')
# Forma simplifica
preço = d*0.50 if d <= 200 else d*0.45
print(preço)