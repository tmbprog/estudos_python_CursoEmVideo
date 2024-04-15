# Programa que lê metros (m) e converta para centímetros (cm) e milímetros (mm)
m = float(input('Metros:'))
print(f'Centímetros: \033[34m{m*100:.0f}cm\033[m \nMilímetros: \033[36m{m*1000:.0f}mm')