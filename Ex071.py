#Caixa eletrônico. Pergunta o valor e informa as celular (50, 20, 10 e 1)
saque = int(input('Quanto você quer sacar? R$ '))
c1 = saque // 50 #divisão por inteiro
ca = saque%50 #resto
print(f'Total de cédulas de R$50: {c1}')
if ca != 0:
    c2 = ca//20
    cb = ca%20
    print(f'Total de cédulas de R$20: {c2}')
    if cb != 0:
        c3 =cb//10
        cc = cb%10
        print(f'Total de cédulas de R$10: {c3}')
        if cc != 0:
            c4 = cc//1
            print(f'Total de cédulas de R$1: {c4}')
print('Volte Sempre!')
#Resposta do Professor:
'''
valor = int(input('Quanto você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        total += 1
    else:
        if totced > 0:
            print(f'Total de  {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break'''