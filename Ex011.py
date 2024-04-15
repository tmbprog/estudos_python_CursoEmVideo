# Programa que calcula a área de uma parede para saber quantos litros de tinta serão necessários para pintá-la. L:2m2
alt = float(input('Altura em metros:'))
l = float(input('Largura em metros:'))
a = alt*l
print (f'A área total da parede é: \033[31m{a}m²\033[m')
# Para fazer o m² = Alt+0178
t = a/2
print (f'A quantidade de tinta necessária será: \033[31m{t}L\033[m')