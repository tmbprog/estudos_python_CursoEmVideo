# Verificar se um ano é bissexto
from datetime import date
n = int(input('Digite um ano qualquer ou 0 para analisar o ano atual:'))
if n == 0:
    n = date.today().year
# Serve para pegar o ano atual da máquina
if (n%4==0 and n%100!=0 or n%400==0):
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')