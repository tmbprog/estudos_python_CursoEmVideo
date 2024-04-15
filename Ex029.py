#Programa que lê a velocidade do carro e aplica a multa. Velocidade máxima 80km/h. Multa: R$7,00 por Km
vc = float(input('Velocidade em Km/h:'))
vm = 80
multa = (vc-vm)*7.00
if vc >= vm:
    print(f'Você ultrapassou o limite de velocidade! Sua multa é: R${multa:.2f}')