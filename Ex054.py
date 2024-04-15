#Programa que lê a idade de 7 pessoas e mostra quantas já atingiram a maior idade e quantas ainda não
cont = 0
cont2 = 0
for c in range(1,8):
    idade = int(input(f'Adicione a idade {c}: '))
    if idade >= 21:
        cont = cont+1
    elif idade < 21:
        cont2 = cont2+1
print(f'De acordo com as idades fornecidas, {cont} pessoas já atingiram a maior idade e {cont2} ainda não.')
