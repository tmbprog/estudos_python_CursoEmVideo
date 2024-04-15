# Pergunte o salário e calcule o aumento. Para > 1.250 aumento de 10%, para <= aumento de 15%
s = float(input('Salário atual: R$'))
a10 = s + (s*10/100)
a15 = s + (s*15/100)
if s > 1250:
    print(f'Seu novo salário será: R${a10:.2f}')
if s <= 1250:
    print(f'Seu novo salário será: R${a15:.2f}')